#class Dairy()
#inheritance constructor library managemet polymorphism 
# # class A:
#    
#   pass

#  class B(A):   # B is child class 
#   pass

# class A:  # Parent Class /Base Class /Super Class/ Generalized
    
#     def show1(self):
#         print("show 1 of  base class ")
# class B(A): # Child Class /Derived Class /Sub Class/ Specialized
#     def show2(self):
#         print(" show 2 of child class ")

# obj=B()   # created a child class object 
# obj.show1()  # invoke a base class Function using the object of child class 
# obj.show2()


# class Person:
#     pass

# class Empl (Person):
#     pass  simar : Airline reservation 
# Amandeep mam : Grocery shop  / Inventory system / stock managemnet system 
# Aminder singh : Library manangemnet system 
# aman : Emply Maintnece sheet /

# class Studnet(Person):
#     pass


groc={
    
     'g01': 'rice',
    'g02': 'sugar',
    'g03': 'tea',
    'g04': 'Flour',
    'g05': 'salt'
}

groc_quantity={'g01': 30,
                 'g02':90,
                 'g03':70,
                 'g04':30,
                 'g05':50,
                 }

Item = input("please enter the item :")
if Item in groc and groc_quantity:
    print("Item in stock")
    print(groc)
else:
    print("Stock unavailable")
    
   





















