from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.CandidateModel import CandidateModel
from src.Models.DeputyModel import DeputyModel

class CandidateDataModel : 
    def __init__(self) : 
        self.candidate_is_sorting = False
        self.department = DepartmentModel()
        self.district = DistrictModel()
        self.candidate = CandidateModel()
        self.deputy = DeputyModel()