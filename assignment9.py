# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< CALCULATE AREA   >>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        AREA=3.14*self.radius**2
        print(f"Radius of the circle is {AREA}")
    
rad=int(input("Enter the radius of the circle: "))
circle_area=Circle(rad)
circle_area.calculate_area()



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<   CALCULATE DISCOUNT       >>>>>>>>>>>>>>>>>>>>>>>>>>

class discount_calculator:
    def __init__(self,price,discount):
        self.price=price
        self.discount=discount
    def calculate_discount(self):
        final_price=self.price-(self.discount/100)*self.price 
        print(f"Price after discount is {final_price}")

PRICE=int(input("Enter the price: "))
DISCOUNT=int(input("Enter the discount: "))
DIS=discount_calculator(PRICE,DISCOUNT)
DIS.calculate_discount()


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<        VOWEL COUNTER      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class COUNTER:
    def __init__(self,vowel):
        self.vowel=vowel
    def vowel_counter(self):
        count=0
        for i in self.vowel:
            if i=="a"or i=="e" or i=="i"or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" :
                count+=1
        print(f"Toatl no of vowels in {self.vowel} is {count}")

vowel=input("Enter the word: ")
word=COUNTER(vowel)
word.vowel_counter()
          