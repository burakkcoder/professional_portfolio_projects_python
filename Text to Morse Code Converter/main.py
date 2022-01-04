import time

print("""
___________              __    ___________         _____                              
\__    ___/___ ___  ____/  |_  \__    ___/___     /     \   ___________  ______ ____  
  |    |_/ __ \\  \/  /\   __\   |    | /  _ \   /  \ /  \ /  _ \_  __ \/  ___// __ \ 
  |    |\  ___/ >    <  |  |     |    |(  <_> ) /    Y    (  <_> )  | \/\___ \\  ___/ 
  |____| \___  >__/\_ \ |__|     |____| \____/  \____|__  /\____/|__|  /____  >\___  >
             \/      \/                                 \/                  \/     \/ 
""")

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

while True:
    new_text = ""
    text = input("Enter the text (Enter 'q' to exit the program) : ").upper()
    if text == "Q":
        print("Program is Ending...")
        time.sleep(2)
        print("Bye!")
        break
    else:
        for x in text:
            if x == " ":
                new_text += "  "
            else:
                new_text += MORSE_CODE_DICT[x] + " "
        print(new_text)