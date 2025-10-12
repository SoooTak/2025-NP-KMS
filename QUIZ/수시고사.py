class coupon:
    def __init__(self, _name, _coupons=0):
        self.name = _name
        self.coupons = _coupons

    def add_coupon(self):
        self.coupons += 1

    def check(self):
        return self.coupons >= 5

    def redeem(self):
        if self.check():
            self.coupons -= 5
            return "교환 가능합니다"
        return "교환 불가합니다"

card = coupon("김민상")
print(card.name, card.coupons)  
card.add_coupon()                   
card.add_coupon()                   
print(card.check())        
for i in range(3):             
    card.add_coupon()
print(card.check())       
print(card.redeem())   
print(card.coupons)
print(card.redeem()) 