# --- Validation Program ---
def validate_nama(nama):
    if nama.isalpha() == False:
        print("Nama tidak valid. Harus huruf.")
        return False
    else:
        return True

def validate_bulan(bulan):
    if bulan.isdigit() == False:
        print("Bulan tidak valid. Harus angka.")
        return False
    elif 1 <= int(bulan) <= 12:
        return True
    else:
        print("Bulan tidak valid. Silakan masukkan bulan antara 1 dan 12.")
        return False

def validate_jumlah_pemasukan(jumlah):
    if jumlah.isdigit() == False:
        print("Jumlah pemasukan tidak valid. Harus angka.")
        return False
    if int(jumlah) < 10000:
        print("Jumlah minimal 10.000")
        return False
    else:
        return True

def validate_jumlah_pengeluaran(jumlah):
    if jumlah.isdigit() == False:
        print("Jumlah pengeluaran tidak valid. Harus angka.")
        return False
    else:
        return True

# --- Kategori ---
kategori_pemasukan = ["Gaji", "Bonus", "Hasil investasi", "Hadiah", "Uang jajan", "Lainnya"]
kategori_pengeluaran = ["Makanan dan minuman", "Transportasi", "Tagihan", "Belanja", "Hiburan", "Pendidikan", "Kesehatan", "Donasi", "Investasi atau tabungan", "Lainnya"]

def pilih_kategori(kategori_list):
    print("\nPilih Kategori:")
    for i, kategori in enumerate(kategori_list, 1):
        print(f"{i}. {kategori}")
    pilihan = input("Masukkan nomor kategori: ")
    if pilihan.isdigit() and 1 <= int(pilihan) <= len(kategori_list):
        if kategori_list[int(pilihan) - 1] == "Lainnya":
            return input("Masukkan kategori lainnya: ")
        else:
            return kategori_list[int(pilihan) - 1]
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        return pilih_kategori(kategori_list)

# --- Main Program ---
while True:
    nama_user = input("Masukkan nama: ")
    if validate_nama(nama_user):
        break

while True:
    bulan = input("Masukkan bulan (1-12): ")
    if validate_bulan(bulan):
        break

daftar_pemasukan = []
daftar_pengeluaran = []

def tambah_pemasukan():
    jumlah = input("Masukkan jumlah pemasukan: ")
    if validate_jumlah_pemasukan(jumlah) == False:
        return tambah_pemasukan()
    else:
        jumlah = float(jumlah)
        kategori = pilih_kategori(kategori_pemasukan)
        daftar_pemasukan.append({'jumlah': jumlah, 'kategori': kategori})

def tambah_pengeluaran():
    jumlah = input("Masukkan jumlah pengeluaran: ")
    if validate_jumlah_pengeluaran(jumlah) == False:
        return tambah_pengeluaran()
    else:
        jumlah = float(jumlah)
        kategori = pilih_kategori(kategori_pengeluaran)
        daftar_pengeluaran.append({'jumlah': jumlah, 'kategori': kategori})

def gabung_transaksi(daftar_transaksi):
    hasil_gabungan = {}
    for transaksi in daftar_transaksi:
        kategori = transaksi['kategori']
        jumlah = transaksi['jumlah']
        if kategori in hasil_gabungan:
            hasil_gabungan[kategori] += jumlah
        else:
            hasil_gabungan[kategori] = jumlah
    return hasil_gabungan

def lihat_laporan():
    print("\n--- Laporan Keuangan ---")
    print("Nama:", nama_user, "| Bulan:", bulan)
    print("\nPemasukan:")
    total_pemasukan = 0
    gabungan_pemasukan = gabung_transaksi(daftar_pemasukan)
    for kategori, jumlah in gabungan_pemasukan.items():
        print("  ", kategori, ": Rp", jumlah)
        total_pemasukan += jumlah
    print("Total Pemasukan: Rp", total_pemasukan)

    print("\nPengeluaran:")
    total_pengeluaran = 0
    gabungan_pengeluaran = gabung_transaksi(daftar_pengeluaran)
    for kategori, jumlah in gabungan_pengeluaran.items():
        print("  ", kategori, ": Rp", jumlah)
        total_pengeluaran += jumlah
    print("Total Pengeluaran: Rp", total_pengeluaran)

    print("\nSaldo Akhir: Rp", total_pemasukan - total_pengeluaran)

def menu_utama():
    while True:
        print("\n--- Menu Utama ---")
        print("1. Input Pemasukan")
        print("2. Input Pengeluaran")
        print("3. Lihat Laporan Keuangan")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_pemasukan()
        elif pilihan == '2':
            tambah_pengeluaran()
        elif pilihan == '3':
            lihat_laporan()
        elif pilihan == '4':
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

menu_utama()