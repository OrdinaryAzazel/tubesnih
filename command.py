import csv
import os
import sys
import random

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
for i in range(101):
    candi[i][0]=0
bahan_bangunan =[['kosong' for i in range(3)]for j in range(4)]
with open('bahan_bangunan.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    i = 0
    for row in reader :
            
            bahan_bangunan[i]=row
            i+=1
bahan_bangunan[1][0]='batu'
bahan_bangunan[2][0]='pasir'
bahan_bangunan[3][0]='air'
for i in range(1,4):
    bahan_bangunan[i][2]=0

username_login=''
def login():
    global username_login
    
    username = input("Username: ")
    password = input('Password: ')
    for i in range(1,103):
        if users[i][0]=='login':
            print('Login gagal!')
            print(f'Anda telah login dengan username {username_login}, silahkan lakukan “logout” sebelum melakukan login kembali.')
            break
        elif users[i][0]==username :
            if users[i][1]!=password:
                print("Password salah!")  
                break
            elif users[i][1]== password:
                print(f"Selamat datang,{username}")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                username_login = username
                users[i][0]= 'login'
                print(username_login)
                print(users[i][0])
                break    
        elif i == 102 :
            print('Username tidak terdaftar!')
            break
          
            
        

                 
#login nya harus diubah
def logout():
    for i in range(1,103):
        if users[i][0]=='login':
            users[i][0]=username_login
            print(f'udah logout {username_login}')
            break
        elif i == 102 :
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

def summonjin():
    print('Jenis jin yang dapat dipanggil:')
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - Bertugas membangun candi")
    
    jenis_jin=''
    jumlah_jin=0
    for i in range(3,103):
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
        i = 3
        while username_check:
            if users[i][0] != username_jin and users[i][0]=='kosong':
                username_check = False
                
            elif users[i][0]==username_jin:
                print(f'Username “{username_jin}” sudah diambil!')
                username_jin = input('Masukkan username jin: ')
                i=3
            else :
                i+=1
            
                
        password_jin = input('Masukkan password jin: ')
    
        while (len(password_jin) < 5 or len(password_jin) >25) :
            print('Password panjangnya harus 5-25 karakter!')
            password_jin = input('Masukkan password jin: ')
        for j in range(3,103):
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

def hapusjin():#belum selesai ada fungsi save
    username_jin = input('Masukkan username jin : ')
    for i in range(3,102):
        if users[i][0] == username_jin:
            users[i][0] = 'kosong'
            users[i][1] = 'kosong'
            users[i][2] = 'kosong'
            if True:#jika belum save
                for i in range(101):
                    if candi[i][0]==username_jin:
                        candi[i][0]='0' #candi dihapus
                        candi[i][1]='kosong'
                        candi[i][2]=0
                        candi[i][3]=0
                        candi[i][4]=0
                        break
    else :
        print('Tidak ada jin dengan username tersebut.')






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


def kumpul(users,bahan_bangunan):
    for i in range(3,103):
        if users[i][2]=='jin_pengumpul':
            pasir = random.randint(0,5)
            batu = random.randint(0,5)
            air = random.randint(0,5)
            bahan_bangunan[1][2]+=batu
            bahan_bangunan[2][2] += pasir
            bahan_bangunan[3][2]+= air
            print(f'Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.')
            break
    else :
        print("Tidak ada Jin Pengumpul yang sudah login.")


# def bangun(users,candi,bahan_bangunan):


def batchkumpul(users,bahan_bangunan):
    total_jin_pengumpul=0
    pasir=0
    batu = 0 
    air = 0
    for i in range(3,103):
        if users[i][2]=='jin_pengumpul':
            total_jin_pengumpul +=1
    if total_jin_pengumpul > 0 :
        print(f'Mengerahkan {total_jin_pengumpul} jin untuk mengumpulkan bahan.')
        for i in range(total_jin_pengumpul):
            pasir += random.randint(0,5)
            batu += random.randint(0,5)
            air += random.randint(0,5)
        bahan_bangunan[1][2]+=batu
        bahan_bangunan[2][2] += pasir
        bahan_bangunan[3][2]+= air
        print(f'Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.')
    else :
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')

#def batchbangun(users,candi,bahan_bangunan):

def laporanjin(users,candi,bahan_bangunan):
    if users[1][0] !='login':
        print('Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.')
    else :
        total_jin = 0
        total_jin_pengumpul = 0
        total_jin_pembangun = 0
        jin_terajin=''
        jin_termalas=''
        for i in range(3,103):
            if users[i][0] != 'kosong':
                total_jin +=1
                if users[i][2]=='jin_pembangun':
                    total_jin_pembangun +=1
                else :
                    total_jin_pengumpul += 1
        pasir = bahan_bangunan[2][2]
        batu = bahan_bangunan[1][2]
        air = bahan_bangunan[3][2]
        #cari jin terajin termalas
        # output
        print(f'Total Jin: {total_jin}')
        print(f'Total Jin Pengumpul: {total_jin_pengumpul}')
        print(f'Total Jin Pembangun: {total_jin_pembangun}')
        print(f'Jin Terajin: {jin_terajin}')
        print(f'Jin Termalas: {jin_termalas}')
        print(f'Jumlah Pasir: {pasir} unit')
        print(f'Jumlah Air: {air} unit')
        print(f'Jumlah Batu: {batu} unit')


def laporancandi(candi,users):
    total_candi= 0
    total_pasir = 0
    total_batu = 0
    total_air = 0
    termahal = 0
    termurah = 0
    idtermurah=0
    idtermahal=0
    if users[1][0] !='login': 
        for i in range(1,101):
            if candi[i][0] != 0: #asumsi candi yang belum terbangun bernilai 0
                total_candi +=1
                total_air+=int(candi[i][4])
                total_pasir+=int(candi[i][2])
                total_batu+=int(candi[i][3])
        harga= [0 for i in range(total_candi)] 
        j=0
        for i in range(1,101):
            if candi[i][0] != 0:
                harga[j]= 10000 * candi[i][2] + 15000 * candi[i][3] + 7500 * candi[i][4]
                j +=1
        termahal = max(harga,default=0)
        termurah = min(harga,default=0)
        for i in range(1,101):
            if (10000 * candi[i][2] + 15000 * candi[i][3] + 7500 * candi[i][4])==termahal:
                idtermahal = candi[i][0]
            elif (10000 * candi[i][2] + 15000 * candi[i][3] + 7500 * candi[i][4])==termurah:
                idtermurah = candi[i][0]
        print(f'Total Candi: {total_candi}')
        print(f'Total Pasir yang digunakan: {total_pasir}')
        print(f'Total Batu yang digunakan: {total_batu}')
        print(f'Total Air yang digunakan: {total_air}')
        if total_candi > 0:
            print(f'ID Candi Termahal: {idtermahal} (Rp {termahal})')
            print(f'ID Candi Termurah: {idtermurah} (Rp {termurah})')
        else :
            print(f'ID Candi Termahal: -')
            print(f'ID Candi Termurah: -')
    else :
        print('Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.')

# users[2][0]='login'


def hancurkancandi(candi,users):
    if users[2][0]=='login':
        id_hapus= int(input('Masukkan ID candi: '))
        for i in range(1,101):
            if id_hapus==candi[i][0]:
                konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_hapus} (Y/N)? ")
                while konfirmasi != 'Y' and konfirmasi != 'y' and konfirmasi != 'N' and konfirmasi != 'n':
                    konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_hapus} (Y/N)? ")
                if konfirmasi == 'y' or konfirmasi =='Y':
                    candi[i][1]='kosong'
                    for j in range(5):
                        if j!=1:
                            candi[i][j]=0
                    print('Candi telah berhasil dihancurkan.')
                    
                    break
                else :
                    print('Candi tidak dihancurkan.')
        else :
            print('Tidak ada candi dengan ID tersebut.')           
    else :
        print('Hancurkan Candi hanya dapat diakses oleh akun Bandung Bondowoso.')

# for j in range(1,101):
#     candi[j][0]= random.randint(1,100)
# print(candi)
def ayamberkokok(candi):
    print('Kukuruyuk.. Kukuruyuk..')
    jumlah_candi=0
    for i in range(1,101):
        if candi[i][0] != 0:
            jumlah_candi += 1
    if jumlah_candi < 100 :
        print(f'Jumlah Candi: {jumlah_candi}')
        print('')
        print(f'Selamat, Roro Jonggrang memenangkan permainan!')
        print("")
        print("*Bandung Bondowoso angry noise*")
        print('Roro Jonggrang dikutuk menjadi candi.')
        quit()
    else :
        print(f'Jumlah Candi: {jumlah_candi}')
        print('')
        print('Yah, Bandung Bondowoso memenangkan permainan!')
        quit()

# def load()


def help(users):
    print('=========== HELP ===========')
    if users[1][0]=='login':
        print('1. logout')
        print('Deskripsi')
        print('2. summonjin')
        print('Deskripsi')
        print('3. hapusjin')
        print('Deskripsi')
        print('4. ubahjin')
        print('Deskripsi')
        print('5. batchkumpul')
        print('Deskripsi')
        print('6. batchbangun')
        print('Deskripsi')
        print('7. laporanjin')
        print('Deskripsi')
        print('8. laporancandi')
        print('Deskripsi')
        print('9. save')
        print('deskripsi')
    elif users[2][0]=='login':
        print('1. logout')
        print('Deskripsi')
        print('2. hancurkancandi')
        print('Deskripsi')
        print('3. ayamberkokok')
        print('Deskripsi')
        print('4. save')
        print('Deskripsi')
    else:
        for i in range(3,103):
            if users[i][2]=='jin_pembangun':
                print('Role Jin Pembangun')
                print('1. ')
                #belum selesaii
        else : #belum login
            print('1. login')
            print('Deskripsi')
            print('2. exit')
            print('Deskripsi')


def save(users,candi,bahan_bangunan):
    folder = input('Masukkan nama folder: ')
    print('')
    print('')
    print('Saving...')
    print('')
    isExist = os.path.exists(save/folder)
    
    if not isExist:
        os.makedirs(save/folder)
        #save new csv file
    elif isExist :
        print(f'Berhasil menyimpan data di folder ')
        #save csv file
    print(f'Berhasil menyimpan data di folder save/{folder} ! ')



