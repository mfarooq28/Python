# This progrma calculates the square root of a number
user_input=float(input("Enter a number :"))
guess = user_input/2
accuracy = 0.05
iterations = 0
while abs (user_input - (guess**2)) > accuracy:
    print("Iterations ", iterations, "Guess square root is :" , guess)
    guess = (guess+(user_input/guess))/2
    print ("Orignal Number is : " , user_input)
print ("Square root of number is ", guess)    
