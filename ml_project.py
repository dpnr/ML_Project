import getNumber
import training
import prediction
import validation
import Perceptron
import runvariants
import random
import generate


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


##implementing bagging

dataset = getNumber.getData(['data-splits/data.train.log'])

## lets create m datasets each having 60% of total datasets
classifiers = []
for m in range(0,100):
    sample = [] 
    
    
    while(len(sample) < 0.6*len(dataset)):
        randomindex = random.randrange(len(dataset))
        sample.append(dataset[randomindex])



    ##send the sample as the train data to the classifier
    classifier = runvariants.aggressivePerceptron(1,sample)
    classifiers.append(classifier)

##### lets run the prediction from here

    
    

print "datasets created and classifiers created"

###lets get the predictions here

predictionResults = prediction.getprediction(classifiers,'data-splits/data.test.log',False)  ## MAKE IT true for getting the average 
print predictionResults
accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
print("optimal accuracy for Aggressive perceptron on Test set is %.2f"%(accuracy))
generate.values_bagging(classifiers,'data-splits/data.eval.anon.log',False,"aggressivePerceptron_bagging_log1")

# runvariants.aggressivePerceptron(n_agg)



