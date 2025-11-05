#Nama =Kresna Hono Putro
#NIM = 2501870
#Kelas =1B

print("Selamat datang, silahkan isi data diri anda")
nama = input("Masukan nama anda: ")
tahun_lahir = int(input("Masukan tahun lahir anda: "))
tempat_lahir = input("Masukkan Tempat anda lahir: ")
mbti = input("Masukkan MBTI anda: ")

umur = abs(2025 - tahun_lahir)

print(f"Halo nama anda: {nama}\nberumur: {umur} lahir di {tempat_lahir} dengan MBTI {mbti}")

