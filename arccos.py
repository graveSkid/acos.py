import math
from sys import argv

SUP_COS = ("Cos\u207B\u00b9")

print("Beregn " + SUP_COS)
print("\n")

def arccos():
    cos = float(input("Tast venligst din cos-værdi her: \n>"))
    print("\n")
    arccos_input = math.acos(cos)
    arccos_output = math.degrees(arccos_input)
    farccos = str(arccos_output)
    print(f"{SUP_COS}({cos}) = {farccos}\u00b0")

arccos()
