import getNumber

def getprediction(trainclass,filename,average):
    prediction= {"correct":0,"wrong":0}
    with open(filename) as testfile:
        for line in testfile:
            terms =line.split()
            true_label = float(terms[0])
            xvector = {}
            wx = 0.0
            if(average==False):
                weights =trainclass.getWeights()
                weight_indexes = weights.keys()[:]
                bias = trainclass.getbias()
            else:
                weights =trainclass.getAvgWeights()
                weight_indexes = weights.keys()[:]
                bias = trainclass.getavgbias()
            for index,term in enumerate(terms):
                if(index!=0):
                    key = term[:term.index(':')]
                    value = term[term.index(":")+1:]
                    xvector[key] = value
            # we got the x vector 
            # now we need to calculate y(wx+b)
            # first we will calculate wx
            for key in xvector:
                #see if there is weight vector already present for that index or not
                if key in weight_indexes:
                    pass
                else:
                    # print('seen a new x vector')
                    trainclass.updateWeight(key,getNumber.getRandom())
                    trainclass.updateAvgWeight(key,getNumber.getRandom())
                wx += float(weights[key])*float(xvector[key])

            result = true_label*(wx+bias)
            if(wx+bias>=1):
                predict = 1
            else:
                predict = -1

            if(true_label == predict):
                #change the weight vector to w+yx
                prediction['correct'] +=1
            else:
                prediction['wrong'] +=1
    return prediction



def getprediction_log(trainclass,filename,average):
    prediction= {"correct":0,"wrong":0}
    
    with open(filename) as testfile:
        for line in testfile:
            terms =line.split()
            true_label = float(terms[0])
            xvector = {}
            wx = 0.0
            if(average==False):
                weights =trainclass.getWeights()
                weight_indexes = weights.keys()[:]
                bias = trainclass.getbias()
            else:
                weights =trainclass.getAvgWeights()
                weight_indexes = weights.keys()[:]
                bias = trainclass.getavgbias()
            for index,term in enumerate(terms):
                if(index!=0):
                    key = term[:term.index(':')]
                    value = term[term.index(":")+1:]
                    xvector[key] = value
            # we got the x vector 
            # now we need to calculate y(wx+b)
            # first we will calculate wx
            for key in xvector:
                #see if there is weight vector already present for that index or not
                if key in weight_indexes:
                    pass
                else:
                    # print('seen a new x vector')
                    trainclass.updateWeight(key,getNumber.getRandom())
                    trainclass.updateAvgWeight(key,getNumber.getRandom())
                wx += float(weights[key])*float(xvector[key])

            result = true_label*(wx+bias)
            
            if(result<0):
                #change the weight vector to w+yx
                prediction['wrong'] +=1
            else:
                prediction['correct'] +=1
    return prediction


def getprediction_naive(train,filename,smoothing):
    prediction= {"correct":0,"wrong":0}
    
    with open(filename) as testfile:
        for line in testfile:
            terms =line.split()
            true_label = float(terms[0])
            probs = {"true":1,"false":1}
            for index,term in enumerate(terms):
                if(index!=0):
                    key = term[:term.index(':')]
                    storeKey_positive = "".join([key,"=+1","/","1"])
                    storeKey_negative = "".join([key,"=+1","/","-1"])
                    try:
                        probs["true"] *= train[storeKey_positive]
                    except:
                        probs["true"] *= (smoothing/40000*smoothing)
                    try:
                        probs["false"] *= train[storeKey_negative]
                    except:
                        probs["false"] *= (smoothing/40000*smoothing)

                
            if(probs["true"] >= probs["false"]):
                predicted = 1.0
            else:
                predicted = -1.0
            
            
            if(predicted == true_label):
                prediction["correct"] += 1
            else:
                prediction["wrong"] += 1
    return prediction