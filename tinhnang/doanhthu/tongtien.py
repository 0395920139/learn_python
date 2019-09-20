def xem_tongtien(date):
    tong_tien = read_file_tongtien_khoidong()
    for tien in tong_tien:
        if tien["ngay hoa don"] == date:
            return tong_tien
def read_file_tongtien_khoidong():
    tong_tien = []
    with open("tinhnang/doanhthu/tien_theo_ngay.csv ", 'r') as f:
        line = f.readline()
        while line:    
            line = f.readline()
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1 :
                tien = {}
                tien['ngay hoa don'] = str_to_reads[0]
                xoa = str_to_reads[1]
                if xoa.endswith('\n'):
                    xoa = xoa[0:len(xoa)-1]
                    tien['tong tien'] = xoa
                tong_tien.append(tien)
    return tong_tien
def tong_tien_theo_ngay():
    tong_tien = read_file_tongtien_khoidong()
    while True:
        date = input(' nhap ngay kiem tra')
        kt = xem_tongtien(date)
        if  kt == None:
            print('ngay khong co hoa don hoac khong ton tai ban vui long nhap lai')
        else :
            total = 0
            for tien in tong_tien:
                if tien['ngay hoa don'] == date :
                    tien_int = int(tien['tong tien']) 
                    total = total + tien_int
            print('tong tien la',total)
            break
                 
