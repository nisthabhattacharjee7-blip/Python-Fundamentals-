# 1 degree C = 33.6 degree F
temp = float(input("Enter the temp in degree C :"))
unit = input ("Enter the unit (C for celcius , F for ferenheit ): ")

if unit == "C" or unit =='c':
    ferenheit = (temp *9/5)+32
    print(f"{temp} degree C is equal to {ferenheit}degree F ")

elif unit =="F" or unit == "f":
    celcius = (temp-32)* 5/9
    print(f"{temp}degree F is equal to {celcius} degree C ")
else :
    print("Invalid unit !")    
