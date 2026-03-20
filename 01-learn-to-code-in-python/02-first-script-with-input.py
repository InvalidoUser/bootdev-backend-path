print("Hello! What is your name?")
name = "Tom"
print(f"Nice to meet you, {name}!")
print("How old are you?")
age = 20
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
print("What's your favorite color?")
color = "green"
print(f"Oh, {color} is a beautiful color!")
# Initially, I wrote this; thanks to some extra practice on the Mimo app.
# Then I transformed it into its second iteration involving input. This is a great milestone for me, finally having an interactive program/script.
name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}!")
age_input = input("How old are you? ")
age = int(age_input)
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!")
