print('-------------------------------------------------------------------------')
print('Nama     :Rabiatul Hikmah                     ')
print('Nim      :2409116049                          ')
print('Program  :Menghitung gaji karyawan berdasarkan jam kerja dan tarif kerja.   ')
print('-------------------------------------------------------------------------')

Nama = str(input("\nMasukkan nama: "))
Nim = int(input("Nim:"))
Kelas = str(input("kelas:"))
print(f"\n-----selamat datang {Nama}----- ")

while True:
    tarif_kerja =int(input("masukkan tarif kerja per jam:"))
    jam_kerja =int(input("Masukkan jam kerja:"))
    gaji = jam_kerja * tarif_kerja
    print(f"jumlah gaji Rp.{gaji}")
    if jam_kerja >= 160:
        bonus = 0.10 * gaji 
        gaji_setelah_bonus = gaji + bonus
        print(f"jam kerja lebih dari 160 jam. Kamu Mendapatkan bonus sebesar 10%. Total bonus Rp.{bonus}")
        print(f"gaji setelah bonus Rp. {gaji_setelah_bonus:.2f}")
    else:
        gaji_setelah_bonus = gaji
        print(f"jam kerja kamu kurang dari 160 jam, kamu tidak mendapatkan bonus. Total gaji Rp. {gaji_setelah_bonus:.2f}")
        
    pilihan = input("\nApakah kamu ingin menghitung gaji lagi? (yes/no):").lower()
    if pilihan == "yes":
        print("\nsilahkan menghitung kembali...")
    elif pilihan == "no":
        print("\nPROGRAM BERHENTI!!!")
        break
    else:
        print("input tidak valid masukkan 'yes/no'")