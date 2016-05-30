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
print(names[3])
print(names[0])
# provides you with the length of names aka the number
# of names in the file
print(len(names))

numbers = [56, 23, 87, 43, 1, 67, 9]
print(numbers)
print("number of numbers", len(numbers))
print("maximum", max(numbers))
print("smallest", min(numbers))

#temporarily sorts
print("the sorted numbers are", sorted(numbers))

print("the original numbers remain unsorted", numbers)

# sorts forever
print(numbers.sort())

#after running the .sort() method the original list becomes sorted
print(numbers)
# len(), max(), min() are methods/functions


# data journalist only need three things when working with numbers:
# the biggest
# the smallest
# average

name = "Monica"
print(name)
print(name.lower())
print(name.upper())

print("Ten Things I Hate About You".swapcase())

word = "Google"
number_of_os = word.count("o")
print(number_of_os)

cats = ["Smushface", "Gallery", "Naples"]

# print("Hello", cats[0]

# print("Hello", cats[1])

# print("Hello", cats[2])

# prints hello for each cat
# flow control
for cat in cats:
    print("Hello", cat)
    if cat == "Smushface":
        print("Here's some food", cat, "!")
    else:
        print("Sorry it looks like we're out of food, I guess?")

# here is a list of different dictionaries :O
# data from places is generally in this format!

cat_info = [
 # cat_info[0]
   { 'name': 'Smushface', 'age': 6 },
 # cat_info[1]
   { 'name': 'Callery', 'age': 2 },
 # cat_info[2]
   { 'name': 'Naples', 'age': 'unknown' }
]

# prints in random order each times
# order does not matter for dictionary entries
print(cat_info[0])

gallery_the_cat=cat_info[1]
print(gallery_the_cat['name'])


for cat in cat_info:
    if cat['age'] == 'unknown'.lower():
        print("NO ONE KNOWS HOW OLD", cat['name'].upper(),"IS")
    else:
        print(cat['name'].upper(), "is", cat["age"], "years old")
#     print(cat['name'])
