# main.py
import infoSV
choice = int(input("BT so: "))
match choice:
    case 1:
        name = infoSV.ten()
        student_id = infoSV.mssv()

        print("\n--- Thông tin sinh viên ---")
        print("Tên sinh viên:", name)
        print("MSSV:", student_id)
    case 2:
        ds_sv = []
        n = int(input("Bạn muốn nhập bao nhiêu sinh viên? "))
        # Nhập thông tin cho n sinh viên
        for i in range(n):
            print(f"\n>>> Nhập thông tin sinh viên {i+1}:")
            sv = infoSV.nhapinfo()
            ds_sv.append(sv)
        infoSV.xuatinfo(ds_sv)
    case 3:
        sv_12A = infoSV.lop12A()
        sv_12B = infoSV.lop12B()
        lopLapTrinhMang = sv_12A + sv_12B
        print("===Danh sach sv lop LTM\n")
        infoSV.xuatinfo(lopLapTrinhMang)

    case 4:
        infoSV.baitoan1()
    case 5:
        infoSV.baitoan2()
    case 6:
        infoSV.sxtu()
    case 7:
        infoSV.inhoa()
    case 8:
        infoSV.loaitu()
    case 9:
        infoSV.binary()
    case 10:
        infoSV.findso()
    case _:
        print("dumb")