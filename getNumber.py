import random
import math

def getRandom():
    return random.uniform(-0.01,0.01)


def getData(filenames):
    data= []
    return_dataset= []
    for filename in filenames:
        with open(filename) as train_file:
            for line in train_file:
                if(len(line.split())> 2):
                    data.append(line)
    
    return data


def getData_Naive(filenames,smoothing):
    data = getData(filenames)
    labels = getStats_files(filenames)
    labelstats = {}
    ## we only store the P(value= + / true) or P(value = - / false)
    for example in data:
        values  = example.split()
        present_label = values[0]
        for term in values[1:]:
            key = term[:term.index(':')]
            storeKey = "".join([key,"=+1","/",present_label])
            if storeKey in labelstats:
                labelstats[storeKey] += 1
            else:
                labelstats[storeKey] = smoothing
    

    labels["true"] += 40000*smoothing
    labels["false"] += 40000*smoothing
    ##divide by respective values and apply log
    labelstats = labelNormalize_logDiv(labels,labelstats)


    return labelstats





def labelNormalize_logDiv(labels,labelstats):
    for label in labelstats:
        presentvalue = float(labelstats[label])
        given = label[label.index('/')+1:]
        if(given=="1"):
            
            labelstats[label] = math.log(presentvalue/labels['true'],2)
        else:
            
            labelstats[label] = math.log(presentvalue/labels['false'],2)
    
    return labelstats

def getKey(dictionary,search_value):
    for key, value in dictionary.iteritems():
        if value == search_value:
            return key
    


def getStats(filename):
    
    labels = {"true":0,"false":0}
    train_data = getData([filename])
    for example in train_data:
        label = example[0:2]
        if(label=="-1"):
            labels['false'] += 1
        else:
            labels['true'] += 1
    return labels

def getStats_files(filenames):
    labels = {"true":0,"false":0}
    train_data = getData(filenames)
    for example in train_data:
        label = example[0:2]
        
        if(label=="-1"):
            labels['false'] += 1
        else:
            labels['true'] += 1
    return labels

def getBest(labels):
    max_index = labels.values().index(max(labels.values()))
    majority_label = labels.keys()[max_index]
    return majority_label