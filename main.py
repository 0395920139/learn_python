#phần đầu chương trinhg
from tinhnang.user.dangnhap import dang_nhap
from tinhnang.user.taotaikhoan import tao_taikhoan
from tinhnang.user.quenmatkhau import quen_matkhau
while True:
    print('                    chao mung den voi app quan ly ban hang                 ')
    print('                              1, Dang nhap                                 ')
    print('                              2, Tao tai khoan                             ')
    print('                              3, quen mat khau                             ')
    print('                         an bat ki 1 phim de ket thuc                      ')
    chon = input('ban cui long chon cac chuc nang')
    if chon == '1':
        dang_nhap()
    elif chon == '2':
        print('xin moi ban tao tai khoan')
        tao_taikhoan()
    elif chon == '3':
        quen_matkhau()
    else :
        break