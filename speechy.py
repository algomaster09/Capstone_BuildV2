import pyttsx3
f1= open("WordsText.txt","r+");
contents=f1.read()
f2= open("dis.txt","r+");
content=f2.read()
engine= pyttsx3.init()
engine.setProperty('rate',140)
engine.setProperty('volume',1)
engine.say("Hello User.. As per calculations")
engine.say("I think there are many")
engine.say("different Objects in front of you like")
engine.say(contents)
engine.say("and many other objects too ")
engine.say(" and the nearest distance")
engine.say(" calculated is")
engine.say(content)
engine.say("centimetre")
engine.say(" and So Please")
engine.say(" be careful and ")
engine.say(" now press the button ")
engine.say("again..")



engine.runAndWait()
