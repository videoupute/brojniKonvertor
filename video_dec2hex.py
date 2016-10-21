"""
Author: VideoUpute
URL:    https://www.youtube.com/channel/UC_0_Jm2Bn-0-ULn_By_1Odw
Video:  https://www.youtube.com/watch?v=MkAn6moL31E
"""

# cifre hexadecimalnog sistema
DIGITS = "0123456789ABCDEF"

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
for i in range(21):
    print (getNumber(i))

print ("Broj 85 decimalno je",getNumber(85), "hexadecimalno!")
