import dataoperations as data_ops


def getAvgs(data):
    values = {}
    count = {}
    avg = {}
    for item in data:
        for key in item:
            if(key in count):
                count[key] += 1
                values[key].append(item[key])
            else:
                count[key] = 1
                values[key] = [item[key]]
    for key in values:
        avg[key] = sum(values[key])/count[key]
    
    # print "### count ####"
    # print count
    # print "#### values #####"
    # print values

    return avg

def writeTo(outputFile,inputfile,avg):
    with open(inputfile) as input:
        data = input.read().split('\n')
    output = open(outputFile,'w')
    for item in data:
        row = []
        values = item.split()
        
        if len(values) != 0 :
            if values[0] == '1':
                row.append('+')
            else:
                row.append('-')
            for value in values[1:]:
                items = value.split(':')
                
                avg_value = avg[items[0]]
                
                if(float(items[1])>avg_value):
                    sym = "+"
                else:
                    sym = "-"
                this_value = "".join([str(items[0]),":",sym])
                row.append(this_value)
        row.sort()
        print >>output," ".join(row)
        



def convertFile(filename):
    filenames = [filename]
    data = data_ops.getData(filenames)
    avg = getAvgs(data)
    outputFile = "output.test"

    writeTo(outputFile,filename,avg)
    
    









    