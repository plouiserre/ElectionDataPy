class DepartmentModel : 
    def __init__(self) : 
        self.number = 0
        self.name = ''
        self.id = 0
        
#TODO correct bug for  departments : 94 "Val d'Oise" and 20 "Côte-dOr" and 21 "Côtes-dArmor"
#TODO create a clean method to put all replace code
    def to_department_model(self, data):
        data = data.replace('[','')
        data = data.replace(']','')         
        data = data.replace("\"","'")
        data = data.replace('\' \'','_')        
        data = data.replace('\' ','_')        
        data = data.replace(' \'','_')
        #data = data.replace('\'','')
        datas = data.split('_')
        
        id = datas[0].replace('\'','')
      
        if id == '2A' or id == '2B' : 
            self.number = 20
            self.name = "Corse"
        elif id == "ZA" :
            self.number = 971
            self.name = "Guadeloupe"
        elif id == "ZB": 
            self.name = "Martinique"
            self.number = 972
        elif id == "ZC": 
            self.name = "Guyane"
            self.number = 973
        elif id == "ZD": 
            self.name = "La Réunion"
            self.number = 974
        elif id =="ZM":
            self.name = "Mayotte"
            self.number = 976
        elif id == "ZN":
            self.name = "Nouvelle-Calédonie"
            self.number = 988
        elif id == "ZP":
            self.name = "Polynésie française"
            self.number = 987
        elif id == "ZS" : 
            self.name = "Saint-Pierre-et-Miquelon"
            self.number = 975
        elif id == "ZW" : 
            self.name = "Wallis et Futuna"
            self.number = 986
        elif id == "ZX" : 
            self.name = "Saint-Martin/Saint-Barthélemy"
            self.number = 978
        elif id == "ZZ" : 
            self.name = "Français établis hors de France"
            self.number = 99
        else :
            id_clean = datas[0].replace('\'','')            
            self.number = int(id_clean)
            #self.name  = datas[1].replace('\'','')
            self.name = datas[1]
            