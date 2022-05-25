from gtts import gTTS
import os
fh = open("test_.txt", "r")
myText = fh.read().replace("\n", " ")
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("test_.mp3")
fh.close()
