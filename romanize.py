import tltk

while(True):
    print("Enter Thai text to romanize: ", end="")
    text = input()
    print(tltk.nlp.th2roman(text))