class RemoteController:

    def __init__(self , brand, model , color):
        self.brand = brand
        self.model = model
        self.color = color

    def showInfo(self):
        print("""
        
        ************************
              INFORMATION
        ************************
        
        Brand = {}
        Model = {}
        Color = {}
        
        """.format(self.brand, self.model, self.color))

    def changeProp(self , marka , model , renk):
        self.brand = marka
        self.model = model
        self.color = renk