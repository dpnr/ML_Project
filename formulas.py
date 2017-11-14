import math

def entropy(feature,dataset):
    

    total = len(dataset)
    plus=minus=plus_pos=plus_neg=minus_pos=minus_neg=plus_entropy=minus_entropy=entropy=0.0
    values = []
    entropy_values = {}
    ## here we have more than just two feature values
    for item in dataset:
        
        # if(item[feature] == "+"):
        #     plus += 1
        #     if(item['result'] == "+"):
        #         plus_pos += 1
        #     else:
        #         plus_neg += 1
        # else:
        #     minus += 1
        #     if(item['result'] == "+"):
        #         minus_pos += 1
        #     else:
        #         minus_neg += 1
        #################
        ##get the unique number of the values
        values.append(item[feature])
        if(item[feature] not in entropy_values):
            entropy_values[item[feature]] = {"positive":0,"negative":0}
        
        if(item['result'] == 0):
            entropy_values[item[feature]]["negative"] += 1
        else:
            entropy_values[item[feature]]["positive"] += 1

    values = list(set(values)) ##Only the unque ones stay inside this
    entropy = 0

    for value in values:
        
        thisTotal = float(entropy_values[value]["positive"] + entropy_values[value]["negative"])
        positive = float(entropy_values[value]["positive"] )
        negative = float(entropy_values[value]["negative"] )
        if(positive != 0.0 and negative != 0.0):
            subEntropy = -1*((positive/thisTotal)*math.log((positive/thisTotal),2) 
                            + (negative/thisTotal)*math.log((negative/thisTotal),2))
        elif(positive == 0.0 ):
            subEntropy = -1*((negative/thisTotal)*math.log((negative/thisTotal),2))
        elif(negative == 0.0 ):
            subEntropy = -1*((positive/thisTotal)*math.log((positive/thisTotal),2))
        
        entropy += (thisTotal/total)*subEntropy
    
   
    return entropy
    


        

