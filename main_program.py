# main_program.py

# Approach 1: import module_name
import car_functions
car1 = car_functions.make_car('subaru', 'outback', color='blue', tow_package=True)
print("Approach 1:", car1)

# Approach 2: from module_name import function_name
from car_functions import make_car
car2 = make_car('honda', 'civic', color='red', sunroof=False)
print("Approach 2:", car2)

# Approach 3: from module_name import function_name as fn
from car_functions import make_car as mc
car3 = mc('toyota', 'camry', color='white', hybrid=True)
print("Approach 3:", car3)

# Approach 4: import module_name as mn
import car_functions as cf
car4 = cf.make_car('ford', 'mustang', color='black', convertible=True)
print("Approach 4:", car4)

# Approach 5: from module_name import *
from car_functions import *
car5 = make_car('chevrolet', 'impala', color='silver', classic=True)
print("Approach 5:", car5)
