class Resource:
    def __init__(self, name, credits) -> None:
        self.name = name
        self.credits = credits
        
    def get_name(self):
        return self.name
    
    def get_credits(self):
        return self.credits
    
    def set_credits(self, credits):
        self.credits = credits
        
    def __str__(self):
        return self.name + " " + str(self.credits)
        
class Resource_List:
    def __init__(self) -> None:
        self.resource_list = []
        
    def get_credits(self, resource):
        for res in self.resource_list:
            if res.get_name() == resource:
                return res.get_credits()
            
    def add_resource(self, resource, credits):
        for res in self.resource_list:
            if res.get_name() == resource:
                res.set_credits(credits)
                return 
        self.resource_list.append(Resource(resource, credits))
        
    def resource_in_list(self, resource):
        for res in self.resource_list:
            if res.get_name() == resource:
                return True
        return False