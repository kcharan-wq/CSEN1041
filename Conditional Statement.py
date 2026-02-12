cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
else:
    print("No Profit No Loss")

#OUTPUT
Enter cost price: 25
Enter selling price: 50
Profit

Enter cost price: 100
Enter selling price: 50
Loss
