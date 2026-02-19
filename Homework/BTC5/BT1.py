import pandas as pd
import numpy as np

class Part1:
    def __init__(self):
        # Khởi tạo dữ liệu chung cho cả Part1
        arr_1 = np.array([2, 4, 6, 8, 10])
        arr_2 = np.array([1, 3, 5, 7, 11])
        self.ser1 = pd.Series(arr_1)
        self.ser2 = pd.Series(arr_2)

    def C1(self):
        # Câu 1:
        # a/  Cho arr_1 là mảng số nguyên chẵn [2, 4, 6, 8, 10], arr_2 là mảng số nguyên lẻ [1, 3, 5, 7, 11]. 
        # Tạo biến kiểu Serries ser1 từ arr_1, ser2 từ arr_2. In danh sách các phần tử của ser1 và ser2
        print(self.ser1)
        print(self.ser2)
        # b/ Thực hiện phép toán và thể hiện kết quả của:  ser1 + ser2 
        print(self.ser1 + self.ser2)
        # c/ Thực hiện phép toán và thể hiện kết quả của:  ser1 - ser2 
        print(self.ser1 - self.ser2)
        # d/ Thực hiện phép toán và thể hiện kết quả của:  ser1 * ser2
        print(self.ser1 * self.ser2)
        # e/ Thực hiện phép toán và thể hiện kết quả của:  ser1 / ser2
        print(self.ser1 / self.ser2)

    def C2(self):
        # Câu 2
        # a/ Kiểm tra xem các phần tử của ser1 có > các phần tử của ser2 không?
        print(self.ser1 > self.ser2)
        # b/ Kiểm tra xem các phần tử của ser1 có < các phần tử của ser2 không?
        print(self.ser1 < self.ser2)
        # c/ Kiểm tra xem các phần tử của ser1 có = các phần tử của ser2 không?
        print(self.ser1 == self.ser2)

    def C3(self):
        # Câu 3
        # a/ Thêm 2 phần tử [6, 12] vào ser2. In lại danh sách các phần tử của ser2.
        self.ser2 = self.ser2._append(pd.Series([6, 12], index = [5, 6]))
        print(self.ser2)
        # b/ Tạo series ser3 chỉ chứa các phần tử có trong ser1 mà không có trong ser2. In danh sách các phần tử của ser3
        ser3 = pd.Series(dtype=int)  # tạo series rỗng
        for i in range(len(self.ser1)):
            if self.ser1[i] not in self.ser2.values:  # .values để so sánh với array
                ser3 = pd.concat([ser3, pd.Series([self.ser1[i]])], ignore_index=True)
        #ser3 = self.ser1[~self.ser1.isin(self.ser2)] #cach 2
        print(ser3)
                
        # c/ Tạo series ser4 chỉ chứa các phần tử có trong ser2 mà không có trong ser1. In danh sách các phần tử của ser4
        ser4 = self.ser2[~self.ser2.isin(self.ser1)]
        #isin() kt ser 2 co trong ser 1 ko, sau do tra ve 1 series toan true false (giong cau 2), ~ la not de dao false thanh true va ngc lai, lay nhung cai ko co
        #ser2[mask] đưa một mảng boolean vào chỉ mục của Series, Pandas sẽ lọc ra những phần tử có giá trị True
        print(ser4)
    def C4(self):
        # Câu 4: Tạo series ser5 chứa các phần tử chỉ có trong ser1 và chỉ có trong ser2. In danh sách các phần tử của ser5
        print("Truoc cau 3a")
        ser5 = self.ser1[self.ser1.isin(self.ser2)]
        print(ser5)
        print("Sau cau 3a")
        self.ser2 = self.ser2._append(pd.Series([6, 12], index = [5, 6]))
        ser5 = self.ser1[self.ser1.isin(self.ser2)]
        print(ser5)

class Part2:
    def __init__(self):
        np.random.seed(42)
        self.ser6 = pd.Series(np.random.randint(1, 10, 35))
    def C1(self):
        #  Câu 1
        # a/ Tạo series ser6 có 35 phần tử số nguyên ngẫu nhiên có giá trị trong khoảng từ 1 đến 9. Cho biết kích thước (shape) của ser6. Xem 5 dòng dữ liệu đầu tiên (head) và 5 dòng dữ liệu cuối cùng (tail) có trong ser6
        print("Ser6 shape: ", self.ser6.shape)
        print("head ser6")
        print(self.ser6.head(5))
        print("tail ser6")
        print(self.ser6.tail(5))
        # b/ In danh sách các phần tử của ser6 theo dạng array
        print(self.ser6.values)
        # c/ Cho biết thông tin thống kê chung (describe()) của ser6
        print(self.ser6.describe())
        # d/ Cho biết tổng của các phần tử có trong ser6
        print(self.ser6.sum())
        # e/ Cho biết phần tử có tần suất xuất hiện nhiều nhất trong ser6
        print(self.ser6.mode())

    def C2(self):
        # Câu 2:  Liệt kê các dòng trong ser6 mà giá trị chia hết cho 2 và cho 3
        sertest = self.ser6[(self.ser6 %2 == 0) & (self.ser6 %3 ==0)]
        print(sertest)
    def C3(self):
        # Câu 3: In các phần tử ở vị trí 0, 5, 10, 15 trong ser6
        print(self.ser6[:16:5])
    def C4(self):
        # Câu 4: In ra các giá trị unique (array) trong ser6
        print(self.ser6.unique())
    def C5(self):
        # Câu 5: Tạo series ser7 với mỗi phần tử có giá trị = lập phương của phần tử trong ser6. 
        # Xem 5 dòng dữ liệu đầu tiên (head) của ser7
        ser7 = self.ser6**2
        print(self.ser6.head(5))
        print(ser7.head(5))
        #Pandas kế thừa từ NumPy.
        #NumPy arrays hỗ trợ broadcasting và toán tử vector hóa. pandas.Series overload toán tử ** → gọi Series.pow(2) → tính bình phương từng phần tử một.

class Part3:
    
    def C1(self):
        # Câu 1: Cho list sau:
        lst = ["abc", "defg", "htlmj", "dfg", "ljsac"]
    # a/ Tạo series ser_chuoi từ lst 
        ser_chuoi = pd.Series(lst)
        print(ser_chuoi)
    # b/ Tạo series ser_dodai với mỗi phần tử có giá trị là chiều dài của mỗi phần tử trong ser_chuoi
        ser_dodai = ser_chuoi.str.len() #tuong tu ser_dodai = pd.Series([len(s) for s in ser_chuoi])
        print(ser_dodai)
    def C2(self):
        # Câu 2: Sử dụng biểu thức điều kiện thích hợp để in ra các dòng trong ser có giá trị là số nguyên tố
        ser = pd.Series(np.array([1, 2, 4, 5, 8, 7, 6, 9]))
        #cach 1:
        #print(ser[ser.apply(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False)])
    #.apply() áp dụng một hàm (lambda) cho từng phần tử x của Series.
    #th khoi lenh lambda x: neu x >1 thi th all(), else false
    #lap tu 2 doi can x (+1 de lay luon gt can x), dk cua for: x k chia het cho i
    #tat ca cac i trong vong deu ko chia het(vd: 5 ko chia het cho 2->can 5 = 3.23)
        #cach2:
        mask = []   # lưu True/False
        for x in ser:   # duyệt trực tiếp giá trị trong ser
            if x > 1:
                for i in range(2, int(x**0.5) + 1):
                    if x % i == 0:
                        mask.append(False)   # không phải số nguyên tố
                        break
                else:
                    mask.append(True)        # số nguyên tố
            else:
                mask.append(False)           # loại bỏ số <= 1

        # dùng mask lọc ser -> giữ index gốc
        ser_null = ser[mask]
        print(ser_null)

    def C3(self):
        import re
        # Câu 3: Cho mẫu email như sau:
        #pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
        #phần \.[A-Za-z]{2,4} chỉ cho phép đuôi domain dài 2–4 ký tự (.vn, .com, .org...)
#         [A-Za-z0-9._%+-]+ → ăn tran_2014

# @ → ăn @

# [A-Za-z0-9.-]+ → ăn hotmail.com (vì pattern cho phép dấu . bên trong)

# \.[A-Za-z]{2,4} → ăn .vn
        pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
#         Đây là biểu thức chính quy để tìm địa chỉ email:

# [A-Za-z0-9._%+-]+ → tên trước dấu @ (có thể chứa chữ, số, dấu chấm, gạch dưới, …)

# @ → dấu @ bắt buộc

# [A-Za-z0-9.-]+ → tên miền chính

# \. → dấu chấm trước phần mở rộng

# [A-Za-z]+ → phần mở rộng miền (com, net, org…)
    # Tạo một series ser_ch, với mỗi phần tử trong ser_ch là một chuỗi
    # Gợi ý: 'reading newspaper from tuoitre.vn', 'tubirona@gmail.com', 'nguyen.nn@yahoo.com', 'tran_2014@hotmail.com.vn'
    # In ra những dòng trong ser_ch thỏa điều kiện chuỗi là email
        # tạo series chuỗi
        ser_ch = pd.Series([
            'reading newspaper from tuoitre.vn',
            'tubirona@gmail.com',
            'nguyen.nn@yahoo.com',
            'tran_2014@hotmail.com.vn'
        ])

        # lọc ra các phần tử thỏa điều kiện email
        mask = [re.fullmatch(pattern, x) is not None for x in ser_ch]
        ser_email = ser_ch[mask]
#         re.fullmatch(pattern, x) kiểm tra chuỗi x có khớp toàn bộ pattern không.
# re.fullmatch(pattern, string)

# Thuộc module re (Regular Expression) của Python.

# Nó kiểm tra xem toàn bộ chuỗi có khớp với pattern không.
# Nếu có → trả về match object; nếu không → None.

# is not None → trả về True/False.
        print(ser_email)

    def C4(self):
        # Câu 4: Cho series:
        ser_names = pd.Series(['Manufacturer', 'Model', 'CarType', 'Min_Price', 'Price', 'Max_Price',
            'MPG_city', 'MPG_highway', 'AirBags', 'DriveTrain', 'Cylinders',
                'EngineSize', 'Horsepower', 'RPM', 'Rev_per_mile', 'Man_trans_avail',
                'Fuel_tank_capacity', 'Passengers', 'Length', 'Wheelbase', 'Width',
                'Turn_circle', 'Rear_seat_room', 'Luggage_room', 'Weight', 'Origin',
                'Make'])
    # Sử dụng biểu thức điều kiện thích hợp để in ra các dòng của ser_names thỏa điều kiện trong chuỗi có chữ 'Price'
        print(ser_names[ser_names.str.contains('Price')]) #, case=False) #bo qua hoa thuong

# .str là accessor của pandas cho các thao tác chuỗi.

# .contains('Price') kiểm tra mỗi phần tử trong Series có chứa chuỗi "Price" không.
# Trong pandas, accessor là một “cửa ngõ” đặc biệt để truy cập vào những thuộc tính hoặc phương thức dành riêng cho kiểu dữ liệu cụ thể bên trong Series/DataFrame.
# Để phân biệt phương thức của Series (như .mean(), .sum()) với phương thức riêng của kiểu dữ liệu.
# Phương thức của Series

# Đây là các hàm “chung” có thể dùng với mọi Series, bất kể kiểu dữ liệu bên trong.

# Ví dụ: .mean(), .sum(), .head(), .tail(), .sort_values(), .dropna(), .apply()…

# Chúng hoạt động trên đối tượng Series (là container) – tức là chúng không quan tâm phần tử bên trong là gì, miễn có thể tính toán được.
# Các phương thức này có thể áp dụng cho Series kiểu số, kiểu chuỗi, kiểu datetime… miễn phù hợp.

# Phương thức/thuộc tính của kiểu dữ liệu bên trong (qua accessor)

# Pandas cho phép bạn đi vào từng kiểu dữ liệu cụ thể bằng accessor:

# .str → các hàm xử lý chuỗi

# .dt → các hàm xử lý datetime

# .cat → các hàm xử lý category

# Những hàm này chỉ hoạt động với Series có kiểu dữ liệu phù hợp.
# Ví dụ: .str.upper() chỉ áp dụng được cho Series kiểu chuỗi.
# Giúp code gọn gàng và tránh nhầm lẫn.
# Một Series/DataFrame có thể chứa nhiều kiểu dữ liệu (chuỗi, datetime, category…).

# Mỗi kiểu dữ liệu lại có các phép xử lý chuyên biệt.

# Accessor giúp gom nhóm những phép xử lý đó lại trong một “namespace” riêng.
choice = int(input("BT1. Part: "))
match choice:
    case 1:
        choice1 = int(input("Câu: "))
        part1 = Part1()
        match choice1:
            # Part 1: Thực hiện các phép toán trên series
            case 1:
                part1.C1()
            case 2:
                part1.C2()
            case 3:
                part1.C3()
            case 4:
                part1.C4()
    case 2:
        choice2= int(input("Cau: "))
        part2 = Part2()
        match choice2:
            # Part 2: Truy xuất các phần tử, và thống kê thông tin trên series
            case 1:
                part2.C1()
            case 2:
                part2.C2()
            case 3:
                part2.C3()
            case 4:
                part2.C4()
            case 5:
                part2.C5()
    case 3:
        choice3 = int(input('Cau: '))
        part3 = Part3()
        match choice3:
            # Part 3: Tạo series từ list, chuỗi và biểu thức điều kiện
            case 1:
                part3.C1()
            case 2:
                part3.C2()
            case 3:
                part3.C3()
            case 4:
                part3.C4()
    case _:
        print('bi mu a?')







