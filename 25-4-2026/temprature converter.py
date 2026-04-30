# emperature Converter(Celsius<->Fahrenheit)

choice = input("Convert(1)Celsiusto Fahrenheit or(2)Fahrenheit to Celsius?Enter 1 or 2:")

if choice == "1":
    c = float (input("enter temperature in Celsius:"))
    f = (c*9/5)+32
    print("Fahrenheit:",f)

elif choice == "2":
    f = float(input("Enter temprature in Fahrenheit:"))
    c = (f-32)*5/9
    print("Celsius:",c)

else:
    print("Invalid choice!")
