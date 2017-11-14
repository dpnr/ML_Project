import math

def getData(filenames):
    data= []
    return_dataset= []
    for filename in filenames:
        with open(filename) as train_file:
            for line in train_file:
                data.append(line)
    
            for ele in data:
                entry = {"result":float(ele[0:1])}
                features = ele[2:].split()
                for value in features:
                    entry[value[:value.index(':')]] = float(value[ value.index(':')+1 :])
                return_dataset.append(entry)

    return return_dataset

def reg_getData(filenames):
    data= []
    return_dataset= []
    for filename in filenames:
        with open(filename) as train_file:
            for line in train_file:
                data.append(line)
    
            for ele in data:
                if(len(ele)>3):
                    entry = {"result":ele[0:1]}
                    features = ele[2:].split()
                    for value in features:
                        entry[value[:value.index(':')]] = value[ value.index(':')+1 :]
                    return_dataset.append(entry)

    return return_dataset

def standard_deviation(values):
    
    num_items = len(values)
    mean = float(sum(values) / num_items)
    differences = [x - mean for x in values]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
 
    # Note: it would be better to return a value and then print it outside
    # the function, but this is just a quick way to print out the values along
    # the way.
    
        
    variance = float(ssd / num_items)
    
    sd = math.sqrt(variance)
    

    return sd