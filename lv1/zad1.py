def total_euro(broj_sati, satnica):
    return broj_sati*satnica
    

broj_sati=float(input("Unesite broj sati:"))
satnica=float(input("Unesite satnicu:"))
total=total_euro(broj_sati, satnica)
print(f"Korisnik je zaradio: {total}")
