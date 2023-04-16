import csv
import os
import sys

users=[['kosong' for i in range(3)]for j in range(103)]
with open('user.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    i = 0
    for row in reader :
            
            users[i]=row
            i+=1
candi =[['kosong' for i in range(5)]for j in range(101)]
with open('candi.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    i = 0
    for row in reader :
            
            candi[i]=row
            i+=1
# print(users)
# print(candi)
# def check():
# Bondo = False
# Roro = True

def login(users):
      loginstatus = False
      while True :
        username = input("Username: ")
        password = input('Password: ')
        for i in range(3):
            if users[i][0]==username :
                if users[i][1]!=password:
                    print("Password salah!")
                    
                    break
                elif users[i][1]== password:
                    print(f"Selamat datang,{username}")
                    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    if users[i][0]=='Bondowoso':
                        users[i][0]='login'
                    else :
                        users[i][0]='login'
                    #     Bondo = True
                         
                    #     return Bondo
                    # else :
                    #     Roro = True
                    #     return Roro
                    # loginstatus = True
                    # return loginstatus

                    # break
            elif i == (3-1):
                 print('Username tidak terdaftar!')
                 

def logout(users):
    if users[1][0]=='login':
        users[1][0]='Bondowoso'
    elif users[2][0]=='login'  :
        users[2][0]=='Roro'
        #keluar dari akun
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

def exit():

    keluar = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')       
    while keluar != "n" and keluar != 'y' and keluar != 'N' and keluar != 'Y':
        keluar = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')
    if keluar == 'n' or keluar == 'N':
        quit()

    else :
        quit()
        #fungsi f04 and exit
#belumberes

def summonjin(users):
    print('Jenis jin yang dapat dipanggil:')
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - Bertugas membangun candi")
    
    jenis_jin=''
    jumlah_jin=0
    for i in range(103):
        if users[i][0]=='kosong':
            jumlah_jin+=1
    if jumlah_jin==0 :
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
    else:
        nomorjin= int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
        while (nomorjin != 1) and (nomorjin != 2):
            print(f'Tidak ada jenis jin bernomor "{nomorjin}"!')
            nomorjin= int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
        if nomorjin == 1 :
            print("Memilih jin 'Pengumpul'.")
            jenis_jin = 'jin_pengumpul'

        else :
            print("Memilih jin 'Pembangun'.")
            jenis_jin = 'jin_pembangun'

        username_jin = input('Masukkan username jin: ')
        
        username_check= True
        while username_check:
            for i in range(103):
                if users[i][0]==username_jin:
                    print(f'Username “{username_jin}” sudah diambil!')
                    username_jin = input('Masukkan username jin: ')
            username_check=False
        password_jin = input('Masukkan password jin: ')
    
        while (len(password_jin) < 5 or len(password_jin) >25) :
            print('Password panjangnya harus 5-25 karakter!')
            password_jin = input('Masukkan password jin: ')
        for j in range(103):
            if users[j][0] == 'kosong':
                users[j][0] = username_jin
                users[j][1] = password_jin
                users[j][2] = jenis_jin
                break
        print('Mengumpulkan sesajen...')
        print('Menyerahkan sesajen...')
        print('Membacakan mantra...')
        print("")
        print(f"Jin {username_jin} berhasil dipanggil!")
def hapusjin(users,candi):
    username_jin = input('Masukkan username jin : ')
    for i in range(1,102):
        if users[i][0] == username_jin:
            users[i][0] = 'kosong'
            users[i][1] = 'kosong'
            users[i][2] = 'kosong'
            if True:#jika belum save
                for i in range(101):
                    if candi[i][0]==username_jin:
                        candi[i][0]='kosong1' #candi dihapus
                        candi[i][1]='kosong1'
                        candi[i][2]='kosong1'
                        candi[i][3]='kosong1'
                        candi[i][4]='kosong1'
                        break
    else :
        print('Tidak ada jin dengan username tersebut.')




# def search(users,indexdicari,stringdicari):
#     found = False
#     for i in range(103):
#         if users[indexdicari][]

def ubahjin(users):
    username_jin = input('Masukkan username jin : ')
    for i in range(103):
        if users[i][0]== username_jin:
            if users[i][2]=='jin_pengumpul':
                ubah = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?')
                while ubah != 'n' and ubah !='N' and ubah != 'y' and ubah !='Y' :
                    ubah = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?')
                
                if ubah == 'y' or ubah =='Y' :
                    users[i][2]='jin_pembangun'
                    break
                else :
                    break
            elif users[i][2]=='jin_pembangun':
                ubah = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?')
                while ubah != 'n' and ubah !='N' and ubah != 'y' and ubah !='Y' :
                    ubah = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?')
                
                if ubah == 'y' or ubah =='Y' :
                    users[i][2]='jin_pengumpul'
                    break
                else :
                    break
    else :
        print('Tidak ada jin dengan username tersebut.')
