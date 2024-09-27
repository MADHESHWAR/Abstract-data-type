class Adtlist:
    def __init__(self):
        self.li=[]
    def Append(self,value):
        self.li.append(value)
    def Insert(self,index,value):
        self.li.insert(index,value)
    def Pop(self,index=-1):
        self.li.pop(index)
    def Remove(self,value):
        self.li.remove(value)
    def Length(self):
        print( len(self.li))
    def Display(self):
        print(self.li)
    
obj=Adtlist()
obj.Append("16")
obj.Insert(0,"17")
obj.Display()
obj.Length()
