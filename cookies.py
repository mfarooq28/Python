# Eating all the cookies
response = float(input("Enter a number : "))
guess = response/2
accuracy = 0.01
iterations = 0 
while abs(response-(guess**2)) > accuracy :
    print ("No of Iterations ", iterations, "Guessed the square root is : ", guess)
    guess = (guess + (response/guess))/2
    iterations = iterations + 1
print ("The original number is :", response)
print ("The square root of the number is :", guess)
