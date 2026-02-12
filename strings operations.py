name = input("Enter your name: ")
course = input("Enter your course: ")

message = "Hello " + name + ", welcome to " + course
print(message)

print("Length of message:", len(message))
print("Uppercase:", message.upper())
print("Does message contain 'welcome'?", "welcome" in message)

#OUTPUT
Enter your name: charan
Enter your course: MECHRAI
Hello charan, welcome to MECHRAI
Length of message: 32
Uppercase: HELLO CHARAN, WELCOME TO MECHRAI
Does message contain 'welcome'? True
