#Assign Variable
message = "Good Morning Brian. Welcome to the Python 3 Crash Course!"
print(f"The message is : {message}")

#Strings
name = "ada lovelace"
#Title
print(name.title())
#Upper
print(name.upper())
#Lower
name = "ADA LOVELACE"
print(name.lower())
#Variables in strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name.title()}!")
#Adding Whitespaces To Strings with Tabs (\t) and Newlines (\n)
print("There is a tab before \tme.")
print("There is a new line before \nme.")
print("I love \n\tPython\n\tJava and \n\tC++")
#Stripping White Spaces {rstip(), lstrip(), strip()}
favourite_language = 'python '
print(favourite_language)
print(favourite_language.rstrip())
favourite_language = favourite_language.rstrip()
print(favourite_language)
#Quotes
message = "One of Python's strengths is its diverse community"
print(message)

#Grouping digits of large numbers with underscores to improve readability
universe_age = 14_000_000_000
speed_of_light = 300_000
planck_constant = 6.626_070_15 * 10**(-34)

nothing_important = universe_age * planck_constant / speed_of_light
print(f"Epic math: {nothing_important}")

#Multiple assignment
x, y, z = 2, 3, 4
result = x**y**z
print(result)

#Constants
MAX_CONNECTIONS = 5000