import csv
def thong_tin_khachhang():
    while True:
        khachhang = input('nhap ten khach hang')
        kt = xem_khachhang(khachhang)
        if kt == None:
            print('khach hang khong ton tai vui long nhap lai')
            pass
        else :
            data = {}
            data['so hoa don'] = []
            tien = 0
            danhsachkhachhang = read_file_khachhang_khoidong()
            for thongtin in danhsachkhachhang:
                if thongtin['nguoi mua'] == khachhang:
                    data['ten khach hang'] = thongtin['nguoi mua']
                    if thongtin['so hoa don'] in data['so hoa don']:
                        pass
                    else :
                        data['so hoa don'].append(thongtin['so hoa don'])
                    str_tongtien = float(thongtin['tong tien'])
                    tien = tien + str_tongtien
            data['tien da mua'] = tien
            return data
            #khachhang['so hoa don'] + '#' + khachhang['ngay hoa don'] + '#' + khachhang['nguoi mua'] + '#' + str_tongtien
            #khachhang['so hoa don'] = hoadon['so hoa don']
            #khachhang['ngay hoa don'] = hoadon['ngay hoa don']
            #khachhang['nguoi mua'] = hoadon['nguoi mua']
            #khachhang['tong tien'] = hoadon['tong tien']
def xem_khachhang(id):
    danhsachkhachhang = read_file_khachhang_khoidong()
    for khachhang in danhsachkhachhang:
        if khachhang["nguoi mua"] == id:
            return danhsachkhachhang
def read_file_khachhang_khoidong():
    danhsachkhachhang = []
    with open("tinhnang/khachhang/infor_custumer.csv ", 'r') as f:
        line = f.readline()
        while line:    
            line = f.readline()
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1 :
                khachhang = {}
                khachhang['so hoa don'] =str_to_reads[0]
                khachhang['ngay hoa don'] = str_to_reads[1]
                khachhang['nguoi mua'] = str_to_reads[2]
                xoa = str_to_reads[3]
                if xoa.endswith('\n'):
                    xoa = xoa[0:len(xoa)-1]
                    khachhang['tong tien'] = xoa
                danhsachkhachhang.append(khachhang)
    return danhsachkhachhang
