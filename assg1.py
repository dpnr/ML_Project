import math
import features
import formulas
import Buildtree
import Node
import predict
import dataoperations

#reading the training data




## reading the training the data

train_dataset = dataoperations.getData(['Updated_Dataset/updated_train.txt'])



## adding the features to the dataset

train_dataset = features.addFeatures(train_dataset)

## calculating entropy for every attribute
    
entropy = Buildtree.calculateEntropy(train_dataset,0)


attributes = entropy.keys()


test_dataset = dataoperations.getData(['Updated_Dataset/updated_test.txt'])

test_dataset = features.addFeatures(test_dataset)


tree = Buildtree.buildtree(Node.Node(' ',train_dataset,attributes," "," ",'',entropy),'')

# tree.displayNode(tree)
# print ("#### ROOT NODE")
# print tree.value
# print len(tree.children)
#print(len(tree.children))
print("\n\n######    ACCURACY VALUES    #####\n\n")

## prediction 

print("\n\n########################## Accuracy on train Data #########################\n")
print(predict.getAccuracy(train_dataset,tree))


print("\n\n########################## Accuracy on test Data #########################\n")
print(predict.getAccuracy(test_dataset,tree))

print("\n\n########################## cross accuracy #########################\n")

for i in range (1,21):
    print("#### For depth %d #####"%i)
    print(predict.getCrossAcc(i))

    print('\n=======================\n')




 ### best accuracy on test data


    
entropy = Buildtree.calculateEntropy(train_dataset,6)





tree = Buildtree.buildtree(Node.Node(' ',train_dataset,attributes," "," ",'',entropy),'')


print("\n\n######    ACCURACY VALUES AFTER LIMITING DEPTH   #####\n\n")

## prediction 

print("\n\n########################## Accuracy on train Data after calculating limiting depth #########################\n")
print(predict.getAccuracy(train_dataset,tree))


print("\n\n########################## Accuracy on test Data after calculating limiting depth #########################\n")
print(predict.getAccuracy(test_dataset,tree))














    



