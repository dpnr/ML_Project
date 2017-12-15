import dataoperations as data_ops
import math


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
    
    return max_values

def getMin(data):
    values = {}
    count = {}
    min_values = {}
    for item in data:
        for key in item:
            if(key in count):
                count[key] += 1
                values[key].append(item[key])
            else:
                count[key] = 1
                values[key] = [item[key]]
    for key in values:
        min_values[key] = min(values[key])
    
    return min_values
    
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


def writeTo_log(outputFile,inputfile,max_values):
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
                
                
                if(float(items[1]) > 0.0):
                    
                    sym = str(math.log(float(items[1]),2))
                elif(float(items[1]) < 0.0):
                    if(math.log(float(items[1])*-1,2) > 0.0):
                        sym = "".join(["-",str(math.log(float(items[1])*-1,2))])
                    else:
                        sym = str(-1 * math.log(float(items[1])*-1,2))
                else:
                    sym = str(0)
                this_value = "".join([str(items[0]),":",sym])
                row.append(this_value)
        row.sort()
        print >>output," ".join(row)
        
def writeTo_scale(outputFile,inputfile,max_values,min_values):
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
                
                if(max_values[items[0]] - min_values[items[0]] != 0):    
                    sym = str( (float(items[1]) - min_values[items[0]]) / float( max_values[items[0]] - min_values[items[0]] ) )
                

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
    

def convertFile_log(filename,output):
    filenames = [filename]
    data = data_ops.getData(filenames)
    maxi =[]
    outputFile = output

    writeTo_log(outputFile,filename,maxi)


def convertFile_scale(filename,output):
    filenames = [filename]
    data = data_ops.getData(filenames)
    
    maxi = getMax(data)
    print maxi
    mini = getMin(data)
    outputFile = output

    writeTo_scale(outputFile,filename,maxi,mini)








    