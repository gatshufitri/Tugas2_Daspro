welcome = '''
=================================
=========Selamat Datang==========
==========Di Cek Gaji============
=================================
'''
print (welcome)
hari_kerja = 25
hari_kerja_perbulan = 30 
hari_lembur = 20
gaji_pokok = 5000000
uang_lembur_perhari = 150000

total_gaji = (hari_kerja/hari_kerja_perbulan)*gaji_pokok+(hari_lembur*uang_lembur_perhari)
total_gaji = int (total_gaji)
print ("Gaji Anda Bulan Ini Rp. {:,}".format (total_gaji))