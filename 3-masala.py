matn = ['salom',123,True,'Hayr','world',3.14,'7214']
text = []
onother = []
for string in matn:
    if type(string) == str:
        text.append(string)
    else:
        onother.append(string)

text.sort()
onother.sort(reverse=True)
print(f"Text listida {text}")
print(f"Boshqa listda {onother}")