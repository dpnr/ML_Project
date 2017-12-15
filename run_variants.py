import math
import features
import formulas
import Buildtree
import Node
import predict
import dataoperations
import run_variants
import convert
import numpy as np
import random
import Perceptron
import training
import getNumber
import prediction
import generate

def decisionTrees(num_trees):
    convert.convertFile('data-splits/data.train')
    train_result = dataoperations.reg_getData(['output.test'])

    train_dataset = train_result["data"]
    trainingLines = open('output.test').readlines()

    convert.convertFile('data-splits/data.test')
    test_result = dataoperations.reg_getData(['output.test'])

    test_dataset = test_result['data']

    convert.convertFile('data-splits/data.eval.anon')
    anon_result = dataoperations.reg_getData(['output.test'])

    anon_dataset = anon_result['data']

    ###Random forests on decision trees

    print('\n\n##### Running Random Forests on Decision trees #####\n')
    randomTrees = []
    tree_count = 0

    for m in range(0,num_trees):
        tree_count += 1
        print("\nBuilding Tree " + str(tree_count) + '\n')
        sample = []
        outputfile_tmp = open('tem.output','w')

        # train_features = train_result["features"] #FIXME

        np.random.shuffle(trainingLines)

        while(len(sample) <= 0.60*(len(trainingLines))):
            randomindex = random.randrange(len(trainingLines))
            outputfile_tmp.write(trainingLines[randomindex])
            sample.append(trainingLines[randomindex])
        
        
            

        tmp_result = dataoperations.reg_getData(['tem.output'])    
        tmp_dataset = tmp_result['data']
        tmp_features = tmp_result['features']

        print("\nCalculating Entropy...")
        entropy = Buildtree.calculateEntropy(tmp_dataset,tmp_features,15)
        print(entropy)
        attributes = entropy.keys()
        
        tree = Buildtree.buildtree(Node.Node(' ',tmp_dataset,attributes," "," ",'',entropy),'')



        ##send the sample as the train data to the classifier
        randomTrees.append(tree)





    # # ## prediction 

    print("\n\n########################## Accuracy on train Data  #########################\n")
    print(predict.getAccuracy_trees(train_dataset,randomTrees,'svm_input.train',False))
    print len(train_dataset)

    print("\n\n########################## Accuracy on test Data  #########################\n")
    print(predict.getAccuracy_trees(test_dataset,randomTrees,'svm_input.test',False))

    print("\n\n########################## Accuracy on anon data  #########################\n")
    print len(anon_dataset)
    print(predict.getAccuracy_trees(anon_dataset,randomTrees,'svm_input.anon',True))





def svm_dt(gamma,c):
    print('\n\n##### Running SVM Decision trees #####\n')
    accuracies_margin = {}
    weights_margin = {}
    bias_margin = {}
    train = Perceptron.simplePerceptron(getNumber.getData(['svm_input.train']),False)

    for i in range(0,10):##number of epochs
        
        train.runtraining_svm(gamma,c) #from the cross validation I got 0.1 as my optimal value for the learning rate
        predictionResults = prediction.getprediction(train,'svm_input.test',False)
        accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
        accuracies_margin[i]=accuracy
        print('Epoch %d Accuracy = %.2f'%(i+1,accuracy))
        weights_margin[i]=train.getWeights()
        bias_margin[i]=train.getbias()

    max_acc_index = getNumber.getKey(accuracies_margin,max(accuracies_margin.values()))
    print('Total number of updates the learning algorithm performs on the training set is %d'%(train.updates))
    print('Train Set accuracy is %.2f'%(max(accuracies_margin.values())))
    optimal_weights = weights_margin[max_acc_index]
    optimal_bias = bias_margin[max_acc_index] 
    
    
    for key in optimal_weights:
        train.updateWeight(key,optimal_weights[key])
    train.bias = optimal_bias

    generate.values(train,'svm_input.anon',False,"DT_SVM")
    
    predictionResults = prediction.getprediction(train,'svm_input.anon',False)
    print(predictionResults)
    accuracy = predictionResults['correct']*100.0/(predictionResults['wrong'] + predictionResults['correct'])
    print("optimal accuracy for SVM on Test set is %.2f"%(accuracy))