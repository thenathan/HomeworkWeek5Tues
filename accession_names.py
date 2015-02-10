import re

accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

for acc in accs:
    if re.search(r"5", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"(d|e)", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"d.*e", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"(d.e)", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"^(x|y)", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"[0123456789]{3,100}", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"\d{3,}", acc):
        print ("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"d[arp]$", acc):
        print("\t" + acc)
