from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel

class FirstRoundDataModel : 
    def __init__(self) :
        self.district = DistrictModel()
        self.department = DepartmentModel()