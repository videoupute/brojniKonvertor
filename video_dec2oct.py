"""
Author: VideoUpute
URL:    https://www.youtube.com/channel/UC_0_Jm2Bn-0-ULn_By_1Odw
Video:  https://www.youtube.com/watch?v=03sKe5GI8r8
"""

# cifre oktalnog sistema
DIGITS = "01234567"

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

print ("Broj 85 decimalno je",getNumber(85), "oktalno!")
