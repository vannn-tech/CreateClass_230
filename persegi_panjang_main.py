from persegi_panjang import PersegiPanjang


def baca_ukuran(nama_ukuran: str) -> int:
    while True:
        try:
            ukuran = int(input(f"Masukkan {nama_ukuran} (cm): "))
            if ukuran <= 0:
                print("Ukurannya harus lebih dari 0, coba lagi.\n")
                continue
            return ukuran
        except ValueError:
            print("Inputnya harus angka bulat, coba lagi.\n")


def main() -> None:
    panjang = baca_ukuran("panjang")
    lebar = baca_ukuran("lebar")
    persegi_panjang = PersegiPanjang(panjang, lebar)

    print("Hasil perhitungan:")
    print(persegi_panjang)
    print(f"Keliling: {persegi_panjang.keliling()} cm")
    print(f"Luas: {persegi_panjang.luas()} cm²")


if __name__ == "__main__":
    main()