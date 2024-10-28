units = int(input("Enter the units you consumed : "))

if units < 50 :
    amount = units * 2.60 + 25 
elif units > 50 and units < 100 :
    amount = units * 3.25 + 35 
elif units > 100 and units < 200 :
    amount = units * 5.26 + 45
elif units > 200 :
    amount = units * 8.45 + 75  
else :
    print("Erorrrr!!!!!")
print("Your electicity bill is",amount)