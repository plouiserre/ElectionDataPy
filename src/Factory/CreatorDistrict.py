from src.Models.DistrictModel import DistrictModel

class CreatorDistrict() : 
    def factory_method(self, election_data):
        district = DistrictModel()
        district_number = election_data[2]
        district.number = int(district_number)
        district.name = election_data[3]
        return district