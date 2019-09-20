#quen mat khau
from .taotaikhoan import *
def quen_matkhau():
    while True:
        taikhoan = input('vui long nhap tai khoan')
        kiem_tra = kiem_tra_taikhoan(taikhoan)
        if kiem_tra == True:
            user = reads_file(taikhoan)
            while True:
                ten_nguoi_dung = input('nhap ten da dang ky:')
                if user['ten nguoi dung'] == ten_nguoi_dung:
                    while True:
                        ngay_sinh = input('nhap ngay sinh da dang ky :')
                        if user['ngay sinh'] == ngay_sinh:
                            while True:
                                gmail = input('nhap gmail da dang ky :')
                                if user['gmail'] == gmail:
                                    print('heloo'+ user['ten nguoi dung'])
                                    print('mat khau cua ban la :' + user['mat khau'])
                                    break
                                print('ban da nhap sai gmail dang ky vui long nhap lai')
                            break
                        print('ban da nhap sai ngay sinh dang ky vui long nhap lai')
                    break
                print('ban da nhap sai ten dang ky vui long nhap lai')
            break
        print('tai khoan khong ton tai ban vui long nhap lai tai khoan')

                