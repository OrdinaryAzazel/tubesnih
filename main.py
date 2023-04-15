import csv
import os
import sys

users=[None for i in range(3)]
with open('user.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    i = 0
    for row in reader :
            
            users[i]=row
            i+=1

print(users)
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
                    loginstatus = True
                    return loginstatus

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
    while keluar != "n" or keluar != 'y' or keluar != 'N' or keluar != 'Y':
        keluar = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)')
    if keluar == 'n' or keluar == 'N':
        quit()

    else :
        quit()
        #fungsi f04 and exit
exit()