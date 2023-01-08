import mysql.connector

class DepartmentRepository : 
    def __init__(self) :
        pass

    def save_departments(self, departments) :    
        mydb = mysql.connector.connect(
            host="localhost",
            user="ElectionsCongressmans",
            password="ASimpleP@ssW0rd"
        )
        
        mycursor = mydb.cursor()
        for department in departments : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.DEPARTMENT(DepartmentName, DepartmentNumber) VALUES (%s, %s)"
            val = (department.name, department.number)
            mycursor.execute(sql, val)
            department.id = mycursor.lastrowid
            
        mydb.commit()