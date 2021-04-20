class siswa:
    jumlah_siswa = 0
    def __init__(self, nama, kelas, alamat, nilai):
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.nilai = nilai
        siswa.jumlah_siswa =+ 1

    def viewSiswa(self):
        print("-------------------")
        print("Data Siswa")
        print("Nama  :  ", self.nama)
        print("Kelas :  ", self.kelas)
        print("Alamat : ", self.alamat)
        print("-------------------")

    def viewNilai(self):
        print("Data Nilai")
        print("Nama : ", self.nama)
        for nilai in self.nilai:
            print("Nilai : ", nilai)
        print("-------------------")

    def viewKeterangan(self):
        print("Keterangan")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata : ", rata)
        if rata > 75:
            keterangan = "Lulus."
        else:
            keterangan = "Tidak lulus."
        print("Keterangan : ", keterangan)
        print("------------------")

siswa1 = siswa("Alex", "XII IIS", "Sleman", (90,80,89,77))
siswa2 = siswa("Umi", "XII MIPA 5", "Yogyakarta", (90,94,88,80))

siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)

siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)