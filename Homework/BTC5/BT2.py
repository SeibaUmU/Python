# # Cho tập tin dữ liệu auto.csv, và list headers sau:
# headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style","drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type","num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
# Câu 1: Đọc dữ liệu từ tập tin auto.csv, kết hợp với list headers đã cho để tạo thành dataframe df có tiêu đề hoàn chỉnh.Liệt kê kiểu dữ liệu các cột của df. Liệt kê 5 dòng dữ liệu đầu tiên (head) của df
# Câu 2: Trong tập dữ liệu, có một số dữ liệu bị thiếu đi kèm với dấu ? , bạn hãy thay thế các dữ liệu này thành NaN. In lại 5 dòng dữ liệu đầu tiên của df
# Câu 3: Đổi kiểu dữ liệu các cột thành kiểu dữ liệu đúng theo mô tả sau
# # 1. make: alfa-romero, audi, bmw, chevrolet, dodge, honda, isuzu, jaguar, mazda, mercedes-benz, porsche,...
# # 2. fuel-type: diesel, gas.
# # 3. num-of-doors: four, two.
# # 4. body-style: hardtop, wagon, sedan, hatchback, convertible.
# # 5. drive-wheels: 4wd, fwd, rwd.
# # 6. engine-location: front, rear.
# # 7. wheel-base: continuous from 86.6 120.9.
# # 8. length: continuous from 141.1 to 208.1.
# # 9. width: continuous from 60.3 to 72.3.
# # 10. height: continuous from 47.8 to 59.8.
# # 11. curb-weight: continuous from 1488 to 4066.
# # 12. engine-size: continuous from 61 to 326.
# # 13. bore: continuous from 2.54 to 3.94.
# # 14. stroke: continuous from 2.07 to 4.17.
# # 15. horsepower: continuous from 48 to 288.
# # 16. peak-rpm: continuous from 4150 to 6600.
# # 17. city-mpg: continuous from 13 to 49.
# # 18. highway-mpg: continuous from 16 to 54.
# # 19. price: continuous from 5118 to 45400.
# Câu 4: Xóa bỏ các cột không cần thiết,chỉ giữ lại các cột:
# # "make","fuel-type","num-of-doors","body-style","drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine size","bore","stroke","horsepower","peak-rpm","city-mpg","highway-mpg","price"
# Câu 5: Liệt kê số dòng có giá trị null trong các thuộc tính
# Câu 6: Nếu cột 'num-of-doors' nếu có chứa giá trị NaN thì thay bằng giá trị phổ biến nhất của cột 'num-of-doors'
# Câu 7: Xóa tất cả các dòng có giá trị NaN trong cột 'price' (nếu có)
# Câu 8: Các cột kiểu số khác nếu chứa giá trị NaN thì thay thế bằng giá trị trung bình
# Câu 9: Đặt lại chỉ mục (index) sau khi đã bỏ các dòng có giá trị NaN trong cột 'price' và các cập nhật trên dữ liệu
# Câu 10: In thông tin thống kê chung của df
# Câu 11: Cho biết thông tin thống kê chung của các cột có kiểu dữ liệu là object.
# Câu 12: Cho biết số lượng của mỗi loại hệ thống dẫn động (drive-wheels)?
# Câu 13: Cho biết số lượng của mỗi loại động cơ (engine-location) ?
# Câu 14: Cho biết các giá trị của cột drive-wheels ?
# Câu 15: Tính giá (price) trung bình của mỗi loại hệ dẫn động (drive-wheels).
# Câu 16: Tính giá (price) trung bình của mỗi chiếc xe dựa vào kiểu dáng thân xe (body-style).
# Câu 17: Tính giá (price) trung bình mỗi kiểu dáng thân xe của các loại hệ dẫn động (drive-wheels).
# Câu 18: Từ câu trên, sử dụng hàm pivot để tạo bảng từ các nhóm cho dễ xem hơn.
# (drive-wheel thể hiện giá trị các dòng,  body-style thể hiện giá trị các cột)
# Câu 19: Vẽ biểu đồ thể hiện phân bố dữ liệu của cột price (histogram)
# Câu 20: Thể hiện hệ số tương quan của df
# Câu 21: Vẽ biểu đồ thể hiện giá trị giữa 'engine-size' và 'price'
# Câu 22: Vẽ biểu đồ boxplot thể hiện giá xe thay đổi như thế nào với từng loại body-style
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# Thiết lập font để hiển thị tiếng Việt
plt.rcParams['font.size'] = 10
sns.set_style("whitegrid")

# Headers được cung cấp
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", 
           "num-of-doors","body-style","drive-wheels","engine-location","wheel-base", 
           "length","width","height","curb-weight","engine-type","num-of-cylinders", 
           "engine-size","fuel-system","bore","stroke","compression-ratio",
           "horsepower","peak-rpm","city-mpg","highway-mpg","price"]

print("=" * 80)
print("PHÂN TÍCH DỮ LIỆU AUTO DATASET")
print("=" * 80)

# Câu 1: Đọc dữ liệu từ tập tin auto.csv
print("\n📋 Câu 1: Đọc dữ liệu và tạo DataFrame")
print("-" * 50)

try:
    # Đọc file CSV với headers đã định nghĩa
    df = pd.read_csv('auto.csv', names=headers, header=None)
    print(f"✅ Đã đọc thành công {len(df)} dòng dữ liệu")
    
    # Liệt kê kiểu dữ liệu các cột
    print("\n🔍 Kiểu dữ liệu các cột:")
    for col, dtype in df.dtypes.items():
        print(f"  {col:20} : {dtype}")
    
    # Hiển thị 5 dòng đầu tiên
    print("\n📊 5 dòng dữ liệu đầu tiên:")
    print(df.head())
    
except FileNotFoundError:
    print("❌ Không tìm thấy file auto.csv")
    print("⚠️  Tạo dữ liệu mẫu để demo...")
    
    # Tạo dữ liệu mẫu để demo
    sample_data = [
        [3,"?","alfa-romero","gas","std","two","convertible","rwd","front",88.6,168.8,64.1,48.8,2548,"dohc","four",130,"mpfi",3.47,2.68,9.0,111,5000,21,27,13495],
        [3,"?","alfa-romero","gas","std","two","convertible","rwd","front",88.6,168.8,64.1,48.8,2548,"dohc","four",130,"mpfi",3.47,2.68,9.0,111,5000,21,27,16500],
        [1,"?","alfa-romero","gas","std","two","hatchback","rwd","front",94.5,171.2,65.5,52.4,2823,"ohcv","six",152,"mpfi",2.68,3.47,9.0,154,5000,19,26,16500],
        [2,164,"audi","gas","std","four","sedan","fwd","front",99.8,176.6,66.2,54.3,2337,"ohc","four",109,"mpfi",3.19,3.40,10.0,102,5500,24,30,13950],
        [2,164,"audi","gas","std","four","sedan","4wd","front",99.4,176.6,66.4,54.3,2824,"ohc","five",136,"mpfi",3.19,3.40,8.0,115,5500,18,22,17450],
        [2,"?","audi","gas","std","two","sedan","fwd","front",99.8,177.3,66.3,53.1,2507,"ohc","five",136,"mpfi",3.19,3.40,8.5,110,5500,19,25,15250],
        [1,158,"audi","gas","std","four","sedan","fwd","front",105.8,192.7,71.4,55.7,2844,"ohc","five",136,"mpfi",3.19,3.40,8.5,110,5500,19,25,17710],
        [1,"?","audi","gas","std","four","wagon","fwd","front",105.8,192.7,71.4,55.7,2954,"ohc","five",136,"mpfi",3.19,3.40,8.5,110,5500,19,25,18920],
        [1,158,"audi","gas","turbo","four","sedan","fwd","front",105.8,192.7,71.4,55.9,3086,"ohc","five",131,"mpfi",3.13,3.40,8.3,140,5500,17,20,23875],
        [0,"?","audi","gas","turbo","two","hatchback","4wd","front",99.5,178.2,67.9,52.0,3053,"ohc","five",131,"mpfi",3.13,3.40,7.0,160,5500,16,22,"?"],
        [2,192,"bmw","gas","std","two","sedan","rwd","front",101.2,176.8,64.8,54.3,2395,"ohc","four",108,"mpfi",3.50,2.80,8.8,101,5800,23,29,16430],
        [0,192,"bmw","gas","std","four","sedan","rwd","front",101.2,176.8,64.8,54.3,2395,"ohc","four",108,"mpfi",3.50,2.80,8.8,101,5800,23,29,16925],
        [0,188,"bmw","gas","std","two","sedan","rwd","front",101.2,176.8,64.8,54.3,2710,"ohc","six",164,"mpfi",3.31,3.19,9.0,121,4250,21,28,20970],
        [1,125,"chevrolet","gas","std","two","hatchback","fwd","front",88.4,141.1,60.3,53.2,1488,"ohc","three",61,"2bbl",2.91,3.03,9.5,48,5100,47,53,5151],
        [1,125,"chevrolet","gas","std","four","sedan","fwd","front",94.5,155.9,63.6,52.0,1874,"ohc","four",90,"2bbl",3.03,3.11,9.6,70,5400,38,43,7957]
    ]
    
    df = pd.DataFrame(sample_data, columns=headers)
    print(f"✅ Đã tạo dữ liệu mẫu với {len(df)} dòng")
    
    print("\n🔍 Kiểu dữ liệu các cột:")
    for col, dtype in df.dtypes.items():
        print(f"  {col:20} : {dtype}")
    
    print("\n📊 5 dòng dữ liệu đầu tiên:")
    print(df.head())

# Câu 2: Thay thế dấu ? thành NaN
print("\n\n📋 Câu 2: Thay thế dấu ? thành NaN")
print("-" * 50)

df = df.replace('?', np.nan)
print("✅ Đã thay thế tất cả dấu '?' thành NaN")
print("\n📊 5 dòng dữ liệu đầu tiên sau khi thay thế:")
print(df.head())

# Câu 3: Đổi kiểu dữ liệu
print("\n\n📋 Câu 3: Đổi kiểu dữ liệu các cột")
print("-" * 50)

# Các cột số cần chuyển đổi
numeric_cols = ['wheel-base', 'length', 'width', 'height', 'curb-weight', 
                'engine-size', 'bore', 'stroke', 'horsepower', 'peak-rpm', 
                'city-mpg', 'highway-mpg', 'price']

# Chuyển đổi các cột số
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

print("✅ Đã chuyển đổi kiểu dữ liệu cho các cột số")
print("\n🔍 Kiểu dữ liệu sau khi chuyển đổi:")
for col, dtype in df.dtypes.items():
    if col in numeric_cols + ['make', 'fuel-type', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location']:
        print(f"  {col:20} : {dtype}")

# Câu 4: Xóa bỏ các cột không cần thiết
print("\n\n📋 Câu 4: Giữ lại các cột cần thiết")
print("-" * 50)

# Lưu ý: có lỗi typo trong yêu cầu "engine size" thay vì "engine-size"
cols_to_keep = ["make","fuel-type","num-of-doors","body-style","drive-wheels",
                "engine-location","wheel-base","length","width","height",
                "curb-weight","engine-size","bore","stroke","horsepower",
                "peak-rpm","city-mpg","highway-mpg","price"]

df = df[cols_to_keep]
print(f"✅ Đã giữ lại {len(cols_to_keep)} cột cần thiết")
print(f"📊 Kích thước DataFrame: {df.shape}")

# Câu 5: Liệt kê số dòng có giá trị null
print("\n\n📋 Câu 5: Số dòng có giá trị null trong các thuộc tính")
print("-" * 50)

null_counts = df.isnull().sum()
print("🔍 Số giá trị null trong từng cột:")
for col, count in null_counts.items():
    if count > 0:
        print(f"  {col:20} : {count}")

# Câu 6: Thay thế NaN trong 'num-of-doors' bằng giá trị phổ biến nhất
print("\n\n📋 Câu 6: Thay thế NaN trong 'num-of-doors'")
print("-" * 50)

if df['num-of-doors'].isnull().sum() > 0:
    most_common_doors = df['num-of-doors'].mode()[0]
    df['num-of-doors'].fillna(most_common_doors, inplace=True)
    print(f"✅ Đã thay thế NaN trong 'num-of-doors' bằng '{most_common_doors}'")
else:
    print("ℹ️  Không có giá trị NaN trong cột 'num-of-doors'")

# Câu 7: Xóa các dòng có giá trị NaN trong cột 'price'
print("\n\n📋 Câu 7: Xóa dòng có NaN trong 'price'")
print("-" * 50)

rows_before = len(df)
df = df.dropna(subset=['price'])
rows_after = len(df)
dropped_rows = rows_before - rows_after

print(f"✅ Đã xóa {dropped_rows} dòng có giá trị NaN trong 'price'")
print(f"📊 Số dòng còn lại: {rows_after}")

# Câu 8: Thay thế NaN trong các cột số khác bằng giá trị trung bình
print("\n\n📋 Câu 8: Thay thế NaN trong các cột số bằng giá trị trung bình")
print("-" * 50)

numeric_cols_to_fill = ['wheel-base', 'length', 'width', 'height', 'curb-weight', 
                        'engine-size', 'bore', 'stroke', 'horsepower', 'peak-rpm', 
                        'city-mpg', 'highway-mpg']

for col in numeric_cols_to_fill:
    if df[col].isnull().sum() > 0:
        mean_value = df[col].mean()
        df[col].fillna(mean_value, inplace=True)
        print(f"✅ Đã thay thế NaN trong '{col}' bằng giá trị trung bình: {mean_value:.2f}")

# Câu 9: Đặt lại chỉ mục
print("\n\n📋 Câu 9: Đặt lại chỉ mục")
print("-" * 50)

df = df.reset_index(drop=True)
print("✅ Đã đặt lại chỉ mục")
print(f"📊 Kích thước DataFrame cuối cùng: {df.shape}")

# Câu 10: Thông tin thống kê chung
print("\n\n📋 Câu 10: Thông tin thống kê chung")
print("-" * 50)
print(df.describe())

# Câu 11: Thống kê các cột object
print("\n\n📋 Câu 11: Thông tin thống kê các cột object")
print("-" * 50)
print(df.describe(include=['object']))

# Câu 12: Số lượng mỗi loại drive-wheels
print("\n\n📋 Câu 12: Số lượng mỗi loại hệ thống dẫn động (drive-wheels)")
print("-" * 50)
drive_wheels_counts = df['drive-wheels'].value_counts()
print(drive_wheels_counts)

# Câu 13: Số lượng mỗi loại engine-location
print("\n\n📋 Câu 13: Số lượng mỗi loại động cơ (engine-location)")
print("-" * 50)
engine_location_counts = df['engine-location'].value_counts()
print(engine_location_counts)

# Câu 14: Các giá trị của cột drive-wheels
print("\n\n📋 Câu 14: Các giá trị của cột drive-wheels")
print("-" * 50)
unique_drive_wheels = df['drive-wheels'].unique()
print(f"Các giá trị unique trong drive-wheels: {unique_drive_wheels}")

# Câu 15: Giá trung bình theo drive-wheels
print("\n\n📋 Câu 15: Giá trung bình theo loại hệ dẫn động")
print("-" * 50)
price_by_drive = df.groupby('drive-wheels')['price'].mean()
print("Giá trung bình theo drive-wheels:")
for drive, price in price_by_drive.items():
    print(f"  {drive:10} : ${price:,.2f}")

# Câu 16: Giá trung bình theo body-style
print("\n\n📋 Câu 16: Giá trung bình theo kiểu dáng thân xe")
print("-" * 50)
price_by_body = df.groupby('body-style')['price'].mean()
print("Giá trung bình theo body-style:")
for body, price in price_by_body.items():
    print(f"  {body:12} : ${price:,.2f}")

# Câu 17: Giá trung bình theo drive-wheels và body-style
print("\n\n📋 Câu 17: Giá trung bình theo drive-wheels và body-style")
print("-" * 50)
price_by_both = df.groupby(['drive-wheels', 'body-style'])['price'].mean()
print(price_by_both)

# Câu 18: Pivot table
print("\n\n📋 Câu 18: Bảng pivot")
print("-" * 50)
pivot_table = df.pivot_table(values='price', 
                           index='drive-wheels', 
                           columns='body-style', 
                           aggfunc='mean')
print(pivot_table)

# Câu 19: Biểu đồ histogram của price
print("\n\n📋 Câu 19: Vẽ biểu đồ phân bố giá")
print("-" * 50)

plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Phân bố giá xe (Price Distribution)', fontsize=16)
plt.xlabel('Giá (Price)', fontsize=12)
plt.ylabel('Tần suất (Frequency)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# Câu 20: Ma trận tương quan
print("\n\n📋 Câu 20: Hệ số tương quan")
print("-" * 50)

# Chỉ tính tương quan cho các cột số
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Ma trận tương quan (Correlation Matrix)', fontsize=16)
plt.tight_layout()
plt.show()

print("\n🔍 Hệ số tương quan với 'price':")
price_corr = correlation_matrix['price'].sort_values(ascending=False)
for var, corr in price_corr.items():
    if var != 'price':
        print(f"  {var:15} : {corr:6.3f}")

# Câu 21: Scatter plot engine-size vs price
print("\n\n📋 Câu 21: Biểu đồ scatter engine-size vs price")
print("-" * 50)

plt.figure(figsize=(10, 6))
plt.scatter(df['engine-size'], df['price'], alpha=0.6)
plt.title('Mối quan hệ giữa Engine Size và Price', fontsize=16)
plt.xlabel('Engine Size', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# Câu 22: Box plot price theo body-style
print("\n\n📋 Câu 22: Box plot giá theo body-style")
print("-" * 50)

plt.figure(figsize=(12, 6))
df.boxplot(column='price', by='body-style', figsize=(12, 6))
plt.title('Phân bố giá theo kiểu dáng thân xe')
plt.suptitle('')  # Xóa title mặc định
plt.xlabel('Body Style', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n" + "=" * 80)
print("✅ HOÀN THÀNH PHÂN TÍCH DỮ LIỆU AUTO DATASET")
print("=" * 80)