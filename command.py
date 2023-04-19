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

def searchusers(idicari,username):
    found = True
    i=1
    while found:
        if users[i][idicari]== username:
            return True
        else :
            i+=1
        if i > 102:
            return False
def searchcandi(idicari,username):
    found = True
    i=1
    while found:
        if users[i][idicari]== username:
            found = False
            return True
        else :
            i+=1
        if i > 101:
            found = False
            return False
        

def login():
    global username_login
    if username_login != '':
        print('Login gagal!')
        print(f'Anda telah login dengan username {username_login}, silahkan lakukan “logout” sebelum melakukan login kembali.')
    else :
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
                    
                    break    
            elif i == 102 :
                print('Username tidak terdaftar!')
                break
          
            
        

                 
#login nya harus diubah
def logout():
    global username_login
    for i in range(1,103):
        if users[i][0]=='login':
            users[i][0]=username_login
            username_login=''
            break
        elif i == 102 :
            print("Logout gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")




# sisa = 100
# for i in range(1,101):
#     if candi[i][0]!=0:
#         sisa -= 1


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
    if users[1][0]=='login':
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
                jenis_jin ='jin_pengumpul'

            else :
                print("Memilih jin 'Pembangun'.")
                jenis_jin ='jin_pembangun'

            username_jin = input('Masukkan username jin: ')
            while searchusers(0,username_jin):
                print(f'Username “{username_jin}” sudah diambil!')
                username_jin = input('Masukkan username jin: ')    
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
    else:
        print("Summon jin hanya dapat diakses bandung bondowoso")


def hapusjin():#belum selesai ada fungsi save
    if users[1][0]=='login':
        username_jin = input('Masukkan username jin : ')
        if searchusers(0,username_jin):
            konfirmasi = input('Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ')
            while konfirmasi != 'n' and konfirmasi !='N' and konfirmasi != 'y' and konfirmasi !='Y' :
                konfirmasi = input('Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ')
            if konfirmasi == 'y' or konfirmasi == 'Y':
                for i in range(3,102):
                    if users[i][0] == username_jin:
                        users[i][0] = 'kosong'
                        users[i][1] = 'kosong'
                        users[i][2] = 'kosong'
                for i in range(1,101): #bila jin sudah membangun candi
                    if candi[i][0]==username_jin:
                        candi[i][0]='0' #candi dihapus
                        candi[i][1]='kosong'
                        candi[i][2]=0
                        candi[i][3]=0
                        candi[i][4]=0
                        break
                print('Jin telah berhasil dihapus dari alam gaib.')
            else :
                print("Jin gagal dihapus")
        else :
            print('Tidak ada jin dengan username tersebut.')
    else :
        print('Hapus jin hanya dapat diakses Bandung Bondowoso.')





def ubahjin():
    if users[1][0]=='login':
        username_jin = input('Masukkan username jin : ')
        if searchusers(0,username_jin):
            for i in range(3,103):
                if users[i][0]== username_jin:
                    if users[i][2]=='jin_pengumpul':
                        ubah = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?')
                        while ubah != 'n' and ubah !='N' and ubah != 'y' and ubah !='Y' :
                            ubah = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?')
                        
                        if ubah == 'y' or ubah =='Y' :
                            users[i][2]='jin_pembangun'
                            print("Jin telah berhasil diubah.")
                            break
                        else :
                            print("Jin tidak diubah.")
                            break
                    elif users[i][2]=='jin_pembangun':
                        ubah = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?')
                        while ubah != 'n' and ubah !='N' and ubah != 'y' and ubah !='Y' :
                            ubah = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?')
                        
                        if ubah == 'y' or ubah =='Y' :
                            users[i][2]='jin_pengumpul'
                            print("Jin telah berhasil diubah.")
                            break
                        else :
                            print("Jin tidak diubah.")
                            break
        else :
            print('Tidak ada jin dengan username tersebut.')
    else :
        print('ubahjin hanya dapat diakses Bandung Bondowoso')

def kumpul():
    for i in range(103):
        if users[i][0]=='login':
            if users[i][2] == 'jin_pengumpul':
                pasir = random.randint(0,5)
                batu = random.randint(0,5)
                air = random.randint(0,5)
                bahan_bangunan[1][2]+=batu
                bahan_bangunan[2][2] += pasir
                bahan_bangunan[3][2]+= air
                print(f'Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.')
                break
            else :
                print('kumpul hanya dapat diakses jin pengumpul')
                break


def bangun():
    for i in range(103):
        if users[i][0] == 'login' :
            if users[i][2] == 'jin_pembangun':   
                for j in range(1,101):
                    idcandi=1 
                    if candi[j][0] == 0:
                        butuh_pasir = random.randint(1,5)
                        butuh_air = random.randint(1,5)
                        butuh_batu = random.randint(1,5)
                        if bahan_bangunan[1][2] > butuh_batu and bahan_bangunan[2][2]>butuh_pasir and bahan_bangunan[3][2]>butuh_air:
                            candi[j][0]=idcandi
                            candi[j][2]=butuh_pasir
                            candi[j][3]=butuh_batu
                            candi[j][4]=butuh_air
                            candi[j][1]=username_login
                            bahan_bangunan[1][2] -=butuh_batu
                            bahan_bangunan[2][2]-=butuh_pasir
                            bahan_bangunan[3][2]-=butuh_air
                            print('Candi berhasil dibangun')
                            totalcandi=100
                            for g in range(1,101):
                                if candi[g][0] != 0:
                                    totalcandi-=1
                            if totalcandi >= 0:
                                print(f'Sisa candi yang perlu dibangun: {totalcandi}.')
                                break
                            else:
                                totalcandi=0
                                bahan_bangunan[1][2] -=butuh_batu
                                bahan_bangunan[2][2]-=butuh_pasir
                                bahan_bangunan[3][2]-=butuh_air
                                print('Candi berhasil dibangun.')
                                print('Sisa candi yang perlu dibangun: 0.')
                                break
                        else :
                            print('Bahan bangunan tidak mencukupi.')
                            print('Candi tidak bisa dibangun!')
                            break
                    else :
                        idcandi+=1
                break
            elif users[i][2] != 'jin_pembangun':
                print('Hanya dapat diakses Jin Pembangun')
                break

# users[1][0]='login'
# summonjin()

# users[1][0]='Bondowoso'
# print(users[0:5])
# users[3][0]='login'
# bangun()
        



def batchkumpul():
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

def batchbangun():
    total_jin_pembangun = 0
    total_batu = 0
    total_pasir = 0
    total_air = 0
    totalcandi=100
    for i in range(3,103):
        if users[i][2]=='jin_pembangun':
            total_jin_pembangun +=1
    
    if total_jin_pembangun == 0:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
    else :
        username_jin = ["kosong" for i in range(total_jin_pembangun)]
        idjin =0
        for i in range(3,103):
            if users[i][2]=='jin_pembangun':
                username_jin[idjin]=users[i][0]
                idjin+=1



        bahan=[[0 for i in range (3)]for j in range(total_jin_pembangun)]
        for i in range(total_jin_pembangun):
            for j in range(3):
                bahan[i][j] = random.randint(1,5)
                if j == 0 :
                    total_batu += bahan[i][j]
                elif j == 1:
                    total_pasir += bahan[i][j]
                else:
                    total_air += bahan[i][j]
        print(f'Mengerahkan {total_jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.')
        if bahan_bangunan[1][2] > total_batu and bahan_bangunan[2][2]>total_pasir and bahan_bangunan[3][2]>total_air:
            for i in range(1,101):
                    idcandi=1
                    idusernamejin=0 
                    if candi[i][0] == 0:
                        # for j in range(total_jin_pembangun):
                        
                        candi[i][2]=bahan[idusernamejin][1]
                        candi[i][3]=bahan[idusernamejin][0]
                        candi[i][4]=bahan[idusernamejin][2]
                            # bahan[j][k]=0
                        candi[i][1]=username_jin[idusernamejin]
                        candi[i][0]=idcandi
                        idusernamejin+=1
                        bahan_bangunan[1][2] -= total_batu            
                        bahan_bangunan[2][2] -= total_pasir
                        bahan_bangunan[3][2] -= total_air
                        print(f'Jin berhasil membangun total {total_jin_pembangun} candi.')
                        
                            
                    else :
                        idcandi+=1
            
            # for g in range(1,101):
            #     if candi[g][0] != 0:
            #         totalcandi-=1   
            # if totalcandi >= 0:
            # bahan_bangunan[1][2] -= total_batu            
            # bahan_bangunan[2][2] -= total_pasir
            # bahan_bangunan[3][2] -= total_air
                      
                            
                            # totalcandi=100
                            # for g in range(1,101):
                            #     if candi[g][0] != 0:
                            #         totalcandi-=1
                            
                            #     print(f'Sisa candi yang perlu dibangun: {totalcandi}.')
                            #     break
                            # else:
                            #     totalcandi=0
                            #     bahan_bangunan[1][2] -=butuh_batu
                            #     bahan_bangunan[2][2]-=butuh_pasir
                            #     bahan_bangunan[3][2]-=butuh_air
                            #     print('Candi berhasil dibangun.')
                            #     print('Sisa candi yang perlu dibangun: 0.')
                            #     break
        else :
            print(f'Bangun gagal {total_pasir - bahan_bangunan[2][2]} pasir, {total_batu - bahan_bangunan[1][2]} batu, dan {total_air - bahan_bangunan[3][2]} air. ')
                     

        
        

def laporanjin():
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


def laporancandi():
    total_candi= 0
    total_pasir = 0
    total_batu = 0
    total_air = 0
    termahal = 0
    termurah = 0
    idtermurah=0
    idtermahal=0
    if users[1][0] =='login': 
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


def hancurkancandi():
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
def ayamberkokok():
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


def help():
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
            if users[i][0]=='login':
                if users[i][2]=='jin_pembangun':
                    print('1. logout ')
                    print('deskripsi')
                    print('2. bangun ')
                    print('deskripsi')
                    print('3. save ')
                    print('deskripsi')
                    break
                #belum selesaii
                else : #belum login
                    print('1. logout ')
                    print('deskripsi')
                    print('2. kumpul ')
                    print('deskripsi')
                    print('3. save ')
                    print('deskripsi')
                    break


def save():
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



