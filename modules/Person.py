import random

class Person:
    __name=""
    __familienName=""
    ucode=[]


    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name=value
    @Name.deleter
    def Name(self):
        del self.__name
    
    @property
    def FamilienName(self):
        return self.__familienName
    @FamilienName.setter
    def FamilienName(self,value):
        self.__familienName=value
    @FamilienName.deleter
    def FamilienName(self):
        del self.__familienName
    



    def crand(self):
        g=[]
        for i in range(1,11):
            nummer2=random.randint(1,1000)
            g.append(nummer2)
        ucode=random.sample(g,1)
        return ucode
 