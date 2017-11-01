def values(trainclass,filename,average):

    eval_output = open('data.eval.result.id','w')

    with open(filename) as testfile:
        for line in testfile:
            terms =line.split()
            true_label = float(terms[0])
            xvector = {}
            wx = 0.0
            if(average==False):
                weights =trainclass.getWeights()
                weight_indexes = weights.keys()[:]
                bias = trainclass.getbias()
            else:
                weights =trainclass.getAvgWeights()
                weight_indexes = weights.keys()[:]
                bias = trainclass.getavgbias()
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
                    print('seen a new x vector')
                    trainclass.updateWeight(key,getNumber.getRandom())
                    trainclass.updateAvgWeight(key,getNumber.getRandom())
                wx += float(weights[key])*float(xvector[key])

            result = (wx+bias)

            if(result >= 0):
                #change the weight vector to w+yx
                print >>eval_output, 1
            else:
                print >>eval_output, 0
    