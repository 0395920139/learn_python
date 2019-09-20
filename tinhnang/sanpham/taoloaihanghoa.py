#tạo loại sản phẩn
import os
def xem_loaihanghoa(id):
    danhsachloaihanghoa = read_file_loaihanghoa_khoidong()
    for loaihanghoa in danhsachloaihanghoa:
        if loaihanghoa["ma loai hang hoa"] == id:
            return loaihanghoa
def tao_loaihanghoa():
    while True:
        id = input('nhap ma loai hang hoa:')
        kt = xem_loaihanghoa(id)
        if kt == None:
            data = {}
            data['ma loai hang hoa'] = id 
            data['ten loai hang hoa'] = input('nhap ten loai hang hoa')
            str_to_save = data['ma loai hang hoa'] + '#' + data['ten loai hang hoa'] + '\n'
            with open('tinhnang/sanpham/LOAIHANGHOA.csv', 'a') as f:    
                f.write(str_to_save)
            break
        else :
            print('ban vui long nhap lai')
def read_file_loaihanghoa_khoidong():
    danhsachloaihanghoa = []
    with open('tinhnang/sanpham/LOAIHANGHOA.csv', 'r') as f:
        line = f.readline()
        while line:    
            line = f.readline()
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1 :
                loaihanghoa = {}
                loaihanghoa['ma loai hang hoa'] = str_to_reads[0]
                xoa = str_to_reads[1]
                if xoa.endswith('\n'):
                    xoa = xoa[0:len(xoa)-1]
                    loaihanghoa['ten loai hang hoa'] = xoa
                danhsachloaihanghoa.append(loaihanghoa)
    return danhsachloaihanghoa
            
