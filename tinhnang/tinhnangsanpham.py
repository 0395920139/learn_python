from .sanpham.taohanghoa import xem_hanghoa 
from .sanpham.taoloaihanghoa import tao_loaihanghoa,xem_loaihanghoa
from .hoadon.taohoadon import tao_hoadon,in_hoadon
from .khachhang.info_custumer import thong_tin_khachhang
from .doanhthu.tongtien import tong_tien_theo_ngay
from .doanhthu.doanhthusp import tong_sp
def menu():
    while True:
        print("+-----------------------------MENU-----------------------------+")
        print("|Chon THH | de xem hang hoa                                      |")
        print("|Chon TLH | de Tao loai hang hoa                                 |")
        print("|Chon XLH | de Xem loai hang hoa                                 |")
        print("|Chon C   | de tao hoa don                                       |")
        print("|Chon R   | de xem thong tin hoa don                             |")
        print("|Chon TT  | de xem thong tin khach hang                          |")
        print("|Chon T   | de tinh doanh thu theo ngay                          |")
        print("|chon G   | de xem so sp da ban dc                               |")
        print('|                 an bat ki 1 phim de ket thuc                   |')
        print("+----------------------------------------------------------------+")
        chon = input('moi ban chon chuc nang')
        if chon.upper() == 'THH':
            ma_hang_hoa = input('nhap ma hang hoa')
            print(xem_hanghoa(ma_hang_hoa))
        elif chon.upper() == 'TLH':
            tao_loaihanghoa()
        elif chon.upper() == 'XLH':
            ma_loai_hang_hoa = input('nhap ma loai hang hoa')
            print(xem_loaihanghoa(ma_loai_hang_hoa))
        elif chon.upper() == 'C':
            tao_hoadon()
        elif chon.upper() == 'R':
            in_hoadon()
        elif chon.upper() == 'TT':
            thong_tin_khachhang()
        elif chon.upper() == 'T':
            tong_tien_theo_ngay()
        elif chon.upper() == 'G':
            tong_sp()
        else : 
            return



    
        

    



