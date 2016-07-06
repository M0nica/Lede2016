# woohoo my first python script
print("Hello World!")
print('Hello World!')

# integers
print(10)
print(10 + 10)


# strings
# won't automatically put a space unless you give it one ;)
print("Hello" + "world!")

print("Hello" + " " + "world!")


print("Hello" + "10")

print("Hello" + str(10))
# http://stackoverflow.com/questions/11844072/python-typeerror-cannot-concatenate-str-and-int-objects
name = "Monica"
print("Hello, " + name)

# Name = input("What's your name?")
# sprint("Hello, " + Name)


name = input("What's your name?")
print ("Hello," + name)

year_of_birth = input("What year were you born?")
age = 2016 - int(year_of_birth)
# print("You are roughly", str(age), "years old")
# you can use commas instead of + to concat
# commas = it will automatically handle unit conversions for us!
print("You are roughly", age, "years old")

# only the first condition that is met will be executed
# if there are a lot of conitions then may want to consider using
# switch statements instead
# or in python is just the word 'or'!
if age >= 21:
    print("Here's your beer unit.")
elif age < 0:
    print("You are an idiot, or from the future!")
else:
    print("Nope, sorry.")
# intendentation matters in Python!
print("Goodbye")
