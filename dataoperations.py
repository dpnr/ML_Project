import math

def getData(filenames):
    data= []
    return_dataset= []
    for filename in filenames:
        with open(filename) as train_file:
            for line in train_file:
                data.append(line)
    
            for ele in data:
                return_dataset.append({"name":ele[2:-1], "result":ele[0:1]})
    
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