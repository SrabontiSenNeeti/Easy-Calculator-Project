#***************Easy Calculator Project 1************
#Add
#Substract
#Multiply
#Divide


print("Select an operation to perform: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


num = input("Select number 1 to 4: ")
if num == "1":
    #Code for add
    num1 =input("Enter first number: ") 
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2))) 
elif num == "2":
    #code for subtract
     num1 =input("Enter first number: ") 
     num2 = input("Enter second number: ")
     print("The Result is " + str(int(num1) - int(num2))) 
elif num == "3":
    #code for Multiply
     num1 =input("Enter first number: ") 
     num2 = input("Enter second number: ")
     print("The Result is " + str(int(num1) * int(num2)))   
elif num == "4":
    #code for Divide
     num1 =input("Enter first number: ") 
     num2 = input("Enter second number: ")
     print("The Result is " + str(int(num1) / int(num2)))          
else:
    print("Invalid Entry")                
