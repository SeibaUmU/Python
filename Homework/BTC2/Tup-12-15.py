def bt12():
    #Hiển thị màn hình hướng dẫn nhập liệu search thông qua nhập tên học sinh. Ví dụ nhập Nguyễn Văn A thì nghĩa là hiển thị xuất ra tên và điểm trung bình môn học.
    name = str(input("Nhap ten hs can tim: "))
    for x, y in sv.items():
        if x == name:
            print(f"Ten hs: {x}, Diem: {y}")
    #Sau đó thay đổi giá trị môn Toán của HS Nguyễn Văn A là 8.0
    for x, y in sv.items():
        if x == name:
            d = list(y)
            d[1] = 8.0
            y = tuple(d)
            print(f"Ten hs: {x}, Diem: {y}")
def bt13():
    fruit = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    price = ('10.000', '20.000', '30.000', '40.000', '50.000', '60.000', '70.000')
    for x in range(2, 6):
        print(f"Trai cay: {fruit[x]}, Gia tien: {price[x]}")

sv = {
    "Nguyen Van A": ("Toan", 7.4, "Ly", 6.5, "Hoa", 7.0)
}

def bt14():
    Tuple1 = ("apple", "banana", "cherry")
    Tuple2 = ("kiwi", "melon", "mango")
    Tuple3 = tuple(Tuple1 + Tuple2)
    print(Tuple3)

def bt15():
    fruit = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "grapes", "dragon", "lemon")
    price = ('10.000', '20.000', '30.000', '40.000', '50.000', '60.000', '70.000', "80.000", "90.000", "100.000")
    while True:
        chon = int(input("Ban muon search 1 loai trai (1) hay toan bo(2) hay update gia(3)? (Nhan 4 de thoat)"))
        if chon == 1:
            name = str(input("Ten trai: "))
            for x in range(len(fruit)):
                if fruit[x] == name:
                    print(f"Ten trai: {fruit[x]}, Gia tien: {price[x]}")
        elif chon == 2:
            for x in range(len(fruit)):
                print(f"Ten trai: {fruit[x]}, Gia tien: {price[x]}")
        elif chon == 4:
            break
        elif chon == 3:
            change = list(str(input("Nhap 5 loai qua muon cap nhat: ")).split())
            changeprice = list(str(input("Nhap gia tien lan luot 5 qua muon cap nhat: ")).split())
            for x in range(len(change)):
                for i in range(len(fruit)):             
                    if change[x] == fruit[i]:
                        y = list(price)
                        y[i] = changeprice[x]
                        price = tuple(y)  
        else:
            print("DMM bi mu ha? pick 1 2 hay 3 4th!")
                    
choice = int(input("BT so: "))
match choice:
    case 12:
        bt12()
    case 13:
        bt13()
    case 14:
        bt14()
    case 15:
        bt15()
    case _:
        print("dumb")


