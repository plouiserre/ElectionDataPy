class PartyModel : 
    def __init__(self, *args) : 
        if len(args) == 0 : 
            self.id = 0
            self.name = ''
            self.short_name = ''        
        else : 
            self.id = args[0] 
            self.name = args[1]
            self.short_name = args[2]