# infoSV.py
import math
def ten():
    name = input("Nhập tên sinh viên: ")
    return name

def mssv():
    id_sv = input("Nhập MSSV: ")
    return id_sv

def nhapinfo():
    sv= {}
    sv["STT"] = input("STT: ")
    sv["HoTen"] = input("HoTen: ")
    sv["MSSV"] = input("MSSV: ")
    sv["Birth"] = input("Birth (dd/mm/yyy): ")
    sv["Que"] = input("Que: ")
    sv["Lop"] = input("Lop: ")
    return sv
def xuatinfo(a):
    for i, sv in enumerate(a, start=1):
        print(f"--------------------")
        for key, value in sv.items():
            print(f"{key}: {value}")

def lop12A():
    lop12A = [
        {"Tên": "Nguyễn Văn A", "MSSV": "12A001", "Ngày sinh": "01/01/2006", "Quê quán": "Hà Nội"},
        {"Tên": "Trần Thị B", "MSSV": "12A002", "Ngày sinh": "15/02/2006", "Quê quán": "Hải Phòng"},
        {"Tên": "Lê Văn C", "MSSV": "12A003", "Ngày sinh": "20/03/2006", "Quê quán": "Nam Định"},
        {"Tên": "Phạm Thị D", "MSSV": "12A004", "Ngày sinh": "05/04/2006", "Quê quán": "Thanh Hóa"},
        {"Tên": "Hoàng Văn E", "MSSV": "12A005", "Ngày sinh": "10/05/2006", "Quê quán": "Nghệ An"},
    ]
    return lop12A
def lop12B():

    lop12B = [
        {"Tên": "Nguyễn Văn F", "MSSV": "12B001", "Ngày sinh": "02/06/2006", "Quê quán": "Đà Nẵng"},
        {"Tên": "Trần Thị G", "MSSV": "12B002", "Ngày sinh": "12/07/2006", "Quê quán": "Huế"},
        {"Tên": "Lê Văn H", "MSSV": "12B003", "Ngày sinh": "22/08/2006", "Quê quán": "Quảng Nam"},
        {"Tên": "Phạm Thị I", "MSSV": "12B004", "Ngày sinh": "30/09/2006", "Quê quán": "Quảng Ngãi"},
        {"Tên": "Hoàng Văn K", "MSSV": "12B005", "Ngày sinh": "11/10/2006", "Quê quán": "Bình Định"},
    ]
    return lop12B
def baitoan1():
    C, H = 50, 30
    values = input("D = ")
    D = values.split(",")

    Q = []
    for x in D:
        Q_tinh = round(math.sqrt((2 * C * int(x)) / H))
        Q.append(Q_tinh)
    print(Q)
def baitoan2():
    X, Y = map(int, input("Nhập X, Y (cách nhau bằng dấu cách): ").split())
    list2chieu = [[None for _ in range(Y)] for _ in range(X)]
    for x in range(X):
        for y in range(Y):
            list2chieu[x][y] = x*y 
    print(list2chieu)
def sxtu():
    value = input("Nhap cac tu (phan tach = dau ,): ")
    arr = value.split(",")
    arr.sort()
    print(arr)
def inhoa():
    chuoi = str(input("Nhap chuoi: "))
    print(chuoi.upper())
def loaitu():
    chuoi = input("Nhập chuỗi: ")
    tu_list = chuoi.split()
    tu_khong_trung = set(tu_list)
    tu_sap_xep = sorted(tu_khong_trung)
    ket_qua = " ".join(tu_sap_xep)
    print("Kết quả:", ket_qua)
def binary():
    binary_input = input("Nhập dãy số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")
    binary_list = binary_input.split(",")
    result = []
    for b in binary_list:
        if int(b, 2) % 5 == 0:  # chuyển sang thập phân và kiểm tra chia hết 5
            result.append(b)
    print(",".join(result))
def findso():
    result = []
    for num in range(1000, 3001):  
        s = str(num)
        if all(int(ch) % 2 == 0 for ch in s):  # kiểm tra tất cả chữ số đều chẵn
            result.append(s)

    print(",".join(result))









