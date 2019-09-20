import json
import os.path
from os import path

def tao_taikhoan():
    user = {}
    while True:
        user['tai khoan'] = input('vui long nhap ten dang nhap:')
        kt = kiem_tra_taikhoan(user['tai khoan'])
        if kt == False:
            user['mat khau'] = input('vui long nhap mat khau:')
            user['ten nguoi dung'] = input('vui long nhap ho va ten:')
            user['ngay sinh'] = input('vui long nhap ngay sinh:')
            user['gmail'] = input('vui long nhap gmail:')
            with open('tinhnang/user/quanlyuser/'+ user['tai khoan'] +'.json', 'w') as outlile:
                json.dump(user,outlile)
        print('tai khoan da co san vui long nhap lai')
def kiem_tra_taikhoan(nguoidung):
    path.exists('tinhnang/user/quanlyuser/' + nguoidung + '.json')
    kt = path.exists('tinhnang/user/quanlyuser/' + nguoidung + '.json')
    return kt

def reads_file(nguoidung):
    data = None
    with open('tinhnang/user/quanlyuser/'+ nguoidung + '.json', 'r') as infile:
        data = json.load(infile)
    return data