def bt1():
    height = 4
    triangle = []
    for i in range(1, height + 1):
        line = '*' * i
        triangle.append(line)
    # In ra tam giác
    for row in triangle:
        print(row)

def bt2(name):
    for i in range(len(ten)):
        if name == ten[i]:
            print(f"Toan: {toan[i]}, Ly: {ly[i]}, Hoa: {hoa[i]}")
            print(f"DTB: {(float(toan[i])+float(ly[i])+float(hoa[i]))/3}")
        

def bt3(a):
    for i in range(len(fruit)):
        for j in range(len(a)):
            if a[j] == fruit[i]:
                print(f"Ten: {fruit[i]}, Gia tien'kg: {price[i]}")
                
def nhapdl():
    print("Nhập dữ liệu sinh viên (mỗi dòng: mssv hoten ngaysinh lop 5 điểm kết quả). Gõ 'x' để kết thúc")

    while True:
        line = input(">> ").strip() #bo enter
        if line.lower() == 'x' or line == '':
            break

        parts = line.split() #phan biet bang space
        # Tìm vị trí ngày sinh (dựa vào dấu '/')
        birth_index = None
        for i in range(len(parts)):
            if '/' in parts[i]:
                birth_index = i
                break

        if birth_index is None or len(parts) < birth_index + 7:
            print("Du lieu ko hop le or thieu, nhap lai.")
            continue

        mssv.append(parts[0])
        tensv.append(' '.join(parts[1:birth_index]))
        birth.append(parts[birth_index])
        lop.append(parts[birth_index + 1])
        diem_sv = [float(x) for x in parts[birth_index + 2 : birth_index + 8]] + [parts[birth_index + 8]]
        diem.append(diem_sv)

    return mssv, tensv, birth, lop, diem
ten = ["Nguyen Van A", "Tran Van B", "Cao Quoc C"]
toan = ["7.4", "6.5", "7.0"]
ly = ["2.0", "7.2", "6.5"]
hoa = ["3.6", "5.4", "9.5"]
fruit = ["apple", "mango", "kiwi", "watermelon", "cherry"]
price = ["10.000", "20.000", "15.000", "30.000", "40.000"]
mssv = []
tensv = []
birth = []
lop = []
diem = [[None for _ in range(8)] for _ in range(len(mssv))]
sv = [mssv, tensv, birth, lop, diem]

choice = int(input("BT so: "))

match choice:
    case 1:
        bt1()

    case 2:
        name = input("Nhap ten hoc sinh: ")
        bt2(name)

    case 3:
        fruitname = input("Trai cay: ").split()
        bt3(fruitname)

    case 4:
        name = input("Nhap ten hoc sinh: ")
        if name in ten:
            bt2(name)
        else:
            print("Hoc sinh ko ton tai")

    case 5:
        fruit.pop()
        price.pop()

        fruit[2:2] = ["strawberry", "banana"]
        price[2:2] = ["3.000", "6.000"]

        print(fruit)
        print(price)
    case 6:
        while True:
            wow = input("Ban muon nhap hay xem hay nhap lai (nhan x de dung)?   ")
            if wow == 'x':
                break
            elif wow == "xem":
                so_sv = len(sv[0])
                for i in range(so_sv):
                    print(f"--- Sinh viên {i+1} ---")
                    print(f"MSSV: {sv[0][i]}")
                    print(f"Họ tên: {sv[1][i]}")
                    print(f"Ngày sinh: {sv[2][i]}")
                    print(f"Lớp: {sv[3][i]}")
                    print(f"Điểm: {sv[4][i][:6]}")
                    print(f"Kết quả: {sv[4][i][6]}")
                    print()
            elif wow == "nhap":
                nhapdl()
            elif wow == "nhap lai":
                for lst in sv:
                    lst.clear()
            else: 
                print("ko hop le, hay nhap lai")
                

    case _:
        print("Lua chon khong hop le")







