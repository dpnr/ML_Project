class Node:
    
    def __init__(self,value,dataset,attributes,target,parentNode,label,entropy):
        self.children = []
        self.value = value
        self.dataset = dataset
        self.attributes = attributes
        self.target =target
        self.parentNode = parentNode
        self.label = label
        self.entropy = entropy
       
    
    def setValue(self,value):
        self.value = value

    def setDataset(self,dataset):
        self.dataset = dataset
    
    def setTarget(self,target):
        self.target = target
    
    def setAttributes(self,attrbutes):
        self.attributes = attrbutes
    
    
    def getAttributes(self):
        return self.attributes

    
    def addChild(self,child):
        self.children.append(child)
    
    def getChildren(self):
        return self.children

    def getTarget(self):
        return self.target

    def getDataset(self):
        return self.dataset
    
    def displayNode(self,node):
    
            print("\n\n#####")
            print("len(node.dataset)")
            print(node.value)
            print(len(node.dataset))
            print(len(node.getChildren()))
            print(node.label)
            print("#####\n\n")
                 
            if(len(node.getChildren())!=0):
                for child in node.getChildren():
                    child.displayNode(child)      
            else:
                pass
            
            

            
