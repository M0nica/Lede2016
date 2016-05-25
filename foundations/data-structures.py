name = "Monica"
city = "Manhattan"
hometown = "Bowie"
age = 22

print("Hi, I'm", name, "from", hometown)

friend_name = "Daena"
friend_city = "Far Rockaway, Queens"
friend_age = 21
friend_hometown = "Jamaica, Queens"

print("This is", friend_name, "from", friend_hometown)

other_friend_name = "Larissa"
other_friend_city = "Brooklyn"
other_friend_age = 29
other_friend_hometown = "New Jersey"
print("Here's", other_friend_name, "from", other_friend_hometown)


# DRY - Don't Repeat Yourself - Rule of Programming!!!

# this is called a dictionary - hashmap/hash table
me = {'name': 'Monica', 'city': 'Manhattan', 'age': 22}

print(me['name'])
print(me['city'])

friend = {'name': 'Daena', 'city': 'Queens', 'age': 21}
print(friend['name'])
print(friend['city'])


other = {'name': 'Blake', 'city': 'Brooklyn', 'name': 'Blakie'}

# error will occur if the key value pair does not exist in the dictionary
# name is a key
# city is a key
# keys are the words in the dictionary -
# Blake is a value
# if the same key has different value then only the second value will appear
# therefore keys should only have one value!
print(other['name'])


# Data Structures!
# int = integers  = whole numbers
# str = strings = words/sentences
# dict = dictionaries = keys/values
# list = stores values in a list (called an array in every other language except for Python )

names = ['Blake', 'Blakie', 'Blakester', 'Watch Guy', 'Belake']
