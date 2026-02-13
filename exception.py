try:
    print("Exception Handling Example")
    
   
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    
    result = num1 / num2
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    
except ValueError:
    print("Error: Please enter valid integer numbers!")
    
else:
  
    print("Result is:", result)
    
finally:

    print("Program finished.")