import getNumber
import Perceptron
import prediction


def crossvalidation_svm():
    print("\n\n##### Running Cross Validation for the SVM #####\n" )
    results = {}
    gammas = [0.0001]
    Cs = [10]
    trainfiles = ['data/CVSplits/training00.data','data/CVSplits/training01.data','data/CVSplits/training02.data','data/CVSplits/training03.data','data/CVSplits/training04.data']
    
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for c in Cs:
        #we need to run for 10 epochs
        for gamma in gammas:
            crossValidations = []
            for index,filename in enumerate(trainfiles):
            
                testfile = trainfiles[index]
                print('taking %s as test file'%(testfile))
                tobetrainedon = trainfiles[:]
                tobetrainedon.remove(testfile)
                dataset =  getNumber.getData(tobetrainedon)
                train = Perceptron.simplePerceptron(dataset,False)
                print("perceptron created")
                for i in range(0,1):
                    train.runtraining_svm(gamma,c) 
                    print("training completed")
                    predictionResults = prediction.getprediction(train,testfile,False)
                    print("prediction completed")
                    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
                
                crossValidations.append(accuracy)
            
            average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
            print('length is %d'%(len(crossValidations)))
            print("Cross Validation accuracy for gamma and C = %s"%(" ".join([str(gamma),str(c)])))
            
            results[" ".join([str(gamma),str(c)])] =  average
            print('Accuracy is %.2f'%(average))
    
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = key
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper

def crossvalidation_logistic():
    print("\n\n##### Running Cross Validation for the Logistic #####\n" )
    results = {}
    gammas = [0.01]
    sigma2s = [100]
    trainfiles = ['data/CVSplits/training00.data','data/CVSplits/training01.data','data/CVSplits/training02.data','data/CVSplits/training03.data','data/CVSplits/training04.data']
    
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for sigma2 in sigma2s:
        #we need to run for 10 epochs
        for gamma in gammas:
            crossValidations = []
            for index,filename in enumerate(trainfiles):
            
                testfile = trainfiles[index]
                print('taking %s as test file'%(testfile))
                tobetrainedon = trainfiles[:]
                tobetrainedon.remove(testfile)
                dataset =  getNumber.getData(tobetrainedon)
                train = Perceptron.simplePerceptron(dataset,False)
                
                for i in range(0,2):
                    train.runtraining_log(gamma,sigma2) 
                    predictionResults = prediction.getprediction_log(train,testfile,False)
                    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
                
                crossValidations.append(accuracy)
            
            average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
            print('length is %d'%(len(crossValidations)))
            print("Cross Validation accuracy for gamma and sigma^2 = %s"%(" ".join([str(gamma),str(sigma2)])))
            
            results[" ".join([str(gamma),str(sigma2)])] =  average
            print('Accuracy is %.2f'%(average))
    
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = key
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper


def crossvalidation_naive():
    print("\n\n##### Running Cross Validation for the Naive #####\n" )
    results = {}
    smoothingValues = [2.0,1.5,1.0,0.5]
    trainfiles = ['data/CVSplits/training00.data','data/CVSplits/training01.data','data/CVSplits/training02.data','data/CVSplits/training03.data','data/CVSplits/training04.data']
    
    
    #we need to run for 10 epochs
    for value in smoothingValues:
        crossValidations = []
        for index,filename in enumerate(trainfiles):
        
            testfile = trainfiles[index]
            print('taking %s as test file'%(testfile))
            tobetrainedon = trainfiles[:]
            tobetrainedon.remove(testfile)
            train =  getNumber.getData_Naive(tobetrainedon,value)
            print("completed")
            for i in range(0,2):
                
                predictionResults = prediction.getprediction_naive(train,testfile,value)
                accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
            
            crossValidations.append(accuracy)
        
        average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
        print('length is %d'%(len(crossValidations)))
        print("Cross Validation accuracy for smoothing value = %s"%(value))
        
        results[value] =  average
        print('Accuracy is %.2f'%(average))
    
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = key
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper

def crossvalidation_svm_dt():
    print("\n\n##### Running Cross Validation for the SVM Decision trees #####\n" )
    results = {}
    gammas = [1,0.1,0.01,0.001,0.00001]
    Cs = [10,1,0.1,0.01,0.001,0.0001]
    trainLines = open('decisionTrees_svm.input').readlines()
    partition = len(trainLines)/5
    for index in range(0,5):
        data = trainLines[index*partition:(index+1)*partition]
        filename = "".join(["data/CVSplits/training0",str(index),".svm"])
        output = open(filename,'w')
        for line in data:
            output.write(line)
            
        
    trainfiles = ['data/CVSplits/training00.svm','data/CVSplits/training01.svm','data/CVSplits/training02.svm','data/CVSplits/training03.svm']
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for c in Cs:
        #we need to run for 10 epochs
        for gamma in gammas:
            crossValidations = []
            for index,filename in enumerate(trainfiles):
            
                testfile = trainfiles[index]
                print('taking %s as test file'%(testfile))
                tobetrainedon = trainfiles[:]
                tobetrainedon.remove(testfile)
                dataset =  getNumber.getData(tobetrainedon)
                train = Perceptron.simplePerceptron(dataset,False)
                
                for i in range(0,1):
                    train.runtraining_svm(gamma,c) 
                    predictionResults = prediction.getprediction(train,testfile,False)
                    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
                
                crossValidations.append(accuracy)
            
            average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
            print('length is %d'%(len(crossValidations)))
            print("Cross Validation accuracy for gamma and C = %s"%(" ".join([str(gamma),str(c)])))
            
            results[" ".join([str(gamma),str(c)])] =  average
            print('Accuracy is %.2f'%(average))
    
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = key
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper

def crossvalidation_logistic_dt():
    print("\n\n##### Running Cross Validation for the Logistic Decision trees #####\n" )
    results = {}
    gammas = [1,0.1,0.01,0.001,0.0001,0.00001]
    sigma2s = [0.1,1,10,100,1000,10000]
    trainfiles = ['data/CVSplits/training00.svm','data/CVSplits/training01.svm','data/CVSplits/training02.svm','data/CVSplits/training03.svm']
    
    
    #run the training for one hyper parameter for 10 epochs
    #test file is 
    for sigma2 in sigma2s:
        #we need to run for 10 epochs
        for gamma in gammas:
            crossValidations = []
            for index,filename in enumerate(trainfiles):
            
                testfile = trainfiles[index]
                print('taking %s as test file'%(testfile))
                tobetrainedon = trainfiles[:]
                tobetrainedon.remove(testfile)
                dataset =  getNumber.getData(tobetrainedon)
                train = Perceptron.simplePerceptron(dataset,False)
                
                for i in range(0,2):
                    train.runtraining_log(gamma,sigma2) 
                    predictionResults = prediction.getprediction_log(train,testfile,False)
                    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
                
                crossValidations.append(accuracy)
            
            average = reduce(lambda x, y: x + y, crossValidations) / len(crossValidations)
            print('length is %d'%(len(crossValidations)))
            print("Cross Validation accuracy for gamma and sigma^2 = %s"%(" ".join([str(gamma),str(sigma2)])))
            
            results[" ".join([str(gamma),str(sigma2)])] =  average
            print('Accuracy is %.2f'%(average))
    
    values = results.values()[:]
    max_value = max(values)
    key = getNumber.getKey(results,max_value)
    best_hyper = key
    print('Cross validation accuracy for the best hyperparameter is %.2f'%(max_value))
    return best_hyper
