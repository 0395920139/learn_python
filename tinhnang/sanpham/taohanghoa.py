#tạo hàng hóa
def xem_hanghoa(id):
    danhsachhanghoa = read_file_hanghoa_khoidong()
    for hanghoa in danhsachhanghoa:
        if hanghoa["ma hang hoa"] == id:
            return hanghoa
def tao_hanghoa():
    while True:
        id = input('nhap ma hang hoa')
        kt = xem_hanghoa(id)
        if kt == None:
            data = {}
            data['ma hang hoa'] = id
            data['ten hang hoa'] = input('nhap ten hang hoa')
            data['don gia'] = input('nhap don gia')
            data['ma loai hang hoa'] = input('nhap ma loai hang hoa')
            str_to_save = data['ma hang hoa'] + '#' + data['ten hang hoa'] + '#' + data['don gia'] + '#' + data['ma loai hang hoa'] + '\n'
            with open('tinhnang/sanpham/hanghoa.csv', 'a') as f:
                f.write(str_to_save)
            break
        else :
            print('ban vui long nhap lai')
# read file csv 
def read_file_hanghoa_khoidong():
    danhsachhanghoa = []
    with open('tinhnang/sanpham/hanghoa.csv', 'r') as f:
        line = f.readline()
        while line:    
            line = f.readline()
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1 :
                hanghoa = {}
                hanghoa['ma hang hoa'] = str_to_reads[0]
                hanghoa['ten hang hoa'] = str_to_reads[1]
                hanghoa['don gia'] = str_to_reads[2]
                xoa = str_to_reads[3]
                if xoa.endswith('\n'):
                    xoa = xoa[0:len(xoa)-1]
                    hanghoa['ma loai hang hoa'] = xoa
                danhsachhanghoa.append(hanghoa)
    return danhsachhanghoa