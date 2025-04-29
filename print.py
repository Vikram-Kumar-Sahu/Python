# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
# ''')


# import pyttsx3
# engine=pyttsx3.init()
# engine.say("Durgesh Nai.20 Rs daadi khakhori free")
# engine.runAndWait()

#set 2
#a=int(input("enter a num: "))
#z=int(input("enter a num: "))
#print(f"The sum is: {a + z}")
#print((a+z)/2);
#print(a**2)

#set 3

# name = input("Enter your name: ")
# date = input("Enter the date: ")

# letter = '''Dear <Name>,
# You are selected.
# <Date>'''

# # Replace placeholders
# letter = letter.replace("<Name>", name)
# letter = letter.replace("<Date>", date)

# print(letter)

# numbers = (1, 2, 3, 4, 5)
# print(numbers.count(3))  # This will count how many times '3' appears in the tuple

# n=int(input("enter a number"))
# for i in range(1,11):
#     print(f"{n}x{i}=",n*i)

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
        if(i==0 or i==(n-1) or j==0 or j==(n-1)):
            print("*",end="")
        else:
            # Print space for the inside of the square
            print(" ", end="")
    print()