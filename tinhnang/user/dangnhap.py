from .taotaikhoan import reads_file,kiem_tra_taikhoan
from tinhnang.tinhnangsanpham import menu
def dang_nhap():
    while True:
        taikhoan = input('nhap tai khoan')
        kiem_tra = kiem_tra_taikhoan(taikhoan)
        if kiem_tra == True:
            user = reads_file(taikhoan)
            if user['tai khoan'] == taikhoan:
                while True:
                    pass_user = input('nhap mat khau')
                    if user['mat khau'] == pass_user:
                        menu()
                    print('mat khau khong dung vui long nhap lai')
        print('ban da nhap sai vui long nhap lai')