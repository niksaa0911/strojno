print("Upisite ocjenu:")
try:
    ocjena = float(input())
    if(ocjena < 0.0 or ocjena > 1.0):
        raise ValueError
    if ocjena >= 0.9:
        print("A")
    elif ocjena >= 0.8:
        print("B")
    elif ocjena >= 0.7:
        print("C")
    elif ocjena >= 0.6:
        print("D")
    elif ocjena < 0.6:
        print("F")
except:
    print("Pogresna vrijednost")