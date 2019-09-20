import json
import os.path
from os import path
def tao_hoadon():
    #phần tạo hóa đơn
    print('moi ban tao hoa don')
    #phần nhập thông tin người mua,hóa đơn
    hoadon = {}
    khachhang = {}
    while True:
        hoadon['so hoa don'] = input("nhap so hoa don:")
        kt = kiem_tra_hoadon(hoadon['so hoa don'])
        if kt==True:
            print('ban vui long nhap lai')
            pass
        else :
            hoadon['ngay hoa don'] = input('nhap ngay hoa don')
            hoadon['nguoi mua'] = input('nhap ho ten nguoi mua')
            hoadon['tong tien truoc thue'] = 0
            hoadon['thue'] = 0.1
            hoadon['tong tien'] = 0
            hoadon['danh sach hoa don'] = []
            #phần nhập thông tin người mua,hóa đơn1
            nhaphanghoa = input('ban co muon nhap hang hoa khong (y/n)')
            stt = 1 
            khachhang['thong tin mua hang'] = []
            while nhaphanghoa.upper() == 'Y':
                #phần nhập thông tin hàng hóa bán
                hanghoa = {}
                muahang = {}
                hanghoa['stt'] = stt
                stt += 1
                hanghoa['ten hang hoa'] = input('nhap ten hang hoa')
                muahang['ten hang hoa'] = hanghoa['ten hang hoa']
                hanghoa['so luong'] = input('nhap so luong')
                muahang['so luong'] = hanghoa['so luong']
                so_luong = int(hanghoa['so luong'])

                hanghoa['don gia'] = input('nhap don gia')
                khachhang['thong tin mua hang'].append(muahang)
                don_gia = int(hanghoa['don gia'])
                thanh_tien = so_luong*don_gia
                str_thanh_tien = str(thanh_tien)

                hanghoa['thanh tien'] = str_thanh_tien
                hoadon['danh sach hoa don'].append(hanghoa)
                hoadon['tong tien truoc thue'] = hoadon['tong tien truoc thue'] + thanh_tien
                hoadon['tong tien'] = hoadon['tong tien truoc thue']*hoadon['thue']

                str_to_save_total = hanghoa['ten hang hoa'] + '#' + hanghoa['so luong'] + '\n'
                with open('tinhnang/doanhthu/total_sanpham.csv', 'a') as f:
                    f.write(str_to_save_total)

                nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
            with open( "tinhnang/hoadon/luuhoadon/" + hoadon['so hoa don'] + '.json', 'w') as outfile:
                json.dump(hoadon,outfile)

            str_tong_tien = hoadon['tong tien']
            str_tien = hoadon['ngay hoa don'] + '#' + str_tong_tien + '\n'
            with open('tinhnang/doanhthu/tien_theo_ngay.csv', 'a') as f:
                f.write(str_tien)

            khachhang['so hoa don'] = hoadon['so hoa don']
            khachhang['ngay hoa don'] = hoadon['ngay hoa don']
            khachhang['nguoi mua'] = hoadon['nguoi mua']
            khachhang['tong tien'] = hoadon['tong tien']
            str_tongtien =str(khachhang['tong tien'])
            # xoa 
            print(type(str_tongtien))
            print(type(khachhang['nguoi mua']))
            print(type(khachhang['ngay hoa don']))
            print(type(khachhang['so hoa don']))
            #xoa
            str_to_save = khachhang['so hoa don'] + '#' + khachhang['ngay hoa don'] + '#' + khachhang['nguoi mua'] + '#' + str_tongtien + '\n'
            with open ("tinhnang/khachhang/infor_custumer.csv ", 'a') as f:
                f.write(str_to_save)
            break
        
def in_hoadon():
    while True:
        sohoadon = input('nhap so hoa don')
        kt = kiem_tra_hoadon(sohoadon)
        if kt == False:
            print('ban vui long nhap lai')
            pass
        else :
            hoadon = reads_file(sohoadon)
            # Hoa don se in o day
            print("                          HOA DON MUA HANG                                  ")
            print("so hoa don:", hoadon["so hoa don"])
            print("ngay xuat:", hoadon["ngay hoa don"])
            print("ten khach hang:", hoadon["nguoi mua"])
            print("_____________________________thong tin hoa don_______________________________")
            print("+----------+------------------+----------+---------------+------------------+")
            print("|   STT    |     hang hoa     | so luong |    don gia    |    thanh tien    |")
            print("+----------+------------------+----------+---------------+------------------+")
            for hanghoa in hoadon["danh sach hoa don"]:
                #kiem tra dag sai
                print(type(hanghoa['stt']))
                print(type(hanghoa['ten hang hoa']))
                print(type(hanghoa['so luong']))
                print(type(hanghoa['don gia']))
                print(type(hanghoa['thanh tien']))
                #kiem tra dang sai
                print("| ", hanghoa['stt'] ,"  | " + hanghoa['ten hang hoa'] + " | "+ hanghoa['so luong'] +" | "+ hanghoa['don gia'] +" | "+ hanghoa['thanh tien'] +" |")
                print("+----------+------------------+----------+---------------+------------------+")
                print("|                                 tong tien truoc thue   +",  hoadon['tong tien truoc thue'] , "|")
                print("+----------+------------------+----------+---------------+------------------+")
                print("|                                 thue                   +", hoadon['thue'] , "|")
                print("+----------+------------------+----------+---------------+------------------+")
                print("|                                 tong tien              +" ,  hoadon['tong tien'] ,"|")
        break
def kiem_tra_hoadon(sohoadon):
    path.exists("tinhnang/hoadon/luuhoadon/" + sohoadon + '.json')
    a = path.exists("tinhnang/hoadon/luuhoadon/" + sohoadon + '.json')
    return a
def reads_file(sohoadon):
    data = None
    with open("tinhnang/hoadon/luuhoadon/" + sohoadon + '.json', 'r') as infile:
        data = json.load(infile)
    return data