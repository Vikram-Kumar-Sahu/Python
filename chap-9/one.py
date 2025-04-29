f=open("text.txt")
string=f.read()
if ("twinkel" in string):
    print("twinkel present")
else:
    print("twinkel not present")
f.close
