""" 
This program simulates a conversation between the user 
and the program. It is meant to be as close to a human 
interaction as possible.

Note: Time seems to return the incorrect value. Time related responses may be incorrect.
"""
from datetime import date
import datetime
import os
import random

# Variables
potential_input = ["hello", "hi", "meet", "weather", "day", "date", "time", "how"]
potential_hellos = ["hola"]
potential_greeting = ["Hello there", "Hi", "Greetings", "Pleasure to meet you"]
time_greetings = ["Good morning!", "Good afternoon!", "Good evening!"]
potential_mood = ["I'm well. How about you?", "I'm good! Thanks for asking. And you?", "I am doing just fine. How about yourself?"]
winter_months = ["December", "January", "February"]
spring_months = ["March", "April", "May"]
summer_months = ["June", "July", "August"]
fall_months = ["September", "October", "November"]
count = 0


# Functions
# Console Clear code forked from https://www.delftstack.com/howto/python/python-clear-console/
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Date and time code forked from https://www.programiz.com/python-programming/datetime
# Returns the date
def get_date():
  return date.today().strftime("%B %d, %Y")

# Returns the current time down to minutes
def get_time():
  hours = datetime.datetime.now().hour
  if hours > 12:
    hours = hours - 12
  if datetime.datetime.now().minute == 0:
    return hours + " o'clock"
  else:
    return str(hours) + ":" + str(datetime.datetime.now().minute)


# Returns a statement for the weather depending on the month.
def get_weather():
  if get_date().split()[0] in winter_months:
    return("The weather is typically cold during Winter. But I could be wrong!")
  elif get_date().split()[0] in spring_months:
    return("The weather is usually warm or rainy in Spring. It really depends on the place.")
  elif get_date().split()[0] in summer_months:
    return("It's generally pretty hot in summer. Did you know it gets up to 117 degrees Fahrenheit in the Sahara Desert during the summer months? Crazy!")
  elif get_date().split()[0] in fall_months:
    return("In fall, it usually starts to get colder. You may want to carry a jacket around.")

# Returns a time-based greeting
# Time value returns forked from https://stackoverflow.com/questions/30071886/how-to-get-current-time-in-python-and-break-up-into-year-month-day-hour-minu
def get_time_greeting():
  now = datetime.datetime.now()
  if now.hour > 12 and now.hour < 18:
    return(time_greetings[1])
  if now.hour < 12:
    return(time_greetings[0])
  else:
    return(time_greetings[-1])

# Checks if the user had a valid input and then responds back. If the input is invalid, it prints a confused message.
def respond(user_input, response_count):
  user_input = user_input.lower()
  for i in range(len(potential_input)):
    if potential_input[i] in user_input:
      valid_response = True
      break
    else:
      valid_response = False
  if valid_response:
    if i <= 1 or user_input.lower() in potential_hellos:
      print(random.choice(potential_greeting) + "! ")
      if response_count < 1:
        print(get_time_greeting())
    elif i == 2:
      print(potential_greeting[-1] + "! ")
    if "how" in user_input and "weather" not in user_input:
      print(random.choice(potential_mood))
      str(input(""))
    if i == 3 or "weather" in user_input:
      print(get_weather())
    if i == 4 or i == 5:
      print("Today's date is " + get_date() + ".")
    if i == 6:
      print("The time is " + get_time() + ".")
  else:
    if "?" in user_input:
      print("Sorry, I'm not sure I understand the question. Try asking me the time!")
    else:
      print("Sorry, I'm not sure I understand.")

# Main Loop
print("The following interaction is a simple chatbot who is only able to respond to questions about the date, time, and weather. You may stop talking at any time but inputting a blank response. Get started by saying hello: ")
while True:
  user_input = str(input(""))
  clear()
  if user_input == "":
    break
  respond(user_input, count)
  count += 1
  
print("Thank you for using the bot!")