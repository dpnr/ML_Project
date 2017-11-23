# we need to train the classifier for 20 epochs
import getNumber
import prediction
import Perceptron
import generate



def majorityBaseline():
    print('\n#####Running Majority Baseline#####\n')
    stats = getNumber.getStats('phishing.train')
    majority_label = getNumber.getBest(stats)
    stats_test = getNumber.getStats('phishing.test')
    accuracy_test = stats_test[majority_label]*100.0/sum(stats_test.values())
    print 'Test accuracy is %.2f'%(accuracy_test)
    stats_dev = getNumber.getStats('phishing.dev')
    accuracy_dev = stats_dev[majority_label]*100.0/sum(stats_dev.values())
    print 'Dev accuracy is %.2f'%(accuracy_dev)

def simplePerceptron(n):
    print('\n#####Running Simple Perceptron#####\n')
    accuracies_simple = {}
    weights_simple = {}
    bias_simple = {}
    train = Perceptron.simplePerceptron(getNumber.getData(['data-splits/data.train']),False)
    for i in range(0,20):
        train.runtraining(n) #from the cross validation I got 0.1 as my optimal value for the learning rate
        predictionResults = prediction.getprediction(train,'data-splits/data.test',False)
        accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
        accuracies_simple[i]=accuracy
        print('Epoch %d Accuracy = %.2f'%(i+1,accuracy))
        weights_simple[i]=train.getWeights()
        bias_simple[i]=train.getavgbias()

    max_acc_index = getNumber.getKey(accuracies_simple, max(accuracies_simple.values()))
    print('Total number of updates the learning algorithm performs on the training set is %d'%(train.updates))
    print('Test Set accuracy is %.2f'%(max(accuracies_simple.values())))
    optimal_weights = weights_simple[max_acc_index]
    optimal_bias = bias_simple[max_acc_index]
    #assign the optimal weights and bias to the classifier trained
    for key in optimal_weights:
        train.updateWeight(key,optimal_weights[key])
    train.bias = optimal_bias
    ##generate the results for the dataset
    generate.values(train,'data-splits/data.eval.anon',False,"simplePerceptron")
    predictionResults = prediction.getprediction(train,'data-splits/data.test',False)
    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
    print("optimal accuracy for simple perceptron on Test set is %.2f"%(accuracy))

def dynamicPerceptron(n_dynamic):
    # #DYNAMIC LEARNING RATE 
    print('\n#####Running Dynamic Perceptron#####\n')
    accuracies_dynamic = {}
    weights_dynamic = {}
    bias_dynamic = {}
    train = Perceptron.simplePerceptron(getNumber.getData(['data-splits/data.train']),True)

    for i in range(0,20):
        
        train.runtraining(n_dynamic/(1+i)) #from the cross validation I got 0.1 as my optimal value for the learning rate

        predictionResults = prediction.getprediction(train,'data-splits/data.train',False)
        accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
        accuracies_dynamic[i]=accuracy
        print('Epoch %d Accuracy = %.2f'%(i+1,accuracy))
        weights_dynamic[i]=train.getWeights()
        bias_dynamic[i]=train.getbias()
        
    
    
    max_acc_index = getNumber.getKey(accuracies_dynamic,max(accuracies_dynamic.values()) )
    print('Total number of updates the learning algorithm performs on the training set is %d'%(train.updates)) 
    print('Development Set accuracy is %.2f'%(max(accuracies_dynamic.values())))
    optimal_weights = weights_dynamic[max_acc_index]
    optimal_bias = bias_dynamic[max_acc_index]
    
    train.runtraining(n_dynamic)
    for key in optimal_weights:
        train.updateWeight(key,optimal_weights[key])
    train.bias = optimal_bias


    generate.values(train,'data-splits/data.eval.anon',False,"dynamicPerceptron")
    predictionResults = prediction.getprediction(train,'data-splits/data.test',False)
    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
    print("optimal accuracy for dynamic learning rate on Test set is %.2f"%(accuracy))

#MARGIN PERCEPTRON 
def marginPerceptron(n_margin_n,n_margin_m):
    print('\n#####Running Margin Perceptron#####\n')
    accuracies_margin = {}
    weights_margin = {}
    bias_margin = {}
    train = Perceptron.simplePerceptron(getNumber.getData(['data-splits/data.train']),False)

    for i in range(0,20):
        
        train.runtraining_margin(n_margin_n,n_margin_m) #from the cross validation I got 0.1 as my optimal value for the learning rate
        predictionResults = prediction.getprediction(train,'data-splits/data.train',False)
        accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
        accuracies_margin[i]=accuracy
        print('Epoch %d Accuracy = %.2f'%(i+1,accuracy))
        weights_margin[i]=train.getWeights()
        bias_margin[i]=train.getbias()

    max_acc_index = getNumber.getKey(accuracies_margin,max(accuracies_margin.values()))
    print('Total number of updates the learning algorithm performs on the training set is %d'%(train.updates))
    print('Development Set accuracy is %.2f'%(max(accuracies_margin.values())))
    optimal_weights = weights_margin[max_acc_index]
    optimal_bias = bias_margin[max_acc_index] 
    
    
    for key in optimal_weights:
        train.updateWeight(key,optimal_weights[key])
    train.bias = optimal_bias

    generate.values(train,'data-splits/data.eval.anon',False,"marginPerceptron")
    predictionResults = prediction.getprediction(train,'data-splits/data.test',False)
    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
    print("optimal accuracy for Margin Perceptron on Test set is %.2f"%(accuracy))

#AVERAGE PERCEPTRON
def averagePerceptron(n_avg):
    print('\n#####Running Average Perceptron#####\n')
    accuracies_avg = {}
    weights_avg = {}
    bias_avg = {}
    train = Perceptron.simplePerceptron(getNumber.getData(['data-splits/data.train','data-splits/data.test']),False)

    for i in range(0,20):
    
        train.runtraining_average(n_avg) #from the cross validation I got 0.1 as my optimal value for the learning rate
        predictionResults = prediction.getprediction(train,'data-splits/data.train',True) ## BUG MAKE IT true for getting the average 
        accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
        accuracies_avg[i]=accuracy
        print('Epoch %d Accuracy = %.2f'%(i+1,accuracy))
        weights_avg[i]=train.getWeights()
        bias_avg[i]=train.getbias()

    max_acc_index = getNumber.getKey(accuracies_avg,max(accuracies_avg.values()))
    print('Total number of updates the learning algorithm performs on the training set is %d'%(train.updates))
    print('Development Set accuracy is %.2f'%(max(accuracies_avg.values())))
    optimal_weights = weights_avg[max_acc_index]
    optimal_bias = bias_avg[max_acc_index] 

    for key in optimal_weights:
        train.updateWeight(key,optimal_weights[key])
    train.bias = optimal_bias

    generate.values(train,'data-splits/data.eval.anon',False,"averagePerceptron")
    predictionResults = prediction.getprediction(train,'data-splits/data.test',True)  ## BUG MAKE IT true for getting the average 
    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
    print("optimal accuracy for Average perceptron on Test set is %.2f"%(accuracy))

#AGGRESSIVE PERCEPTRON

def aggressivePerceptron(n_agg,trainData):
    print('\n#####Running Aggressive Perceptron#####\n')
    accuracies_agg = {}
    weights_agg = {}
    bias_agg = {}
    train = Perceptron.simplePerceptron(trainData,False)

    for i in range(0,20):
        
        train.runtraining_aggressive(n_agg) #from the cross validation I got 0.1 as my optimal value for the learning rate
        predictionResults = prediction.getprediction([train],'data-splits/data.test.log',False) ## BUG MAKE IT true for getting the average 
        accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
        accuracies_agg[i]=accuracy
        print('Epoch %d Accuracy = %.2f'%(i+1,accuracy))
        weights_agg[i]=train.getWeights()
        bias_agg[i]=train.getbias()

    
    
    max_acc_index = getNumber.getKey(accuracies_agg,max(accuracies_agg.values()))
    print('Total number of updates the learning algorithm performs on the training set is %d'%(train.updates))
    print('Development Set accuracy is %.2f'%(max(accuracies_agg.values())))
    optimal_weights = weights_agg[max_acc_index]
    optimal_bias = bias_agg[max_acc_index] 

    for key in optimal_weights:
        train.updateWeight(key,optimal_weights[key])
    train.bias = optimal_bias

    return train

    # generate.values(train,'data-splits/data.eval.anon',False,"aggressivePerceptron")
    # predictionResults = prediction.getprediction(train,'data-splits/data.test',False)  ## BUG MAKE IT true for getting the average 
    # accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
    # print("optimal accuracy for Aggressive perceptron on Test set is %.2f"%(accuracy))
