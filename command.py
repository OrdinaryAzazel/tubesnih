
import os,random,argparse
parser = argparse.ArgumentParser()
parser.add_argument('path', type = str, nargs="?", const="")
args = parser.parse_args()
parents_path = os.getcwd()+ '\\' + 'save'

if not args.path:
    print("Tidak ada nama folder yang diberikan!")
    path_data_user = f"{parents_path}\\user.csv"
    path_data_candi = f"{parents_path}\\candi.csv"
    path_data_bahan_bangunan = f"{parents_path}\\bahan_bangunan.csv"
elif os.path.exists(f"{parents_path}\\{args.path}"):
    print('Loading...')
    path_data_user = f"{parents_path}\\{args.path}\\user.csv"
    path_data_candi = f"{parents_path}\\{args.path}\\candi.csv"
    path_data_bahan_bangunan = f"{parents_path}\\{args.path}\\bahan_bangunan.csv"
    print('Selamat datang di program “Manajerial Candi”')
else:
    path_data_user = f"{parents_path}\\user.csv"
    path_data_candi = f"{parents_path}\\candi.csv"
    path_data_bahan_bangunan = f"{parents_path}\\bahan_bangunan.csv"
    print(f"Folder ,\"{args.path}\" tidak ditemukan.")

def read_user(file_csv):
    with open(file_csv) as csv:
        data = csv.readlines()
        listdata=[['kosong' for i in range(3)]for j in range(103)]
        i = 0
        for baris in data:
            j = 0
            ruang = [0 for i in range (3)]
            temp = ''
            for huruf in baris:
                if huruf == ';' or huruf == '\n':
                    ruang[j] = temp
                    j += 1
                    temp = ''
                elif huruf!='kosong':
                    temp += huruf
            listdata[i]=ruang
            i += 1
        
        return listdata
users=read_user(path_data_user)
def read_bahan(file_csv):
    with open(file_csv) as csv:
        data = csv.readlines()
        listdata = [['kosong' for i in range(3)] for i in range (4)]
        i = 0
        for baris in data:
            j = 0
            ruang = [0 for i in range (3)]
            temp = ''
            for huruf in baris:
                if huruf == ';' or huruf == '\n':
                    ruang[j] = temp
                    j += 1
                    temp = ''
                else:
                    temp += huruf
            listdata[i] = ruang
            i += 1
        return listdata
bahan_bangunan=read_bahan(path_data_bahan_bangunan)
def procedure_bahan():
    bahan_bangunan[1][0]='batu'
    bahan_bangunan[1][1]='bahan keras nih kayanya'
    bahan_bangunan[2][0]='pasir'
    bahan_bangunan[2][1]='bahan lembut inimah'
    bahan_bangunan[3][0]='air'
    bahan_bangunan[3][1]='bahan cairr banget'
    for i in range(1,4):
        bahan_bangunan[i][2]=0
procedure_bahan()
def read_candi(file_csv):
    with open(file_csv) as csv: 
        data = csv.readlines()
        listdata = [[0 for i in range(5)] for j in range (101)]
        for i in range(1,101):
            for j in range(2,5):
                listdata[i][j] = 0
        i = 0
        for baris in data :
            j = 0
            part = [0 for i in range(5)]
            temp = ""
            for huruf in baris:
                if huruf == ";" or huruf == "\n":
                    part[j] = temp
                    j += 1
                    temp = ""
                elif huruf!='kosong':
                    temp += huruf
                elif huruf != 0:
                    temp += huruf

                
            if temp != "":
                part[j] = temp
            listdata[i] = part
            i += 1
        
        return (listdata)
candi = read_candi(path_data_candi)
for i in range(1,101):
    for j in range(5):
        if candi[i][0] !=0:
            if j != 1:
                candi[i][j]=int(candi[i][j])
            else :
                candi[i][j]=candi[i][j]
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
def exit():

    keluar = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')       
    while keluar != "n" and keluar != 'y' and keluar != 'N' and keluar != 'Y':
        keluar = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')
    if keluar == 'n' or keluar == 'N':
        quit()

    else :
        save()
        quit()
        #fungsi f04 and exit
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
def hapusjin():
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
                idcandi=1
                for j in range(1,101):
                     
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
    if users[1][0]=='login':
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
                looping =total_jin_pembangun
                idcandi=1
                idusernamejin=0 
                for i in range(1,101):
                        if candi[i][0] == 0:
                            # for j in range(total_jin_pembangun):
                            candi[i][2]=bahan[idusernamejin][1]
                            candi[i][3]=bahan[idusernamejin][0]
                            candi[i][4]=bahan[idusernamejin][2]
                            candi[i][1]=username_jin[idusernamejin]
                            candi[i][0]=idcandi
                            idusernamejin+=1
                            idcandi+=1
                            looping-=1
                            if idusernamejin == total_jin_pembangun :
                                break
                
                        else :
                            idcandi+=1
                bahan_bangunan[1][2] -= total_batu            
                bahan_bangunan[2][2] -= total_pasir
                bahan_bangunan[3][2] -= total_air
                  
                print(f'Jin berhasil membangun total {total_jin_pembangun} candi.')
        
            else :
                kurang_pasir=total_pasir - bahan_bangunan[2][2]
                kurang_batu = total_batu - bahan_bangunan[1][2]
                kurang_air= total_air - bahan_bangunan[3][2]
                if kurang_air>0 and kurang_pasir>0 and kurang_batu>0 :
                    print(f'Bangun gagal kurang {(total_pasir - bahan_bangunan[2][2])} pasir, {total_batu - bahan_bangunan[1][2]} batu, dan {total_air - bahan_bangunan[3][2]} air. ')
                elif kurang_air>0 and kurang_batu>0 :
                    print(f'Bangun gagal kurang {total_batu - bahan_bangunan[1][2]} batu dan {total_air - bahan_bangunan[3][2]} air. ')
                elif kurang_air > 0 and kurang_pasir>0:
                    print(f'Bangun gagal kurang {total_pasir - bahan_bangunan[2][2]} pasir dan {total_air - bahan_bangunan[3][2]} air. ')
                elif kurang_batu > 0 and kurang_pasir>0:
                    print(f'Bangun gagal kurang {total_pasir - bahan_bangunan[2][2]} pasir dan {total_batu - bahan_bangunan[1][2]} batu. ')
                elif kurang_pasir>0:
                    print(f'Bangun gagal kurang {total_pasir - bahan_bangunan[2][2]} pasir.')
                elif kurang_batu>0:
                    print(f'Bangun gagal kurang {total_batu - bahan_bangunan[1][2]} batu.')
                elif kurang_air>0:
                    print(f'Bangun gagal kurang {total_air - bahan_bangunan[3][2]} air.')
    else :
        print("Hanya dapat diakses Bandung BOndowoso.")
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
        
        total_candi = 0
        for i in range(1,101):
            if candi[i][0] != 0:
                total_candi+=1
        if total_candi==0:
            jin_terajin='-'
            jin_termalas= '-'
        else :
            jin= terajin()
            jin_terajin=jin[0]
            jin_termalas=jin[1]
        

        
        
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
    rajinbangun = 0
    malesbangun =0
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
def terajin():
    totaljinpembangun=0
    for i in range(103):
        if users[i][2] == 'jin_pembangun':
            totaljinpembangun +=1
    jin_dan_totalcandi=[['kosong' for i in range(2)]for j in range(totaljinpembangun)]
    g= 0
    for i in range(3,103):
        if users[i][2] == 'jin_pembangun':
            jin_dan_totalcandi[g][0]=users[i][0]
            g+=1
    for i in range(totaljinpembangun):
        jin_dan_totalcandi[i][1]=0

    for i in range(1,101):
        if candi[i][0] !=0 :
            j=0
            while True:
                
                if jin_dan_totalcandi[j][0]==candi[i][1]:
                    jin_dan_totalcandi[j][1]+=1
                    break
                else :
                    j+=1
    print(jin_dan_totalcandi)
    terbanyak=0
    
    iddicarimax=0
    for i in range(totaljinpembangun):
        if jin_dan_totalcandi[i][0] != 'kosong':
            
            if jin_dan_totalcandi[i][1]>terbanyak:
                iddicarimax=i
                terbanyak = jin_dan_totalcandi[i][1]
            elif jin_dan_totalcandi[i][1]==terbanyak:
                if jin_dan_totalcandi[i][1]==jin_dan_totalcandi[iddicarimax][1]:
                    jin1=jin_dan_totalcandi[i][0]
                    jin2=jin_dan_totalcandi[iddicarimax][0]
                    if jin1<jin2:
                        iddicarimax=i
                        terbanyak = jin_dan_totalcandi[i][1]
                    else :
                        terbanyak = jin_dan_totalcandi[iddicarimax][1]
    tersedikit=terbanyak
    iddicarimin=0
    for i in range(totaljinpembangun):
        if jin_dan_totalcandi[i][0] != 'kosong':
            if jin_dan_totalcandi[i][1]<tersedikit:
                iddicarimin=i
                tersedikit = jin_dan_totalcandi[i][1]
            elif jin_dan_totalcandi[i][1]==tersedikit:
                if jin_dan_totalcandi[i][1]==jin_dan_totalcandi[iddicarimin][1]:
                    jin1=jin_dan_totalcandi[i][0]
                    jin2=jin_dan_totalcandi[iddicarimin][0]
                    if jin1>jin2:
                        iddicarimin=i
                        tersedikit = jin_dan_totalcandi[i][1]
                    else :
                        tersedikit = jin_dan_totalcandi[iddicarimin][1]
    jin=['kosong' for i in range(2)]
    jin[0]=jin_dan_totalcandi[iddicarimax][0]
    jin[1]=jin_dan_totalcandi[iddicarimin][0]
    # print(jin)
    return(jin)


                
                    

                # iddicari = i
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
        print('Hancurkan Candi hanya dapat diakses oleh akun Roro Jongrang.')
def ayamberkokok():
    if users[2][0]== 'login':
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
    else :
        print("Hanya bisa diakses roro jonggrang!")
def help():
    print('=========== HELP ===========')
    if users[1][0]=='login':
        print('1. logout')
        print('   Keluar dari akun saat ini')
        print('2. summonjin')
        print('   Memanggil jin jahanam dari alam ghaib:Pengumpul atau Pembangun!')
        print('3. hapusjin')
        print('   Menghapus jin jahanam')
        print('4. ubahjin')
        print('   Mengubah jin pembangun menjadi pengumpul atau sebaliknya')
        print('5. batchkumpul')
        print('   Mengumpulkan bahan dengan semua jin pengumpul')
        print('6. batchbangun')
        print('   Membangun candi dengan semua jin pembangun')
        print('7. laporanjin')
        print('   Melihat data laporan jin')
        print('8. laporancandi')
        print('   Melihat data candi terbangun')
        print('9. save')
        print('   Menyimpan progress')
        print('10.exit')
        print('   Keluar dari program')
    elif users[2][0]=='login':
        print('1. logout')
        print('   Keluar dari akun saat ini')
        print('2. hancurkancandi')
        print('   Menghancurkan candi yang telah terbangun')
        print('3. ayamberkokok')
        print('   Menghentikan permainan dengan teriak ayam')
        print('4. save')
        print('   Menyimpan progress')
        print('5. exit')
        print('   Keluar dari program')
    else:
        belumlogin=True
        for i in range(3,103):
            if users[i][0]=='login':
                belumlogin = False
                if users[i][2]=='jin_pembangun':
                    print('1. logout ')
                    print('   Keluar dari akun saat ini')
                    print('2. bangun ')
                    print('   Membangun candi')
                    print('3. save ')
                    print('   Menyimpan progress')
                    print('4. exit')
                    print('   Keluar dari program')
                    break
                #belum selesaii
                else : 
                    print('1. logout ')
                    print('   Keluar dari akun')
                    print('2. kumpul ')
                    print('   Mengumpulkan bahan bangunan')
                    print('3. save ')
                    print('   Menyimpan progress')
                    print('4. exit')
                    print('   Keluar dari program')
                    break
                
        if belumlogin:
            print('1. login')
            print('   Masuk ke dalam akun.')
            print('2. exit')
            print('   Keluar dari program')
            print('3. save')
            print('   Menyimpan Proses')
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type = str, nargs="?", const="")
    args = parser.parse_args()
    parents_path = os.getcwd()+ '\\' + 'save'
    if not args.path:
        print("Tidak ada nama folder yang diberikan!")
    elif os.path.exists(f"{parents_path}\\{args.path}"):
        print('Loading...')
        path_data_user = f"{parents_path}{args.path}\\user.csv"
        path_data_candi = f"{parents_path}{args.path}\\candi.csv"
        path_data_bahan_bangunan = f"{parents_path}{args.path}\\bahan_bangunan.csv"
        print('Selamat datang di program “Manajerial Candi”')
    else:
        print(f"Folder ,\"{args.path}\" tidak ditemukan.")
def tocsv(file,data,n1,n2):
    string=''
    f = open(file, 'w+')
    for i in range(n1):
        for j in range(n2):
            if j != (n2-1):
                string = string + str(data[i][j]) + ';'
            else :
                string = string + str(data[i][j])
        string = string + "\n"
        f.write(string)
        string=''
    f.close()
def save():
    
    folder = input('Masukkan nama folder: ')
    print('')
    print('')
    print('Saving...')
    print('')
    isExist = os.path.exists('save')
    logout()  
    if isExist:
        if os.path.exists(f'save\\{folder}'):
            tocsv(f'save\\{folder}\\user.csv',users,103,3)
            tocsv(f'save\\{folder}\\candi.csv',candi,101,5)
            tocsv(f'save\\{folder}\\bahan_bangunan.csv',bahan_bangunan,1,3)
        else :

            os.makedirs(f'save\\{folder}')
            print(f'Membuat folder save/{folder}!')
            tocsv(f'save\\{folder}\\user.csv',users,103,0)
            tocsv(f'save\\{folder}\\candi.csv',candi,101,0)
            tocsv(f'save\\{folder}\\bahan_bangunan.csv',bahan_bangunan,4,0)
        print(f'Berhasil menyimpan data di folder save/{folder} ! ')