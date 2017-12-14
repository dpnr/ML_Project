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

def decisionTrees(num_trees):
    convert.convertFile('data-splits/data.train')
    train_result = dataoperations.reg_getData(['output.test'])

    train_dataset = train_result["data"]
    trainingLines = open('output.test').readlines()

    convert.convertFile('data-splits/data.test')
    test_result = dataoperations.reg_getData(['output.test'])

    test_dataset = test_result['data']

    ###Random forests on decision trees

    print('\n\n##### Running Random Forests on Decision trees #####\n')
    randomTrees = []
    tree_count = 0

    for m in range(0,num_trees):
        tree_count += 1
        print "\nBuilding Tree " + str(tree_count) + '\n'
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
        entropy = Buildtree.calculateEntropy(tmp_dataset,tmp_features,3)
        print(entropy)
        attributes = entropy.keys()
        
        tree = Buildtree.buildtree(Node.Node(' ',tmp_dataset,attributes," "," ",'',entropy),'')



        ##send the sample as the train data to the classifier
        randomTrees.append(tree)





    # # ## prediction 

    print("\n\n########################## Accuracy on train Data of depth "+str(3) +" #########################\n")
    print(predict.getAccuracy_trees(train_dataset,randomTrees))

    print("\n\n########################## Accuracy on test Data of depth "+str(3) +" #########################\n")
    print(predict.getAccuracy_trees(test_dataset,randomTrees))