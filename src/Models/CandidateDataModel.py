from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.CandidateModel import CandidateModel

class CandidateDataModel : 
    def __init__(self) : 
        self.district_number = 0
        self.district_name = ''
        self.candidate_last_name = ''
        self.candidate_first_name = ''
        self.candidate_sexe = ''
        self.candidate_birth_date = ''
        self.candidate_party = ''
        self.candidate_job = ''
        #TODO check the name of this variable
        self.candidate_is_sorting = False
        self.department = DepartmentModel()
        #self.district = DistrictModel()
        #self.candidate = CandidateModel()