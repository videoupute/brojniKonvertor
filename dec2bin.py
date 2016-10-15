"""
Author: VideoUpute
URL:    https://www.youtube.com/channel/UC_0_Jm2Bn-0-ULn_By_1Odw
Video:
"""

# cifre brojcanog sistema
DIGITS = "01"

def getNumber(dec):
    global DIGITS
    bin_ = ""
    rest = []

    while True:
        temp = (dec % len(DIGITS))
        dec = int(dec/len(DIGITS))
        rest.append(temp)
        if dec == 0:
            break

    for k in rest[::-1]:
        bin_ += DIGITS[k]
    return bin_

print("Brojevi binarnog brojcanog sistema od 0 do 20: ")
for i in range(20):
    print (getNumber(i))

print ("Broj 85 decimalno je",getNumber(85), "binarno!")
