from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ElectionModel import ElectionModel

#TODO find better naming for candidatedatamodel because it is confusing with the list of candidates
class CandidateDataModel : 
    def __init__(self) : 
        self.candidate_is_sorting = False
        self.department = DepartmentModel()
        self.district = DistrictModel()
        self.candidates = []
        self.deputies = []
        self.election = ElectionModel()