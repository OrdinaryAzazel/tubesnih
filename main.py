import csv

users=[None for i in range(3)]
with open('user.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter=';')
    i = 0
    for row in reader :
            
            users[i]=row
            i+=1

print(users)
# def check():
Bandung = False
Roro = True

def login(users):
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
                         
                         return
                    break
            elif i == (3-1):
                 print('Username tidak terdaftar!')
                 
login(users)