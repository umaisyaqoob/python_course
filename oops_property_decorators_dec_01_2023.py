class CollageInfo:
    def __init__(self, collage_name, address):
        self.collage_name = collage_name
        self.address  = address

    # Getter Method
    @property
    def collage_detail(self):
        return f"{self.collage_name} is on {self.address}"
    
    # def test():
    #     return f"Umais"
    
    @collage_detail.setter
    def collage_detail(self, data):
        self.collage_name, self.address = data

    @collage_detail.deleter
    def collage_detail(self):
        del self.collage_name 
        del self.address 
    

collage_info = CollageInfo("Post Graduate Collage of Science", "Collage Road Samnabad Faisalabad (38000) Punjab Pakistan")

print(collage_info.collage_detail)

collage_info.collage_detail = ("Postgraduate Collage of Faisalabad" , "Pakistan")

print(collage_info.collage_detail)

del collage_info.collage_detail

# print(collage_info.test())


