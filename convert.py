import dataoperations as data_ops


def getMax(data):
    values = {}
    count = {}
    max_values = {}
    for item in data:
        for key in item:
            if(key in count):
                count[key] += 1
                values[key].append(item[key])
            else:
                count[key] = 1
                values[key] = [item[key]]
    for key in values:
        max_values[key] = max(values[key])
    
    # print "### count ####"
    # print count
    # print "#### values #####"
    # print values

    return max_values

def writeTo(outputFile,inputfile,max_values):
    with open(inputfile) as input:
        data = input.read().split('\n')
    output = open(outputFile,'w')
    for item in data:
        row = []
        values = item.split()
        
        if len(values) != 0 :
            if values[0] == '1':
                row.append('1')
            else:
                row.append('0')
            for value in values[1:]:
                items = value.split(':')
                
                max_value = max_values[items[0]]
                
                sym = str(float(items[1])/max_value)
                this_value = "".join([str(items[0]),":",sym])
                row.append(this_value)
        row.sort()
        print >>output," ".join(row)
        



def convertFile(filename,output):
    filenames = [filename]
    data = data_ops.getData(filenames)
    maxi = getMax(data)
    outputFile = output

    writeTo(outputFile,filename,maxi)
    
    









    