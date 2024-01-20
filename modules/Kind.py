from Person import Person

class Kind(Person):
    def __init__(self):
        super().__init__()
    

    def crand(self):
        l2=[]
        for j in range(1,11):
            nummer2=random.random()
            l2.append(nummer2)
        return l2

