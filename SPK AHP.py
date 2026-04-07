# ==========================================
# SISTEM PENDUKUNG KEPUTUSAN - METODE AHP
# Versi Final Tanpa Library Tambahan
# ==========================================

# RANDOM INDEX (RI)
RI_dict = {
    1: 0.00,
    2: 0.00,
    3: 0.58,
    4: 0.90,
    5: 1.12,
    6: 1.24,
    7: 1.32,
    8: 1.41,
    9: 1.45,
    10: 1.49
}


# ==============================
# VALIDASI INPUT ANGKA
# ==============================
def input_angka(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai <= 0:
                print("Nilai harus lebih dari 0.")
            else:
                return nilai
        except:
            print("Input harus berupa angka!")


# ==============================
# INPUT DATA
# ==============================
def input_data():
    print("=" * 60)
    print("SISTEM PENDUKUNG KEPUTUSAN - METODE AHP")
    print("=" * 60)

    judul = input("Masukkan Judul SPK: ")

    while True:
        try:
            n = int(input("Masukkan jumlah kriteria (1-10): "))
            if 1 <= n <= 10:
                break
            else:
                print("Jumlah kriteria harus antara 1 - 10.")
        except:
            print("Input harus berupa angka!")

    kriteria = []
    for i in range(n):
        nama = input("Nama Kriteria ke-" + str(i+1) + ": ")
        kriteria.append(nama)

    return judul, n, kriteria


# ==============================
# INPUT MATRIKS PERBANDINGAN
# ==============================
def input_matriks(n, kriteria):
    matriks = []

    for i in range(n):
        baris = []
        for j in range(n):
            if i == j:
                baris.append(1.0)
            elif j < i:
                baris.append(1 / matriks[j][i])
            else:
                nilai = input_angka(
                    "Perbandingan " + kriteria[i] + 
                    " terhadap " + kriteria[j] + ": "
                )
                baris.append(nilai)
        matriks.append(baris)

    return matriks


# ==============================
# HITUNG JUMLAH KOLOM
# ==============================
def hitung_jumlah_kolom(matriks, n):
    jumlah_kolom = []
    for j in range(n):
        total = 0
        for i in range(n):
            total += matriks[i][j]
        jumlah_kolom.append(total)
    return jumlah_kolom


# ==============================
# NORMALISASI
# ==============================
def normalisasi_matriks(matriks, jumlah_kolom, n):
    normalisasi = []
    for i in range(n):
        baris = []
        for j in range(n):
            baris.append(matriks[i][j] / jumlah_kolom[j])
        normalisasi.append(baris)
    return normalisasi


# ==============================
# HITUNG PRIORITAS
# ==============================
def hitung_prioritas(normalisasi, n):
    prioritas = []
    for i in range(n):
        total = 0
        for j in range(n):
            total += normalisasi[i][j]
        prioritas.append(total / n)
    return prioritas


# ==============================
# UJI KONSISTENSI
# ==============================
def uji_konsistensi(matriks, prioritas, n):
    hasil = []

    for i in range(n):
        total = 0
        for j in range(n):
            total += matriks[i][j] * prioritas[j]
        hasil.append(total)

    lambda_list = []
    for i in range(n):
        lambda_list.append(hasil[i] / prioritas[i])

    lambda_max = sum(lambda_list) / n

    if n == 1:
        return lambda_max, 0, 0

    CI = (lambda_max - n) / (n - 1)
    RI = RI_dict[n]

    if RI == 0:
        CR = 0
    else:
        CR = CI / RI

    return lambda_max, CI, CR


# ==============================
# TAMPILKAN HASIL
# ==============================
def tampilkan_hasil(judul, kriteria, matriks, normalisasi, prioritas, lambda_max, CI, CR):
    n = len(kriteria)

    print("\n" + "=" * 60)
    print("HASIL PERHITUNGAN AHP")
    print("Judul :", judul)
    print("=" * 60)

    print("\nMatriks Perbandingan:")
    for i in range(n):
        for j in range(n):
            print("{:.4f}".format(matriks[i][j]), end="\t")
        print()

    print("\nMatriks Normalisasi:")
    for i in range(n):
        for j in range(n):
            print("{:.4f}".format(normalisasi[i][j]), end="\t")
        print()

    print("\nVektor Prioritas:")
    for i in range(n):
        print(kriteria[i], ":", round(prioritas[i], 4))

    print("\nUji Konsistensi:")
    print("Lambda Max :", round(lambda_max, 4))
    print("CI         :", round(CI, 4))
    print("CR         :", round(CR, 4))

    if CR < 0.1:
        print("Status     : Konsisten")
    else:
        print("Status     : Tidak Konsisten")


# ==============================
# MAIN PROGRAM
# ==============================
def main():
    judul, n, kriteria = input_data()
    matriks = input_matriks(n, kriteria)
    jumlah_kolom = hitung_jumlah_kolom(matriks, n)
    normalisasi = normalisasi_matriks(matriks, jumlah_kolom, n)
    prioritas = hitung_prioritas(normalisasi, n)
    lambda_max, CI, CR = uji_konsistensi(matriks, prioritas, n)

    tampilkan_hasil(judul, kriteria, matriks, normalisasi, prioritas, lambda_max, CI, CR)


if __name__ == "__main__":
    main()