


def getSortedEnt(entropy):
    presentvalue = min(entropy.values())
    keys = entropy.keys()[:]
    values = entropy.values()[:]
    presentindex = values.index(presentvalue)
    
    sortedentropy = {"best":keys[presentindex]}
    length = len(keys)
    for i in values:
        
        nextmin = min(minval for minval in values if minval > presentvalue)
        index = values.index(nextmin)
        sortedentropy[keys[presentindex]] = keys[index]
        presentindex = index
        presentvalue = nextmin
        if(nextmin == max(values)):
            sortedentropy[keys[presentindex]] = "complete"
            break
    

    return sortedentropy


def getEntLimiting(entropy,num):
    entropy_limited ={}
    if(num!=1):
        for i,item in enumerate(sorted(entropy, key=entropy.get, reverse=False)):
            
            if(i<=num-1):
                entropy_limited[item] = entropy[item]
        
    else:
        index = entropy.values().index(max(entropy.values()))
        entropy_limited["best"]=entropy.keys()[index]
        entropy_limited[entropy.keys()[index]] = 'complete'
       
        return entropy_limited
    return getSortedEnt(entropy_limited)