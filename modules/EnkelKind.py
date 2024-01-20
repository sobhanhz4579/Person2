from Kind import Kind


class EnkelKind(Kind):
    def __init__(self):
        super().__init__()
    
    def information(self):
        str1=self.Name
        str2=self.FamilienName
        result=str1+str2
        return result.upper()

