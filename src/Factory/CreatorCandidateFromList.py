from src.Factory.CreatorCandidate import CreatorCandidate

class CreatorCandidateFromList(CreatorCandidate) : 
    def __init__(self, parties) :
        super().__init__(parties)
        
        
    def factory_method(self, election_data):
        self.datas = election_data
        self.can.last_name = self.datas[6]
        self.can.sexe =  self.datas[5]
        self.__set_candidate_first_name()
        self.__set_candidate_birthdate()
        self.__set_candidate_party()
        self.__set_candidate_jobs()
        if self.datas[11] == 'Oui' :
           self.can.is_sorting = True
        
        return self.can
    
    
    def __set_candidate_birthdate(self) : 
        birthdate = ''
        if  self.is_candidate_first_name_simple == False :
            birthdate = self.datas[9]
        else : 
            birthdate = self.datas[8]
        self.can.birthdate = self.determined_birthdate(birthdate) 
        
        
    def __set_candidate_first_name(self) :  
        if str.isalpha(self.datas[8]) : 
            self.is_candidate_first_name_simple = False
            self.can.first_name = self.datas[7]+" "+self.datas[8]
        else :
            self.can.first_name = self.datas[7]
            
            
    def __set_candidate_party(self) : 
        party_shortname = ''
        if  self.is_candidate_first_name_simple :
           party_shortname = self.datas[9]
        else :
           party_shortname = self.datas[10]
        for party in self.parties : 
            if party.short_name == party_shortname : 
                self.can.party_id = party.id
                break
            
            
    def __set_candidate_jobs(self) : 
         if  self.is_candidate_first_name_simple :
            self.can.job = self.datas[10]
         else :
            self.can.job = self.datas[11]