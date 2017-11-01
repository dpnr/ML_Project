import getNumber
import Perceptron
import prediction

def crossvalidation():

    dataSplits = []
    ##lets split the training file into 5 parts
    # with open('data-splits/data.train','r') as file:
    #     data = file.read().split('\n')
    #     chunk = len(data)/5
    #     for i in range(0,5):
    #         if(i!=4):
    #           thisChunk = data[i*chunk:(i+1)*chunk]
    #         else:
    #           thisChunk = data[i*chunk:]
    #         #wirte into a file
    #         output = open('training0'+str(i)+'.data','w')
    #         for line in thisChunk:
    #             print >>output, line

    print("\n##### Running Cross Validation for the Simple Perceptron #####\n" )
    results = {'1':0,'0.1':0,'0.01':0}
    trainfiles = ['training00.data','training01.data','training02.data','training03.data','training04.data']
    trainedclassifiers = []
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for value in [1,0.1,0.01]:
        #we need to run for 10 epochs
        crossValidations = []
        for index,filename in enumerate(trainfiles):
            
            testfile = trainfiles[index]
            print('taking %s as test file'%(testfile))
            tobetrainedon = trainfiles[:]
            tobetrainedon.remove(testfile)
            dataset =  getNumber.getData(tobetrainedon)
            train = Perceptron.simplePerceptron(dataset,False)
            for i in range(0,10):
                # print('Running %d epoch'%(i+1))
                train.runtraining(value)
                predictionResults = prediction.getprediction(train,'data-splits/data.test',False)
                accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])    
            
            crossValidations.append(accuracy)
                 
        average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
        print("Cross Validation accuracy for learning rate = %.2f"%(value))
        results[str(value)] = average
        print 'Accuracy is %.2f'%(average)
    #lets send back the best hyperparameter
    values = results.values()[:]
    max_value = max(values)
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    key = getNumber.getKey(results,max_value)
    best_hyper = float(key)
    return best_hyper

def crossvalidation_dynamic():
    print("\n##### Running Cross Validation for the Dynamic Perceptron #####\n" )
    results = {}
    trainfiles = ['CVSplits/training00.data','CVSplits/training01.data','CVSplits/training02.data','CVSplits/training03.data','CVSplits/training04.data']
    trainedclassifiers = []
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for value in [1,0.1,0.01]:
        #we need to run for 10 epochs
        crossValidations = []
        for index,filename in enumerate(trainfiles):
            
            testfile = trainfiles[index]
            print('taking %s as test file'%(testfile))
            tobetrainedon = trainfiles[:]
            tobetrainedon.remove(testfile)
            dataset =  getNumber.getData(tobetrainedon)
            train = Perceptron.simplePerceptron(dataset,False)
            for i in range(0,10):
                train.runtraining(value/(1+i))
                predictionResults = prediction.getprediction(train,'phishing.dev',False)
                accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
                  
            crossValidations.append(accuracy)
                 
        average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
        print('length is %d'%(len(crossValidations)))
        print("Cross Validation accuracy for learning rate = %.2f"%(value))
        results[str(value)] =  average
        print 'Accuracy is %.2f'%(average)
    
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    best_hyper = float(key)
    return best_hyper


def crossvalidation_margin():
    print("\n##### Running Cross Validation for the Margin Perceptron #####\n" )
    results = {}
    margins = [1,0.1,0.01]
    trainfiles = ['CVSplits/training00.data','CVSplits/training01.data','CVSplits/training02.data','CVSplits/training03.data','CVSplits/training04.data']
    trainedclassifiers = []
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for value in [1,0.1,0.01]:
        #we need to run for 10 epochs
        for margin in margins:
            crossValidations = []
            for index,filename in enumerate(trainfiles):
            
                testfile = trainfiles[index]
                print('taking %s as test file'%(testfile))
                tobetrainedon = trainfiles[:]
                tobetrainedon.remove(testfile)
                dataset =  getNumber.getData(tobetrainedon)
                train = Perceptron.simplePerceptron(dataset,False)
                for i in range(0,10):
                    train.runtraining_margin(value,margin) 
                    predictionResults = prediction.getprediction(train,'phishing.dev',False)
                    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
                
                crossValidations.append(accuracy)
            
            average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
            print('length is %d'%(len(crossValidations)))
            print("Cross Validation accuracy for learning rate = %s"%(" ".join([str(value),str(margin)])))
            
            results[" ".join([str(value),str(margin)])] =  average
            print 'Accuracy is %.2f'%(average)
    
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = key
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper

def crossvalidation_avg():
    print("\n##### Running Cross Validation for the Average Perceptron #####\n" )
    results = {'1':0,'0.1':0,'0.01':0}
    trainfiles = ['CVSplits/training00.data','CVSplits/training01.data','CVSplits/training02.data','CVSplits/training03.data','CVSplits/training04.data']
    trainedclassifiers = []
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for value in [1,0.1,0.01]:
        #we need to run for 10 epochs
        crossValidations = []
        for index,filename in enumerate(trainfiles):

            testfile = trainfiles[index]
            print('taking %s as test file'%(testfile))
            tobetrainedon = trainfiles[:]
            tobetrainedon.remove(testfile)
            dataset =  getNumber.getData(tobetrainedon)
            train = Perceptron.simplePerceptron(dataset,False)
            for i in range(0,10):
                train.runtraining_average(value)
                predictionResults = prediction.getprediction(train,'phishing.dev',True)
                accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
                
            crossValidations.append(accuracy)
        
        average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
        print("Cross Validation accuracy for learning rate = %.2f"%(value))
        results[str(value)] = average
        print 'Accuracy is %.2f'%(average)
    #lets send back the best hyperparameter
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = float(key)
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper

def crossvalidation_aggressive():
    print("\n##### Running Cross Validation for the Aggressive Perceptron #####\n" )
    results = {'1':0,'0.1':0,'0.01':0}
    trainfiles = ['CVSplits/training00.data','CVSplits/training01.data','CVSplits/training02.data','CVSplits/training03.data','CVSplits/training04.data']
    trainedclassifiers = []
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for value in [1,0.1,0.01]:
        #we need to run for 10 epochs
        crossValidations = []
        for index,filename in enumerate(trainfiles):
            
            testfile = trainfiles[index]
            print('taking %s as test file'%(testfile))
            tobetrainedon = trainfiles[:]
            tobetrainedon.remove(testfile)
            dataset =  getNumber.getData(tobetrainedon)
            train = Perceptron.simplePerceptron(dataset,False)
            for i in range(0,10):
                train.runtraining_aggressive(value)
                predictionResults = prediction.getprediction(train,'phishing.dev',False)
                accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
            
            crossValidations.append(accuracy)
        
        average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
        print("Cross Validation accuracy for mu = %.2f"%(value))
        results[str(value)] = average
        print 'Accuracy is %.2f'%(average)
    #lets send back the best hyperparameter
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = float(key)
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper