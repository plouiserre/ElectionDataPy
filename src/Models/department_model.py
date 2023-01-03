class DepartmentModel : 
    def __init__(self) : 
        self.id = 0
        self.name = ''
        
    def to_department_model(self, data):
        data = data.replace('[','')
        data = data.replace(']','')
        datas = data.split(' ')
        id_clean = datas[0].replace('\'','')
        self.id = int(id_clean)
        self.name  = datas[1].replace('\'','')