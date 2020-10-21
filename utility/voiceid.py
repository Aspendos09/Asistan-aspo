#pyttsx3 sistemdeki sesleri tespit etme kodu
#daha detaylı bilgi https://www.devdungeon.com/content/text-speech-python-pyttsx3
#pyttsx3 sistemde yüklü olan dilleri göstermiyor ise https://stackoverflow.com/questions/56730889/pyttsx-isn-t-showing-installed-languages-on-windows-10
# Print all available voices
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

