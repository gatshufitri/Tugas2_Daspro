selamat = '''
+++++++++++++++++++++++++++++++++++++++
+++++++++Selamat Belajar Elif++++++++++
+++++++++++++++++++++++++++++++++++++++
'''
print (selamat)

nama = input("Masukan Nama Anda : ")
umur = int(input("Masukan Umur Anda : "))
tinggi_badan = float(input("Masukan Tinggi Badan Anda : "))
berat_badan = float(input("Masukan Berat Badan Anda : "))

x = '''
Biodata Anda'''
print (x)

print ("Nama Saya",nama)
if umur > 17:
    print("Anda Sudah Remaja")
elif umur < 17:
    print("Anda Belum Remaja")

if tinggi_badan > 165:
    print("Anda Tinggi")
elif tinggi_badan < 165:
    print("Anda Pendek")

if berat_badan > 70 :
    print("Anda Sangat Berat Kurangi Makan Anda")
elif berat_badan < 70 :
    print("Berat Badan Anda Ideal")