"""
Author: VideoUpute
URL:    https://www.youtube.com/channel/UC_0_Jm2Bn-0-ULn_By_1Odw
Video:
"""

# cifre brojcanog sistema
DIGITS = "01"

def getNumber(num):
    global DIGITS
    word = ""
    code = []

    while True:
        temp = (num % len(DIGITS))
        num = int(num/len(DIGITS))
        code.append(temp)
        if num == 0:
            break

    for k in code[::-1]:
        word += DIGITS[k]
    return word

print("Brojevi binarnog brojcanog sistema od 0 do 20: ")
for i in range(20):
    print (getNumber(i))

print ("Broj 85 decimalno je",getNumber(85), "binarno!")
