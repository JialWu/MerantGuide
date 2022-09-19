class Resource:
    def __init__(self, name, credits) -> None:
        self.name = name
        self.credits = credits
    def get_name(self):
        return self.name + " " + str(self.credits)
    def __str__(self):
        return self.get_name()
        
class Resource_List:
    def __init__(self) -> None:
        self.resource_list = []
    def add_resource(self, resource):
        self.resource_list.append(resource)
    def get_resource(self):
        return self.resource_list