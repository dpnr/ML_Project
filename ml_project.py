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

# datatset = getNumber.getData(['training01.data','training02.data','training03.data','training04.data'])
# print datatset
# n = validation.crossvalidation()
# print "Best learning rate is %.3f"%(n)
# runvariants.simplePerceptron(n)


# #DYNAMIC LEARNING RATE 

# n_dynamic = validation.crossvalidation_dynamic()
# print "Best learning rate is %.3f"%(n_dynamic)
# runvariants.dynamicPerceptron(n_dynamic)

# #MARGIN PERCEPTRON 

n_margin = validation.crossvalidation_margin()
print "Best learning rate is %s and margin is %s"%(n_margin[:n_margin.index(" ")],n_margin[n_margin.index(" ")+1:])
n_margin_n = float(n_margin[:n_margin.index(" ")])
n_margin_m = float(n_margin[n_margin.index(" ")+1:])
runvariants.marginPerceptron(n_margin_n,n_margin_m)


#AVERAGE

# n_avg = validation.crossvalidation_avg()
# print "Best learning rate is %.3f"%(n_avg)
# runvariants.averagePerceptron(n_avg)



#AGRRESSIVE

# for filename in ['training00.data','training01.data','training02.data','training03.data','training04.data','data-splits/data.train','data-splits/data.test','data-splits/data.eval.anon']:
#     convert.convertFile_log(filename,".".join([filename,"log"]))


# convertFile_scale

# for filename in ['training00.data','training01.data','training02.data','training03.data','training04.data','data-splits/data.train','data-splits/data.test','data-splits/data.eval.anon']:
#     convert.convertFile_scale(filename,".".join([filename,"scale"]))

n_agg = validation.crossvalidation_aggressive()
print "Best mu value is %.3f"%(n_agg)

runvariants.aggressivePerceptron(n_agg)



