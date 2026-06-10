# Python Temperature Converter
units=input("Is the Temperature is in Celsius or Fahrenheit: ")
temp=float(input("Enter the Temperature: "))
if units == "C":
    temp=round(9*temp/5+32, 1)
    print(f"The Temperature in Fahrenheit is:{temp} ")
elif units == "F":
    temp=round((temp-32)*5/9, 1)
    print(f"The Temperature in Celsius is:{temp} ")
else:
    print("Invalid Input")