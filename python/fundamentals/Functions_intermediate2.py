
#1 Update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
print(x)
students[0]['last_name'] = "Bryant"
print(students)
sports_directory['soccer'][0] = "Andres"
print(sports_directory)
z[0]['y']=30
print(z)

#2 Iterate Through a List of Dictionaries
def iterateDictionary(someL):
    joiner = ", "
    for i in someL:
        std = ""
        for key in i:
            std += str(key) + " - " + str(i[key]) + "#"
        std = std.split("#")
        std.pop()
        std = joiner.join(std)
        print(std)
        
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)

#3 Get values from a list of dictionaries
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4 Iterate through a dictionary with list values
def printInfo(some_dict):
    for i in some_dict:
        print(str(len(some_dict[i])) + " " + str(i).upper())
        for val in some_dict[i]:
            print(val)
    
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
    
    
    
    
    
    