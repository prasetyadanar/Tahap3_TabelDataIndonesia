def fungsi_fpb(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def fungsi_kpk(a,b):
    return abs(a*b) // fungsi_fpb(a, b)

def main():
    a = int(input("Masukan Bilangan Pertama : "))
    b = int(input("Masukan Bilangan Kedua : "))

    fpb = fungsi_fpb(a, b)
    kpk = fungsi_kpk(a, b)

    print(f"FPB dari {a} dan {b} adalah : {fpb}")
    print(f"KPK dari {a} dan {b} adalah : {kpk}")

main()