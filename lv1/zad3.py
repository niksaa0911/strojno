import statistics

brojevi=[]

while True:
    broj=input("Unesite broj:")
    if broj.isdigit():
        brojevi.append(int(broj))
    elif broj=="Done" or broj=="done":
        break
    else:
        print("Niste unijeli broj.")

print("Korisnik je unio", len(brojevi), "brojeva")
print("Srednja vrijednost je:", sum(brojevi)/len(brojevi))
print("Max vrijednost je:", max(brojevi))
print("Min vrijednost je:", min(brojevi))

brojevi.sort()
print(brojevi)