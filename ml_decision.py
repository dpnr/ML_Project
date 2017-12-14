import math
import features
import formulas
import Buildtree
import Node
import predict
import dataoperations
import convert

#reading the training data

## reading the training the data

convert.convertFile('data-splits/data.train')

train_dataset = dataoperations.reg_getData(['output.test'])
reg_traindataset = dataoperations.getData(['data-splits/data.test'])



## adding the features to the dataset

# train_dataset = features.addFeatures(train_dataset)# features already present

# print("dataset with features looks like")
# print(train_dataset)
## calculating entropy for every attribute

entropy = Buildtree.calculateEntropy(reg_traindataset,7)


attributes = entropy.keys()

convert.convertFile('data-splits/data.test')
test_dataset = dataoperations.reg_getData(['output.test'])

# # test_dataset = features.addFeatures(test_dataset)
convert.convertFile('data-splits/data.eval.anon')
anon_dataset = dataoperations.reg_getData(['output.test'])



tree = Buildtree.buildtree(Node.Node(' ',train_dataset,attributes," "," ",'',entropy),'')


# print "\n ###### END OF TREE ######\n"
# tree.displayNode(tree)



# # ## prediction 

print("\n\n########################## Accuracy on train Data of depth"+str(7) +"#########################\n")
print(predict.getAccuracy(train_dataset,tree))


print("\n\n########################## Accuracy on test Data of depth"+str(7) +"#########################\n")
print(predict.getAccuracy(test_dataset,tree))


print("\n\n########################## Accuracy on anon Data of depth"+str(7) +"#########################\n")
print(predict.getAccuracy(anon_dataset,tree))

# print("\n\n########################## cross accuracy #########################\n")

# for i in range (1,21):
#     print("#### For depth %d #####"%i)
#     print(predict.getCrossAcc(i))

#     print('\n=======================\n')




#  ### best accuracy on test data


    
# entropy = Buildtree.calculateEntropy(train_dataset,6)





# tree = Buildtree.buildtree(Node.Node(' ',train_dataset,attributes," "," ",'',entropy),'')


# print("\n\n######    ACCURACY VALUES AFTER LIMITING DEPTH   #####\n\n")

# ## prediction 

# print("\n\n########################## Accuracy on train Data after calculating limiting depth #########################\n")
# print(predict.getAccuracy(train_dataset,tree))


# print("\n\n########################## Accuracy on test Data after calculating limiting depth #########################\n")
# print(predict.getAccuracy(test_dataset,tree))














    



