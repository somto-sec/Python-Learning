message = "Hello World"
#message is a variable for hello world
print(message)
print(len(message))
#to print the length of the content in the message (string)
print(message[0])
#for printing out a character in the string, works from 0 i.e 0=N in this case
print(message[0:5])
#for printing from a particular character to another, character before the semi colon is inclusive and character after is not inclusive
print(message.lower())
#printing message in lowercase, upper prints it in uppercase
print(message.count("l"))
#counts amount of times that pops up in the string message
greeting = "Hello"
name = "Micheal"
message = f'{greeting}, {name}. Welcome'
print(message)
#String formatting
