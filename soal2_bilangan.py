def bilangan_prima(a):
    prima = True
    if a < 2:
        prima = False
    
    for i in range (2, int(a**0.5)+1):
        if (a % i == 0):
            prima = False

    return prima

def bilangan_kategori(b):
    kategori = []

    if isinstance(b, int):
        kategori.append("Bilangan Bulat")
        
        if b >= 0:
            kategori.append("Bilangan Cacah")

        if b < 0:
            kategori.append("Bilangan Negatif")
        
        if b == 0:
            kategori.append("Bilangan Nol")
        
        if b > 0:
            kategori.append("Bilangan Asli")
        
        if b % 2 == 0:
            kategori.append("Bilangan Genap")
        else:
            kategori.append("Bilangan Ganjil")

        if bilangan_prima(b):
            kategori.append("Bilangan Prima")
        elif b > 1:
            kategori.append("Bilangan Komposit")

    return kategori

def main():
    bilangan = int(input("Masukkan Bilangan : "))
    kategori = bilangan_kategori(bilangan)
    kategori_string = ", ".join(kategori)

    print(f"kategori dari bilangan {bilangan} adalah : {kategori_string}")

main()