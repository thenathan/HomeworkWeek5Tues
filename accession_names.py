import re

accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

for acc in accs:
    if re.search(r"5", acc):
        print("\t" + acc)

print ("\n")

for acc in accs:
    if re.search(r"(d|e)", acc):
        print("\t" + acc)
