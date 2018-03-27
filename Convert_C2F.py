# This program will convert the Celsius Temprature into Farenheit
user_response = input (" Please Enter the Celsius Temprature :")
celsius = float (user_response)
farenheit = ((celsius*9)/5)+32
print ("The Equivalent Farenheit Temprature is :", farenheit , "degrees farenheit. ")

if farenheit < 32 :
    print ("It is freezing")
elif farenheit < 50:
    print("It is chilly")
elif farenheit < 90 :
    print("It is OK")
else :
    print("It is hot")

