from persegi_panjang import PersegiPanjang

def main():
    while True:
        try:
            panjang = int(input("Masukkan panjang (cm): "))
            lebar = int(input("Masukkan lebar (cm): "))

            p1 = PersegiPanjang(panjang, lebar)
            break
        except ValueError as e:
            print("Error:", e)
            print("Silakan masukkan ulang.\n")

    print(p1)
    print("Keliling:", p1.keliling(), "cm")
    print("Luas:", p1.luas(), "cm2")