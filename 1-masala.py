a = int(input("A ni kiriting: "))
b = int(input("B ni kiriting: "))

juft_sonlar = [son for son in range(a,b+1) if son%2==0]
print(juft_sonlar)