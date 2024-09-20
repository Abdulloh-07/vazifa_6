a = int(input("A ni kiriting: "))
b = int(input("B ni kiriting: "))

toq_sonlar = [son for son in reversed(range(a,b+1)) if son%2==1]
print(toq_sonlar)