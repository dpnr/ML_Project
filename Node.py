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
        
        
        if(  node.value in ['complete','alphabet','first_same'] and len(node.getChildren())==0 ) :
            print("\n\n#####")
            print("//len(node.dataset)")
            print(node.value)
            print(len(node.dataset))
            print(len(node.getChildren()))
            print(node.dataset)
            print(node.label)
            print("#####\n\n")
        # if(node.value == 'middle_name' and len(node.dataset)==126):
        #     print('\n\n\n\ndataset\n\n\n')
        #     print(len(node.dataset))
        #     print(node.dataset)

        
        
        # for child in self.getChildren():
        #     print("//len(child.dataset)")
        #     print(len(child.dataset))
        #     print(len(child.getChildren()))
                 
        if(len(node.getChildren())!=0):
            for child in node.getChildren():
                child.displayNode(child)      
        else:
            pass
            
            

            
