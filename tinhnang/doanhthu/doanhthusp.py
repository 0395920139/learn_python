
def read_file_sanpham_khoidong():
    san_pham = []
    with open("tinhnang/doanhthu/total_sanpham.csv ", 'r') as f:
        line = f.readline()
        while line:    
            line = f.readline()
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1 :
                ban = {}
                ban['ten hang hoa'] = str_to_reads[0]
                xoa = str_to_reads[1]
                if xoa.endswith('\n'):
                    xoa = xoa[0:len(xoa)-1]
                    ban['so luong'] = xoa
                san_pham.append(ban)
        return san_pham
def xem_sp(id):
    xem = read_file_sanpham_khoidong()
    for kt in xem:
        if kt['ten hang hoa'] == id:
            return xem
def tong_sp():
    tong_sp = read_file_sanpham_khoidong()
    while True:
        ten = input('nhap ten san pham')
        kt = xem_sp(ten)
        if kt == None:
            print('ban da nhap sai vui long nhap lai')
        else :
            total = 0
            for tim_kiem in tong_sp:
                if tim_kiem['ten hang hoa'] == ten:
                    int_tong = int(tim_kiem['so luong'])
                    total = total + int_tong
            print('tong sp ',ten,'ban dc la',total)