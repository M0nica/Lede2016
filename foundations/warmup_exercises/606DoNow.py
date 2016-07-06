name = "Tara"
print("hello", "name")

print("hello", name)

#SyntaxError: Missing parentheses in call to 'print'

borough_name = 'Manhattan'
z = [ 'Manhattan', 'Queens']
x = {'borough_name': 'Manhattan', 'population':500, 'Queens': 200
}

y = {
'Manhattan': 500,
'Queens' : 200
}

# uses key
print(x['borough_name'])

# KeyError: 'Manhattan' , x does not have a key manhattan
# print(x[borough_name])

# dictionary  - no indices
# key error 0
# print(x[0])
# KeyError: 'borough_name'
# print(y['borough_name'])
print(y[borough_name])
# KeyError: 0
# print(y[0])
# print(z['borough_name'])
# list indices must be integers or slices, not str
# print(z[borough_name])
print(z[0])

integers = [1,2,3,4]

for integer in integers:
    print(integer * 100)


murders = {'Albany': 23, 'Kings County':10, 'Rochester': 7, 'Yonkers': 9}

total_murders  = murders['Albany'] + murders['Kings County'] + murders['Rochester'] + murders['Yonkers']

print("there are", sum(murders.values()),"murders")

kingsM = 100 * murders['Kings County']/total_murders

print(kingsM, "of murders happen in Kings County")
