
import getNumber
import training


class simplePerceptron:

    def __init__(self,trainingdata,dynamic):
        self.weight = {}
        self.trainingdata = trainingdata
        self.bias = getNumber.getRandom() 
        self.dynamic = dynamic
        self.learningRate = self.setlearningRate(0)
        self.avg_weight = {}
        self.avg_bias = getNumber.getRandom()
        self.epoch_history ={}
        self.updates = 0

    def runtraining(self,r):
        for line in self.trainingdata:
            training.getfeedback(line,self,r)
    def runtraining_svm(self,r,c):
        for line in self.trainingdata:
            training.getfeedback(line,self,r,c)

    # def runtraining_margin(self,r,margin):
    #     for line in self.trainingdata:
    #         training.getfeedback_margin(line,self,r,margin)
    
    # def runtraining_average(self,r):
    #     for line in self.trainingdata:
    #         training.getfeedback_average(line,self,r)

    # def runtraining_aggressive(self,r):
    #     for line in self.trainingdata:
    #         training.getfeedback_aggressive(line,self,r)
            
    
    def updateWeight(self,key,value):
        self.weight[key] = value
    
    def updateAvgWeight(self,key,value):
        self.avg_weight[key] = value
    
    def printWeights(self):
        print(self.weight)
    
    def getWeights(self):
        return self.weight

    def getAvgWeights(self):
        return self.avg_weight

    def getbias(self):
        return self.bias
    
    def getavgbias(self):
        return self.avg_bias

    def setlearningRate(self,rate):
        self.learningRate = rate
