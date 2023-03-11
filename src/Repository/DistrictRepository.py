class DistrictRepository : 
    def __init__(self, mydb):
        self.mydb = mydb
        
    def save_districts(self, districts) : 
        mydb = self.mydb.get_my_db()
        mycursor = mydb.cursor()
        for district in districts : 
            sql = "INSERT INTO ELECTIONSCONGRESSMANS.DISTRICT(DistrictName, Position, DepartmentId) VALUES (%s, %s, %s)"
            val = (district.name, district.number, district.department.id)
            mycursor.execute(sql, val)
            district.id = mycursor.lastrowid
        
        mydb.commit()