testing = {"alphabet":0,"first_same":0,"complete":0,"undefined":0}
import Buildtree
import dataoperations
import features
import Node





def predict(item,tree,attr):

    result = tree.label
    ##traverse through tree till you find a bucket with label
    if(len(tree.getChildren()) == 1):
        child = tree.getChildren()[:]

        return child[0].label

    elif(tree.label in ['+','-'] and len(tree.getChildren()) != 1):
        return tree.label

    elif(tree.value in ['last_even'] and len(tree.getChildren())<2 ):
        
        if(tree.label not in ['+','-']):
            for child in tree.getChildren()[:]:
                if(child.value in ['alphabet','first_same','complete']):
                    testing[child.value] += 1
                else:
                    testing['undefined'] += 1
            return '+'

    
    else:
        children = tree.getChildren()[:]
        if(len(children)!=0):
                    
                    if(item[attr] == children[0].target ):
                    
                        # if(item['name'] in testvariable.test):
                                                
                        #     for child in children:
                        #        pass

                        result = predict(item,children[0],tree.entropy[attr])  
                        
                    else:
                        result = predict(item,children[1],tree.entropy[attr])
                          
                                        
                 
        else:
            print('no children')
            

    return result              

def getAccuracy(dataset,tree):
    count = {"-":0,"+":0,"undefined":0}
    prediction = {"correct":0,"wrong":0}
    for item in dataset:
        test=predict(item,tree,tree.entropy['best'])
        if(test == "-"):
            count['-'] += 1
        elif(test == "+"):
            count['+'] += 1
        else:
            
            count['undefined'] += 1
        
        if(item['result']==test):
            prediction['correct'] += 1
        else:
            prediction['wrong'] += 1

    # print(count)
    # print(prediction)
    
    accuracy = ((prediction['correct']+0.0)/(prediction['correct']+prediction['wrong']))*100
   
        
    return accuracy

def getCrossAcc(num):
#we need do the cross validation
    cross_accurracies =[]
    file_input = ['Updated_Dataset/Updated_CVSplits/updated_training00.txt','Updated_Dataset/Updated_CVSplits/updated_training01.txt','Updated_Dataset/Updated_CVSplits/updated_training02.txt','Updated_Dataset/Updated_CVSplits/updated_training03.txt']
    
    for filename in file_input:
        
        files = file_input[:]
       
        
        test_dataset = dataoperations.getData([filename])
        test_dataset = features.addFeatures(test_dataset)
        
        files.remove(filename)
        train_dataset = dataoperations.getData(files)
        train_dataset = features.addFeatures(train_dataset)
        #update the entropy based on the depth
        entropy = Buildtree.calculateEntropy(train_dataset,num)
        tree = Buildtree.buildtree(Node.Node(' ',train_dataset,[]," "," ",'',entropy),'')
        cross_accurracies.append(getAccuracy(test_dataset,tree))

    print("\nstandard deviation")
    print(dataoperations.standard_deviation(cross_accurracies))    
    print("------------------")
    print("Accuracy")
   
    return sum(cross_accurracies) / float(len(cross_accurracies))
       

    
            


            



