class ResultServices :
    
    def __init__(self) :
        pass
    
    def store_results(self, election_datas_model, districts, dependency) : 
        result_repository = dependency.get_dependency("resultrepository")
        results=[]
        for election_data_model in election_datas_model :
            for district in districts : 
                if district.name == election_data_model.district.name and district.number == election_data_model.district.number and district.department.name == election_data_model.department.name and district.department.number == election_data_model.department.number:
                    election_data_model.result.district_id = district.id 
            results.append(election_data_model.result)
        result_repository.save_results(results)
        