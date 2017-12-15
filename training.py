import getNumber
import math

def getfeedback_svm(line,train,gamma,c,t):
    #get a random value from -0.01 to 0.01
    #we need to calculate y(wx+b) value
    terms = line.split()
    y= float(terms[0])
    
    xvector = {}
    wx = 0.0
    weights =train.getWeights()
    weight_indexes = weights.keys()[:]
    index = -1 
    for term in terms:
        index += 1

        if(index!=0):
            key = term[:term.index(':')]
            value = term[term.index(":")+1:]
            xvector[key] = value
    # we got the x vector 
    # now we need to calculate y(wx+b)
    # first we will calculate w

    for key in xvector:
        #see if there is weight vector already present for that index or not
        # print "guessing this takes time"
        if key in weight_indexes:
            pass
        else:
            train.updateWeight(key,getNumber.getRandom())
        wx += float(weights[key])*float(xvector[key])
        # print "done"
    # now once we got the wx value we add the bias and then multiply with label
    result = y*(wx+train.getbias())
    gamma_t = gamma /(1 + (gamma*t/c))
    if(result<=1):
        #change the weight vector to w+yx
        train.bias = (1-gamma_t)*train.bias + (gamma_t*c*y)
        train.updates += 1
        
        for key in xvector:
            newWeight = (1-gamma_t)*float(weights[key]) + gamma_t*c*y*float(xvector[key])
            train.updateWeight(key, newWeight)
        
    else:
        train.bias = (1-gamma_t)*train.bias 
        train.updates += 1
        
        for key in xvector:
            newWeight = (1-gamma_t)*float(weights[key]) 
            train.updateWeight(key, newWeight)
        
    

def getfeedback_logistic(line,train,gamma,sigma2,t):
    #get a random value from -0.01 to 0.01
    #we need to calculate y(wx+b) value
    terms = line.split()
    y= float(terms[0])
    
    xvector = {}
    wx = 0.0
    weights =train.getWeights()
    weight_indexes = weights.keys()[:]
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
            train.updateWeight(key,getNumber.getRandom())
        wx += float(weights[key])*float(xvector[key])
    # now once we got the wx value we add the bias and then multiply with label
    
    
    wx = round(wx,2)
    gamma_t = gamma /(1 + t)
    
    #update the weight vector no matter what
    train.bias = (1-2*gamma_t/sigma2)*train.bias + (gamma_t*(y*math.exp(-1*y*train.bias)/(1+ math.exp(-1*y*train.bias) )))
    try:
        term1 = (1-2*gamma_t/sigma2)
        term2 = ( gamma_t * y * math.exp(-1*y*wx) )/(1+math.exp(-1*y*wx)) 
    except OverflowError:
        term2 = float(222222222)


    train.updates += 1
    for key in xvector:
        newWeight = (term1)*float(weights[key]) + (term2*float(xvector[key]))
        train.updateWeight(key, newWeight)
    