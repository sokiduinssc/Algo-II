print("Masukkan Angka Tahun =")
tahun = int(input())
if tahun % 4 == 0:
    print("Tahun Kabisat")
else:
    if tahun % 100 == 0:
        print("BUkan Tahun Kabisat")
    else:
        if tahun % 400 == 0:
            print("Tahun kabisat ")
        else:
            print("Bukan Kabisat")
