import math

def entropy(feature,dataset):
    
    total = len(dataset)
    plus=minus=plus_pos=plus_neg=minus_pos=minus_neg=plus_entropy=minus_entropy=entropy=0.0
    for item in dataset:
        
        if(item[feature] == "+"):
            plus += 1
            if(item['result'] == "+"):
                plus_pos += 1
            else:
                plus_neg += 1
        else:
            minus += 1
            if(item['result'] == "+"):
                minus_pos += 1
            else:
                minus_neg += 1
   
    if(plus==0 or minus==0):
        if(minus ==0):
            plus_entropy = -1*((plus_pos/plus)*math.log((plus_pos/plus),2) + (plus_neg/plus) * math.log((plus_neg/plus),2))
            return (plus/total)*(plus_entropy)
        else:
            minus_entropy = -1*((minus_pos/minus)*math.log((minus_pos/minus),2)+(minus_neg/minus)*math.log((minus_neg/minus),2))
            return (minus/total)*(minus_entropy)
    else:
        plus_entropy = -1*((plus_pos/plus)*math.log((plus_pos/plus),2) + (plus_neg/plus) * math.log((plus_neg/plus),2))
        minus_entropy = -1*((minus_pos/minus)*math.log((minus_pos/minus),2)+(minus_neg/minus)*math.log((minus_neg/minus),2))
        entropy = (plus/total)*(plus_entropy)+(minus/total)*(minus_entropy)
    
   
    return entropy
    


        

