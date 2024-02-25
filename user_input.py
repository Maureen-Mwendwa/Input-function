#Input()function used to take the input from the user.
name = input('What is your name?') #Prompting the user to input their name
age = int(input('Please enter your age:')) # Prompting the user to input their age.Also, Convert age to an integer for comparison
location = input('Please enter your current area of residence:') # Prompting the user to input their current area of residence
# Check if the age is within the accepted range (18-24)
if age >= 18 and age <= 24:
    print('Hello and Welcome to L&L limited. We are glad to have you', name,'. Currently, we are receiving applications from youths aged 18-24. I am glad you are aged', age,'which is within our accepted age bracket. Since you are in', location,', we would like to hear more about your farming practices in the area. Feel free to reach us via our email at L&Llimited.co.ke')
else:
    print("We're sorry, but you are not eligible to apply at this time as our applications are currently only open to individuals aged 18-24.Thank you for your interest in L&L limited. We appreciate your understanding.")