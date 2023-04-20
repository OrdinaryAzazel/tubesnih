
import command

while True:
    masukan = input('>>> ')
    if masukan =='login':
        command.login()
    elif masukan == 'logout':
        command.logout()
    elif masukan == 'summonjin':
        command.summonjin()
    elif masukan == 'ubahjin':
        command.ubahjin()
    elif masukan =='bangun':
        command.bangun()
    elif masukan =='hapusjin':
        command.hapusjin()
    elif masukan == 'kumpul':
        command.kumpul()
    elif masukan == 'batchkumpul':
        command.batchkumpul()
    elif masukan == 'help':
        command.help()
    elif masukan == 'laporanjin':
        command.laporanjin()
    elif masukan == 'laporancandi':
        command.laporancandi()
    elif masukan == 'hancurkancandi':
        command.hancurkancandi()
    elif masukan == 'ayamberkokok':
        command.ayamberkokok()
    elif masukan =='save':
        command.save()
    elif masukan == 'exit':
        command.exit()
    elif masukan=='batchbangun':
        command.batchbangun()
    elif masukan =='':
        continue
    else :
        print(f'{masukan} tidak ada di command list.')
  

    