class computers:
    budget=0
    def __init__(self,name,contact_no,budget):
        self.name=name
        self.contact_no=contact_no
        self.budget=budget
    def get_detailslaptops(self):
        if self.budget>=30000:
            print("we have these laptops a/c to your budget:HP15-BW0XX,HPNotebook14-dq0007ca14,HPStream11Celeron6thGeneration")
        else:
            print("oops sorry! we have no laptops availible according to your budget")
        
        if self.budget>=40000:
            print("we have these laptops for you:Lenovo Miix 320,HP EliteBook Folio 9470M,Dell XPS 13 9300")
        else:
            print("oops we have nothing in your desired range")
                  
    def get_details_PCs(self):
        if self.budget>=40000:
            print("these are some PCs a/c to your desired range: RX 560 4 GB GPU,RX 470 8 GB GPU")
        else:
            print("oops we have nothing in your desired range")
        
        if self.budget>=50000:
            print("these are some PCs in your desired range:HP 290 G4 Ci3,HP 290 G4 Ci5,HP ProDesk 400 G7 MT Ci5 ")
        else:
            print("oops sorry we have nothing in your desired range")      
                  

name=input("enter your name: ")                
contact_no=input("enter your contact_no: ")
budget=eval(input("enter your desired budget "))
customer1=computers(name,contact_no,budget)
customer1.get_detailslaptops()
customer1.get_details_PCs()                  
