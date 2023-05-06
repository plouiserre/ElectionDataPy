from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ElectionModel import ElectionModel

class ElectionDistrictFirstRoundModel : 
    def __init__(self) :
        self.district = DistrictModel()
        self.department = DepartmentModel()
        self.department = DepartmentModel()
        self.election = ElectionModel()
        self.candidates = []