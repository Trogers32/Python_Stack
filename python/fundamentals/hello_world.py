#arr[0], arr[1] = arr[1], arr[0] #python's easy swap


# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Timothy"
print( "Hello ", name ) # with a comma
print( "Hello " + name ) # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello ", name ) # with a comma
print( "Hello " + str(name) ) # with a +  -- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}".format(fave_food1, fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}" ) # with an f string


my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz


my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:       # only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

