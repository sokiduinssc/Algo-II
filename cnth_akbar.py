def ambil_input():
    data = (input("Masukkan sesuatu: "))
    return data

hasil = ambil_input()
print("Isi variabel hasil:", hasil)
print("Tipe data:", type(hasil))

# studi kasus dari tugas yang dibuat akbar
# diatas adalah inputan string, jika input menggunakan tipe data lainnya maka akan eror
# untuk mengantisipasi agar yang diinput jika yang diinput dibaca sebagai tipe data lain dan tidak eror saat ditampilkan
# maka menggunakan fungsi try-execpt, try–except adalah mekanisme penanganan kesalahan (error handling) di Python.
# Tujuannya agar program tidak langsung berhenti (crash) ketika terjadi kesalahan saat dijalankan (runtime error).

def ambil_input():
    data = input("Masukkan sesuatu: ")

    try:
        if "." in data:
            data = float(data)
        else:
            data = int(data)
    except ValueError:
        pass

    return data

hasil = ambil_input()
print("Isi variabel hasil:", hasil)
print("Tipe data:", type(hasil))