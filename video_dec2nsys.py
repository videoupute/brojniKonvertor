#cifre ili znakovi naseg sistema
DIGITS = "01AB!#"

def getNumber(dec):
	global DIGITS
	bin_ = ""
	rest = []

	while True:
		temp = dec % len(DIGITS)
		dec = int(dec/len(DIGITS))
		rest.append(temp)
		if dec == 0:
			break

	for c in rest[::-1]:
		bin_ += DIGITS[c]

	return bin_

for i in range(21):
	print(i,"=>",getNumber(i))

print("Broj 85 decimalno je", getNumber(85), "u nasem sistemu")
