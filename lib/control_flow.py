#!/usr/bin/env python3

def admin_login(username, password):
   if username.lower() == "admin" and password == "12345":
       return "Access granted"
   else:
         return "Access denied"
   
admin_login("admin", "12345")

    # your code here
    

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 60:
        return "It's a little chilly out there!"
    elif  temperature >85:
    # your code here
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
hows_the_weather(50)

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    # your code heref 
fizzbuzz(15)

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed"
    else:
        print ("Invalid operation!")
        return None
    # your code here
calculator("+", 5, 3)
