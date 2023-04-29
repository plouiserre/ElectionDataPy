from Models.DepartmentModel import DepartmentModel
from Models.DistrictModel import DistrictModel
from Models.ElectionModel import ElectionModel

class FirstRoundDataModel : 
    def __init__(self) :
        self.district = DistrictModel()
        self.department = DepartmentModel()
        self.department = DepartmentModel()
        self.election = ElectionModel()