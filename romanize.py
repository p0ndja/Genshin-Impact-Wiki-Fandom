import tltk

while(True):
    try:
        print("Enter Thai text to romanize: ", end="")
        text = input()
        print(tltk.nlp.th2roman(text))
    except:
        print("Bye Bye")
        break