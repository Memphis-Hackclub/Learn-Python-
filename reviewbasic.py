#review from last week and expansion of topics
name = "Philip" #string varible
years = 8.0833333 #float varible
decades = 1 #integer varible
senSubVerb = "" #empty strings
senPer = "" #empty strings

otherWords = [] #empty list
otherWords = ["is","years", "old"] #setting list equal to more values

def makeSentence(word, name, yearFloat, year, senSubVerb, senPer): #making a function and passing values in
  if word == "is": #using an if statment so if word is equal to 'is' it will do the indented code below
    senSubVerb = ""+name+" is " #modifing a varible 
  if word == "years": #using an if statemnt again but if word is equal to 'years' it will do the indented code below
    senPer = str(year)+""+str(yearFloat)+" years "+str(otherWords[2]) #this is varible modification we making year and yearFloa a string so it can be displayed, then we are adding in the thrid item in the otherWords list as a sting
  sentence = senSubVerb+senPer # the final varible
  return senSubVerb, senPer, sentence  #this returns all the varibles that are important to this function


for i in otherWords:# this for loop loops through every value in the otherWords list and passes it into the function called below.
  sentenceParts = makeSentence(i, name, years, decades, senSubVerb, senPer)#this calls the returned values of the function equal to sentenceParts
  senSubVerb = sentenceParts[0] # this gets the senSubVerb from sentenceParts as it is the first item in the list of returned values. This statemnt is important as it passes it back through the function so we do not lose our varible.
  senPer = sentenceParts[1]# this gets the senPer from sentenceParts as it is the first item in the list of returned values. This statemnt is important as it passes it back through the function so we do not lose our varible.
  sentence = sentenceParts[2] # this gets the sentence varible

print(sentence) #this prints our final sentence varible
