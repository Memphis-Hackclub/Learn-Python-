#data types - ints and floats
age = 15
height = 5.6
add = age+height
print(type(add))
addint = int(add)
print(type(add))

#data types - strings
name = "Blake F"
name2 = "Philip P"
name3 = "Jacob H"

#list - creating a list
memberList = ["Blake F", "Philip P", "Jacob H"]
print(memberList)
memberList.append("Will B")
print(memberList)

#list - find the length of a list
print(len(memberList))
member_number = len(memberList)

#for loops - go through a list
for i in range(member_number):
  print(memberList[i])

#functions - creating a function
def greet(name,afternoon):
  if afternoon == True:
    print("Hello "+name+" good evening!")
  if afternoon == False:
    print("Hello You Nerd Mr"+name+"tis a good mrning we are having today")  
greet("Ethan",False)

#functions - return a value
def EOnumber(number):
  if number % 2 == 0:
    return "even"
  else:
    return "odd"
numberval = EOnumber(14) 
print(numberval)
