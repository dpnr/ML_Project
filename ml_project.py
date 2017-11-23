import getNumber
import training
import prediction
import validation
import Perceptron
import runvariants
import convert



#Uncomment the below for running the cross validation

# for the Majority baseline
# runvariants.majorityBaseline()




#SIMPLE PERCEPTRON

datatset = getNumber.getData(['training01.data','training02.data','training03.data','training04.data'])
# print datatset

for filename in ['training00.data','training01.data','training02.data','training03.data','training04.data','data-splits/data.train','data-splits/data.test','data-splits/data.eval.anon']:
    convert.convertFile(filename,".".join([filename,"nor"]))

n = validation.crossvalidation()
n_svm_r = float(n[:n.index(" ")])
n_svm_c = float(n[n.index(" ")+1:])
runvariants.svm(n_svm_r,n_svm_c)


# #DYNAMIC LEARNING RATE 

# n_dynamic = validation.crossvalidation_dynamic()
# print "Best learning rate is %.3f"%(n_dynamic)
# runvariants.dynamicPerceptron(n_dynamic)

# #MARGIN PERCEPTRON 

# n_margin = validation.crossvalidation_margin()
# print "Best learning rate is %s and margin is %s"%(n_margin[:n_margin.index(" ")],n_margin[n_margin.index(" ")+1:])
# n_margin_n = float(n_margin[:n_margin.index(" ")])
# n_margin_m = float(n_margin[n_margin.index(" ")+1:])
# runvariants.marginPerceptron(n_margin_n,n_margin_m)


#AVERAGE

# n_avg = validation.crossvalidation_avg()
# print "Best learning rate is %.3f"%(n_avg)
# runvariants.averagePerceptron(n_avg)



#AGRRESSIVE

# n_agg = validation.crossvalidation_aggressive()
# print "Best mu value is %.3f"%(n_agg)
# runvariants.aggressivePerceptron(n_agg)



