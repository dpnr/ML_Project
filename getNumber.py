import random

def getRandom():
    return random.uniform(-0.01,0.01)


def getData(filenames):
    data= []
    return_dataset= []
    for filename in filenames:
        with open(filename) as train_file:
            for line in train_file:
                if(line != '\n'):
                    data.append(line)
    
    return data

def getKey(dictionary,search_value):
    for key, value in dictionary.iteritems():
        if value == search_value:
            return key


def getStats(filename):
    
    labels = {"true":0,"false":0}
    train_data = getData([filename])
    for example in train_data:
        label = example[0:2]
        if(label=="+1"):
            labels['true'] += 1
        else:
            labels['false'] += 1
    return labels

def getBest(labels):
    max_index = labels.values().index(max(labels.values()))
    majority_label = labels.keys()[max_index]
    return majority_label