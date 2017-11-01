import getNumber

def getfeedback(line,train,r):
    #get a random value from -0.01 to 0.01
    #we need to calculate y(wx+b) value
    terms = line.split()
    
    y= float(terms[0])
    if(y == 0.0):
        y = -1.0
    
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
    result = y*(wx+train.getbias())

    if(result<=0):
        #change the weight vector to w+yx
        train.bias += r*y
        train.updates += 1
        for key in xvector:
            newWeight = float(weights[key])+r*y*float(xvector[key])
            train.updateWeight(key, newWeight)
    else:
        pass

def getfeedback_margin(line,train,r,margin):
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
    result = y*(wx+train.getbias())

    if(result<=margin):
        #change the weight vector to w+yx
        train.bias += r*y
        train.updates += 1
        for key in xvector:
            newWeight = float(weights[key])+r*y*float(xvector[key])
            train.updateWeight(key, newWeight)
    else:
        pass
    

def getfeedback_average(line,train,r):
    #get a random value from -0.01 to 0.01
    #we need to calculate y(wx+b) value
    terms = line.split()
    y= float(terms[0])
    
    xvector = {}
    wx = 0.0
    weights =train.getWeights()
    avg_weights = train.getAvgWeights()
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
            train.updateAvgWeight(key,getNumber.getRandom())
        wx += float(avg_weights[key])*float(xvector[key])
    # now once we got the wx value we add the bias and then multiply with label
    result = y*(wx+train.getavgbias())

    if(result<=0):
        #change the weight vector to w+yx
        train.bias += r*y
        for key in xvector:
            newWeight = float(weights[key])+r*y*float(xvector[key])
            train.updateWeight(key, newWeight)
    else:
        pass
    
    train.updates += 1
    #we have to update the average wright and bias no matter what for every example
    for key in weights:
        train.updateAvgWeight(key,weights[key]+avg_weights[key] )
        train.avg_bias += train.getbias() 

def getfeedback_aggressive(line,train,mu):
    #get a random value from -0.01 to 0.01
    #we need to calculate y(wx+b) value
    terms = line.split()
    y= float(terms[0])
    
    xvector = {}
    wx = 0.0
    xtx = 0.0
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
        xtx += float(xvector[key])*float(xvector[key])
    # now once we got the wx value we add the bias and then multiply with label
    result = y*(wx+train.getbias())

    if(result<=0):
        train.updates += 1
        # now once we got the wx value we add the bias and then multiply with label
        result = y*(wx+train.getbias())
        #here we use the aggressive learning rate which we calculate and store in agg_rate
        agg_rate = (mu-(y*wx))/(xtx+1)
        #change the weight vector to w+yx
        train.bias += agg_rate*y
        for key in xvector:
            newWeight = float(weights[key])+agg_rate*y*float(xvector[key])
            train.updateWeight(key, newWeight)
    else:
        pass