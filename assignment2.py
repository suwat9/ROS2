class Token:
    def __init__(self):
        self.name = "BTC"
        self.price = 1300000
        self.network = "Bitcoin"
        self.amount = 100
    def show(self):
        print("Token : ",self.name," Price : ",self.price," Network :",self.network," Amount : ",self.amount)

class Address:
    def __init__(self):
        self.home_no = "111"
        self.road = "hadchaosamran"
        self.district = "nawung"
        self.province = "Phetchaburi"
        self.postcode = "76000"
    def show(self):
        print("Address : ",self.home_no," ", self.road, " ", self.district, " ",self.province,' ',self.postcode)
class Account:
    def __init__(self):
        self.id = "001"
        self.name = "Suwat"
        self.token = Token()
        self.address = Address()
    def show(self):
        print("Account : ",self.id, self.name)
        self.token.show()
        self.address.show()

acc = Account()
acc.show()
