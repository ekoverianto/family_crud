from turtle import clear
from Keluarga import Keluarga
import mysql.connector
import os

db = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'orang'
)

# if db.is_connected():
#     print('Berhasil Terhubung')
# else:
#     print('Gagal Terhubung')

def tampilData():
    Keluarga().readData(db)

def tambahData():
    _nama = input('Masukan Nama: ')
    _jenis_kelamin = input('Masukan Jenis Kelamin: ')
    Keluarga().readData(db)
    _id_parent = int(input('Masukan ID Parent (Cek id parent di atas): '))
    Keluarga(_nama, _jenis_kelamin, _id_parent).createData(db)

def ubahData():
    Keluarga().readData(db)
    _id = int(input('Masukan id data yang akan diubah (Cek id di atas): '))
    _nama = input('Masukan Nama (Baru): ')
    _jenis_kelamin = input('Masukan Jenis Kelamin (Baru): ')
    _id_parent = int(input('Masukan ID Parent (Baru): '))
    Keluarga(_nama, _jenis_kelamin, _id_parent).updateData(db, _id)

def hapusData():
    Keluarga().readData(db)
    _id = int(input('Masukan id data yang akan dihapus (Cek id di atas): '))
    Keluarga().deleteData(db, _id)

def navigasi():
    print('==================')
    print('Pilih Menu:')
    print('1. Tampil Data')
    print('2. Tambah Data')
    print('3. Ubah Data')
    print('4. Hapus Data')
    print('5. Keluar Aplikasi')
    print('==================')

    menu = int(input('Masukan Menu: '))

    os.system('clear')

    if menu == 1:
        tampilData()
    elif menu == 2:
        tambahData()
    elif menu == 3:
        ubahData()
    elif menu == 4:
        hapusData()
    elif menu == 5:
        exit()
    else:
        print('Navigasi tidak ditemukan')

if __name__ == "__main__":
    while(True):
        navigasi()