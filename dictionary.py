minecraftInfo = {'year':2011, 'publisher':'Mojang Studios', 'type':'sandbox'} # creating a dictionary about the video game Minecraft
print("\n Dictionaries")
print(minecraftInfo)
print(minecraftInfo['year']) # accessing the key year in our dictionary minecraftInfo 

key = input("\n What would you like to know about MineCraft?\n") #getting a key to pull from our minecraftInfo dictionary
print(minecraftInfo[key]) #printing the value for the key

minecraftInfo['version'] = "bedrock" #adding a new key to the dictionary
print("\n adding a key")
print(minecraftInfo)
print(minecraftInfo['version']) # printing a new key
minecraftInfo['version'] = "java" #modifing the key

key = input("\n Would you like to add a new key to the Minecraft Library?") # allowing the user to add a key
value = input("What would like "+key+" to be equal too?") # alowing the user to add a value for that key
minecraftInfo[key] = value #creating the key and value
print(minecraftInfo[key]) #printing the new value

minecraftInfo.pop("year") #removing the year value
print("\n removing a key") 
print(minecraftInfo)

print("\n adding a key and list value")
minecraftInfo['releases'] = [2.7, 2.8, 3]
print(minecraftInfo)
