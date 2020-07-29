
amount= int(input("Enter amont : "))
rate = float(input("Enter rate :"))
rate1 = rate/100
year = int(input("Enter year :"))
value = amount*(1+rate1)**year

print("Future value :",round(value,2))
