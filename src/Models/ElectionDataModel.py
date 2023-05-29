from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ResultModel import ResultModel

class ElectionDataModel : 
    def __init__(self) : 
        self.candidate_is_sorting = False
        self.department = DepartmentModel()
        self.district = DistrictModel()
        self.candidates = []
        self.deputies = []
        self.result = ResultModel()        