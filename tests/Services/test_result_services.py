import unittest

from mock import Mock

from src.Models.DepartmentModel import DepartmentModel
from src.Models.DistrictModel import DistrictModel
from src.Models.ElectionDataModel import ElectionDataModel
from src.Models.ResultModel import ResultModel

from src.Services.ResultServices import ResultServices

#TODO factorize
class ResultServicesTest(unittest.TestCase) : 
    def test_results_data_district_id_with_one_elections_data_with_first_result(self) :
        dependency = Mock()
        first_election_data_model = ElectionDataModel()
        first_election_data_model.district = DistrictModel()
        first_election_data_model.district.name = '2ème circonscription'
        first_election_data_model.district.number = 2
        first_election_data_model.first_result = ResultModel()
       
        
        election_datas_model = [first_election_data_model]
        
        
        first_district = DistrictModel()
        first_district.name = '2ème circonscription'
        first_district.number = 2
        first_district.id = 234
        
        districts = [first_district]
        
        result_service = ResultServices()
        result_service.store_results(election_datas_model, districts, dependency)
        
        self.assertEqual(234, election_datas_model[0].first_result.district_id)
        
        
    def test_results_data_district_id_with_two_elections_data_with_first_result(self) :
        dependency = Mock()
        first_election_data_model = ElectionDataModel()
        first_election_data_model.district = DistrictModel()
        first_election_data_model.district.name = '2ème circonscription'
        first_election_data_model.district.number = 2
        first_election_data_model.first_result = ResultModel()
        
        second_election_data_model = ElectionDataModel()
        second_election_data_model.district = DistrictModel()
        second_election_data_model.district.name = '9ème circonscription'
        second_election_data_model.district.number = 9
        second_election_data_model.first_result = ResultModel()
        
        election_datas_model = [first_election_data_model, second_election_data_model]
        
        
        first_district = DistrictModel()
        first_district.name = '2ème circonscription'
        first_district.number = 2
        first_district.id = 234
        
        second_district = DistrictModel()
        second_district.name = '9ème circonscription'
        second_district.number = 9
        second_district.id = 666
        
        districts = [first_district, second_district]
        
        result_service = ResultServices()
        result_service.store_results(election_datas_model, districts, dependency)
        
        self.assertEqual(234, election_datas_model[0].first_result.district_id)
        self.assertEqual(666, election_datas_model[1].first_result.district_id)
        
        
    def test_results_data_district_id_with_two_elections_data_with_first_second_results(self) :
        dependency = Mock()
        first_election_data_model = ElectionDataModel()
        first_election_data_model.district = DistrictModel()
        first_election_data_model.district.name = '2ème circonscription'
        first_election_data_model.district.number = 2
        first_election_data_model.first_result = ResultModel()
        
        second_election_data_model = ElectionDataModel()
        second_election_data_model.district = DistrictModel()
        second_election_data_model.district.name = '5ème circonscription'
        second_election_data_model.district.number = 5
        second_election_data_model.second_result = ResultModel()
        
        third_election_data_model = ElectionDataModel()
        third_election_data_model.district = DistrictModel()
        third_election_data_model.district.name = '9ème circonscription'
        third_election_data_model.district.number = 9
        third_election_data_model.first_result = ResultModel()
        third_election_data_model.second_result = ResultModel()
        
        election_datas_model = [first_election_data_model, second_election_data_model, third_election_data_model]
        
        
        first_district = DistrictModel()
        first_district.name = '2ème circonscription'
        first_district.number = 2
        first_district.id = 234
        
        second_district = DistrictModel()
        second_district.name = '5ème circonscription'
        second_district.number = 5
        second_district.id = 666
        
        third_district = DistrictModel()
        third_district.name = '9ème circonscription'
        third_district.number = 9
        third_district.id = 999
        
        districts = [first_district, second_district,third_district]
        
        result_service = ResultServices()
        result_service.store_results(election_datas_model, districts, dependency)
        
        self.assertEqual(234, election_datas_model[0].first_result.district_id)
        self.assertEqual(666, election_datas_model[1].second_result.district_id)
        self.assertEqual(999, election_datas_model[2].first_result.district_id)
        self.assertEqual(999, election_datas_model[2].second_result.district_id)
        
        
    def test_results_data_district_id_with_same_district_number_differents_departments(self) :
        dependency = Mock()
        first_election_data_model = ElectionDataModel()
        first_election_data_model.district = DistrictModel()
        first_election_data_model.district.name = '2ème circonscription'
        first_election_data_model.district.number = 2
        first_election_data_model.department = DepartmentModel()
        first_election_data_model.department.name = "Gironde"
        first_election_data_model.department.number = 33
        first_election_data_model.first_result = ResultModel()
        
        second_election_data_model = ElectionDataModel()
        second_election_data_model.district = DistrictModel()
        second_election_data_model.district.name = '2ème circonscription'
        second_election_data_model.district.number = 2
        second_election_data_model.department = DepartmentModel()
        second_election_data_model.department.name = "Hauts de Seine"
        second_election_data_model.department.number = 92
        second_election_data_model.first_result = ResultModel()
        
        election_datas_model = [first_election_data_model, second_election_data_model]
        
        
        first_district = DistrictModel()
        first_district.name = '2ème circonscription'
        first_district.number = 2
        first_district.id = 234
        first_district.department = DepartmentModel()
        first_district.department.name = "Gironde"
        first_district.department.number = 33
        
        second_district = DistrictModel()
        second_district.name = '2ème circonscription'
        second_district.number = 2
        second_district.id = 666
        second_district.department = DepartmentModel()
        second_district.department.name = "Hauts de Seine"
        second_district.department.number = 92
        
        districts = [first_district, second_district]
        
        result_service = ResultServices()
        result_service.store_results(election_datas_model, districts, dependency)
        
        self.assertEqual(234, election_datas_model[0].first_result.district_id)
        self.assertEqual(666, election_datas_model[1].first_result.district_id)
        
        
    def test_result_repository_called(self) :
        dependency = Mock()
        
        result_service = ResultServices()
        result_service.store_results([], [], dependency)
        
        self.assertTrue(dependency.get_dependency.called)