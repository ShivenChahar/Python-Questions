class Solution:
    
    def calculate_bill(self, units):
        total = 0
        if units <= 5000 : 
            if units <= 100 :
                total = 5*units
            elif units > 100 and units <= 300 :
                total = (100*5) + ((units-100)*7)
            elif units > 300 :
                total = (5*100)+(7*200)+((units-300)*10)
            return total