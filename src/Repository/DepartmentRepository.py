class DepartmentRepository : 
    def __init__(self, mydb) :
        self.mydb = mydb

    def save_departments(self, departments) :    
        mydb = self.mydb.get_my_db()
        
        mycursor = mydb.cursor()
        for department_number in departments : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.DEPARTMENT(DepartmentName, DepartmentNumber) VALUES (%s, %s)"
            val = (departments[department_number].name, department_number)
            mycursor.execute(sql, val)
            departments[department_number].id = mycursor.lastrowid
            
        mydb.commit()