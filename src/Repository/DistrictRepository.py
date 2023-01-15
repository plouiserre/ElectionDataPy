import mysql.connector

#TODO externalise mydb code in a centrale class
class DistrictRepository : 
    def __init__(self):
        pass
    
    def save_districts(self, districts) : 
        mydb = mysql.connector.connect(
            host="localhost",
            user="ElectionsCongressmans",
            password="ASimpleP@ssW0rd"
        )
        mycursor = mydb.cursor()
        for district in districts : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.DISTRICT(DistrictName, Position, DepartmentId) VALUES (%s, %s, %s)"
            val = (district.name, district.number, district.department_id)
            mycursor.execute(sql, val)
            district.id = mycursor.lastrowid
        
        mydb.commit()