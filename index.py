# question1: Arithmetic Operators


x = 3

x = x + 3

print(x)


y = 2

y = y * 2

print(y)


result = x / y
print(result)


# question2: Comparison and Logical Operators


a = int(input("Enter a value for a: "))

b = int(input("Enter a value for b: ")) 

if a > b:

    print("a is greater than b")


b = int(input("Enter a value for b: "))

if b % 2 == 0:

    print("b is even")


    a = int(input("Enter a value for a: "))

    c = int(input("Enter a value for c: ")) 

    if c<= a:

        print("c is less than or equal to a")


        a = int(input("Enter a value for a: "))

        b = int(input("Enter a value for b: "))

        c = int(input("Enter a value for c: "))

        if a > b or (b % 2 == 0 and c <= a):

            print("final_condition is True")
        else:

            print("final_condition is False")


# question3: Conditional Statements

score = int(input("Enter your test score (0-100): "))

if score >= 90:

    print("Grade: A") 

elif score >= 80:

    print("Grade: B")

elif score >= 70:

    print("Grade: C")

elif score >= 60:

    print("Grade: D")

else:

    print("Grade: F")

print("Your grade is:", grade)

# question4: Combining Operators and Conditionals

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")
