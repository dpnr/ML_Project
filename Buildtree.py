import formulas
import Node
import operator
import entropylist








def calculateEntropy(train_dataset,num):
    sorted_entropy={}
    entropy= {}
    keys = train_dataset[0].keys()
    for feature in keys:
        if(feature not in ['name','result']):
            entropy[feature] = formulas.entropy(feature,train_dataset)
    
    if(num==0):
        sorted_entropy = entropylist.getSortedEnt(entropy)
    else:
        sorted_entropy = entropylist.getEntLimiting(entropy,num)
    return sorted_entropy

def majority(node):
    maxfreq ={"+":0,"-":0}
    if(len(node.dataset)!=0):
        for value in node.dataset:
            if(value['result']=='+'):
                if(value['result'] in maxfreq.keys()):
                    maxfreq[value['result']] +=1
            else:
                if(value['result']=='-'):
                    if(value['result'] in maxfreq.keys()):
                         maxfreq[value['result']] +=1

            
    else:
        for value in node.parentNode.dataset:
            if(value['result']=='+'):
                if(value['result'] in maxfreq.keys()):
                    maxfreq[value['result']] +=1
            else:
                if(value['result']=='-'):
                    if(value['result'] in maxfreq.keys()):
                         maxfreq[value['result']] +=1
    
    maxvalue = max(maxfreq.values())
    index = maxfreq.values().index(maxvalue)
    return maxfreq.keys()[index]


def getValues(dataset,attribute):
    values = []
    for item in dataset:
        if(item[attribute] not in values):
            values.append(item[attribute])
    return values

def buildtree(node,root):
    sorted_entropy = node.entropy
    if(node.value==" "):
        node.value= sorted_entropy['best']
       
    
    dataset_result = {"+":[],"-":[]}
    dataset_node = {"+":[],"-":[]}
     # we know the dataset
    if(node.value=="complete"  or len(node.getDataset())==0 ):
        # print("###NODE VALUE")
        # print(node.value)
        return Node.Node(node.value,[],[],node.parentNode.dataset[0][node.parentNode.value],node,majority(node),sorted_entropy)
    
    else:
        for item in node.getDataset():
            if(item['result']=="+"):
                dataset_result["+"].append(item)
            else:
                dataset_result["-"].append(item)
        
        for item in node.getDataset():
            if(item[node.value]=="+"):
                dataset_node["+"].append(item)
            else:
                dataset_node["-"].append(item)
    

    if( len(dataset_result["+"])==0 or len(dataset_result["-"])==0):
       
        if(len(dataset_result["+"])==0):
            target = "+"
        elif(len(dataset_result["-"])==0):
            target = '-'
        else:
            target = majority(node)
        # print("###NODE VALUE")
        # print(node.value)
        return Node.Node(node.value,[],[],target,node,majority(node),sorted_entropy)
    else:
       for index,value in enumerate(getValues(node.getDataset(),node.value)):
                tree = buildtree(Node.Node(sorted_entropy[node.value],dataset_node[value],[],value,node,'',sorted_entropy),'')
                node.addChild(tree)
            
                
                
    
    ##split the data according to values and place as chidlren inside those nodes
    #print('return function')

    return node
    

