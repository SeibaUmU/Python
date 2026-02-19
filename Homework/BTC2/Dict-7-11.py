def bt7():
    x = sv["Sở Thích"]
    print(f"Sở thích: {x}")
    sv["Sở Thích"] = "Game"
    x = sv["Sở Thích"]
    print(f"Sở thích: {x}")

def bt8():
    for x in sv: #In  ra tất cả key name
        print(x)
    x = sv["Date"] #Dùng key name đã in ra để truy xuất 1 giá trị nào đó
    print(x)    
    for x in sv: #In  ra tất cả giá trị theo key name đó.
        print(sv[x])
    for x, y in sv.items(): #In ra tất cả key name và giá trị đồng thời
        print(x, y)

def bt9():
    #+ Kiểm tra và in ra số lượng thành phần trong Dictionry
    print(len(sv))
    #+ Thêm vào Ngoại ngữ và Dân Tộc, và in ra kết quả tất cả thành phần trong Dictionary
    sv.update({
    "Ngoại ngữ": "Anh",
    "Dân tộc": "Kinh"
    })
    print(sv)
    #+ Xoá key name và giá trị “sở thích” và sau đó in ra tất cả thành phần lại lần nữa.
    sv.pop("Sở Thích")
    print(sv)

def bt10():
    #+ Nest lại 3 dict của 3 sinh viên trên thành một dict mới tên Lop DHDT12B.
    DHDT12B = { 
        "sv1": sv1,
        "sv2": sv2,
        "sv3": sv3
    }
    print(DHDT12B)
    #+ In ra key name tất cả thành phần trong dict Lop DHDT12B
    for sv_key, sv_info in DHDT12B.items():
        print(f"Các key của {sv_key}:")
        for key in sv_info.keys():
            print(f" - {key}")
    #+ Search và xuất ra bộ dữ liệu dict của sinh viên thứ 2
    print(DHDT12B["sv2"])
    #+Copy dict Lop DHDT12B và tạo ra dict mới là tên môn học ANHVAN01
    ANHVAN01 = DHDT12B.copy()
    #+ Thêm 2 dict của 2 sinh viên Lop DHDT12A vào Lop ANHVAN01.
    svA1 = {
    "Tên": "Phạm Minh D",
    "MSSV": 4,
    "Lop": "DHDT12A" }
    svA2 = {
    "Tên": "Hoàng Lan E",
    "MSSV": 5,
    "Lop": "DHDT12A" }
    ANHVAN01.update( {
        "sv4" : svA1,
        "sv5" : svA2
    })
    print(ANHVAN01)
    

def bt105():
    #+ Nest lại 3 dict của 3 sinh viên trên thành một dict mới tên Lop DHDT12B.
    DHDT12B = { 
        "sv1": sv1,
        "sv2": sv2,
        "sv3": sv3
    }
    
    #+ Search và xuất ra bộ dữ liệu dict của sinh viên thứ 2
    
    #+Copy dict Lop DHDT12B và tạo ra dict mới là tên môn học ANHVAN01
    ANHVAN01 = DHDT12B.copy()
    #+ Thêm 2 dict của 2 sinh viên Lop DHDT12A vào Lop ANHVAN01.
    svA1 = {
    "Tên": "Phạm Minh D",
    "MSSV": 4,
    "Lop": "DHDT12A" }
    svA2 = {
    "Tên": "Hoàng Lan E",
    "MSSV": 5,
    "Lop": "DHDT12A" }
    ANHVAN01.update( {
        "sv4" : svA1,
        "sv5" : svA2
    })
    
    return DHDT12B, ANHVAN01

def bt11():
    #+ Thêm vào 2 sinh viên cho Lop DHDT12B thành tổng 5 sinh viên.
    sv4 = {"Ten": "Trong", "MSSV":4, "Lop": "DHDT13b"}
    sv5 = {"Ten": "Tai", "MSSV":5, "Lop": "DHDT14b"}
    DHDT12B.update({
        "sv4":sv4,
        "sv5":sv5
    })
    #+ Thêm vào Lop ANHVAN01 hai sinh viên mới Lop DHDT12B
    sv6 = {"Tên": "Nguyễn Văn F", "MSSV": "DH006", "Lop": "DHDT12A"}
    sv7 = {"Tên": "Trần Thị G", "MSSV": "DH007", "Lop": "DHDT12A"}
    ANHVAN01["sv6"] = sv6
    ANHVAN01["sv7"] = sv7
    #+ Chỉnh sửa toàn bộ dict DHDT12B, Lop ANHVAN01 và 2 sinh viên Lop DHDT12A bằng cách thêm thành phần quê quán, trình độ anh văn điểm Toiec hiện tại, tình trạng học phí.
    for lop in [DHDT12B, ANHVAN01]:
        for sv in lop.values():
            sv["Quê quán"] = "TP.HCM"
            sv["TOEIC"] = 450
            sv["Học phí"] = "Đã đóng"
    print(ANHVAN01)
    #+ Xoá 1 sinh viên Lop DHDT12A do chưa đóng học phí khỏi Lop ANHVAN01
    ANHVAN01["sv7"]["Học phí"] = "Chưa đóng"
    for key, sv in list(ANHVAN01.items()):
        if sv["Lop"] == "DHDT12A" and sv["Học phí"] == "Chưa đóng":
            del ANHVAN01[key]
    print(DHDT12B)
    print(ANHVAN01)


sv = {"STT":1, "Họ và Tên": "Nguyễn Quốc Thiện", "MSSV":"23673831", "Date":"26/9/2005", "Quê":"TpHCM", "Học Phí":"20.000.000", "Sở Thích":"Gái"}
sv1= {"Ten": "Thien", "MSSV":1, "Lop": "DHDT18b"}
sv2={"Ten": "Thang", "MSSV":2, "Lop": "DHDT19b"}
sv3={"Ten": "Dat", "MSSV":3, "Lop": "DHDT15b"}
choice = int(input("Lua chon bai: "))
match choice:
    case 7:
        bt7()
    case 8:
        bt8()
    case 9:
        bt9()
    case 10:
        bt10()
    case 11:
        DHDT12B, ANHVAN01 = bt105()
        bt11()
    case _:
        print("dumb")