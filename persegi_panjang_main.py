from persegi_panjang import PersegiPanjang


def baca_ukuran(nama_ukuran: str) -> int:
    while True:
        try:
            return int(input(f"Masukkan {nama_ukuran} (cm): "))
        except ValueError:
            print("Inputnya harus angka bulat, coba lagi.\n")


def main() -> None:
    while True:
        try:
            panjang = baca_ukuran("panjang")
            lebar = baca_ukuran("lebar")

            p1 = PersegiPanjang(panjang, lebar)
            break
        except ValueError as e:
            print("Error:", e)
            print("Silakan masukkan ulang.\n")

    print(p1)
    print("Keliling:", p1.keliling(), "cm")
    print("Luas:", p1.luas(), "cm2")


if __name__ == "__main__":
    main()