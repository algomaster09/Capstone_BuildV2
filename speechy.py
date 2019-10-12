import pyttsx3
f1= open("WordsText.txt","r+");
contents=f1.read()
mytext = "Hello User.... As per hhhhhhlations, I think there are many different Objects in front of you like "+contents+" and many other objects too     so please be careful"
engine= pyttsx3.init()
engine.setProperty('rate',140)
engine.setProperty('volume',1)
engine.say("Hello User.. As per calculations")
engine.say("I think there are many")
engine.say("different Objects in front of you like")
engine.say(contents)
engine.say("and many other objects too ")
engine.say("So Please be careful")

engine.runAndWait()
