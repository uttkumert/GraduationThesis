from gtts import gTTS
import os
fh = open("RAI.txt", "r")
myText = fh.read().replace("\n", " ")
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("RAI.mp3")
fh.close()