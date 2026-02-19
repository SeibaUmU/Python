import random
import math
#Thang code, THien thuyet trinh, Trong code phu, Phi tinh bao

# Low prime numbers de tang toc chuong trinh
lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
             449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


# Hàm kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if num % prime == 0:
            return False
    # tim c * 2^r = num - 1
    c =num - 1
    while c % 2 == 0:
        c //= 2  # Make c odd
    # cminh ko phai snt 10 lan
    for _ in range(10):
        if not rabin_miller(num, c):
            return False
    return True

def rabin_miller(n, d):
    """Rabin-Miller test"""
    a = random.randint(2, n - 2)
    x = pow(a, d, n)  # a^d % n
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2
        if x == 1:
            return False
        elif x == n - 1:
            return True

    return False
# Hàm tìm số nguyên tố ngẫu nhiên
def generate_prime(keysize):
    while True:
        prime = random.getrandbits(keysize//2)
        if is_prime(prime):
            return prime


# Hàm tìm nghịch đảo modulo
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1 # Lưu giá trị ban đầu của m, và thiết lập hệ số ban đầu
    while a > 1:
        if m == 0:
            return None  # Tránh chia cho 0
        q = a // m #q la thuong chia lay nguyen cua a va m
        m, a = a % m, m #cap nhat m, a theo Euclid (a se nhan gia tri m truoc khi chia)
        x0, x1 = x1 - q * x0, x0 #cap nhat x0, x1
    return x1 + m0 if  x1 < 0 else x1 #neu x1 am thi + x0 de ket qua luon duong

# Tạo khóa công khai và khóa bí mật RSA
def generate_keys(keysize=2048):
    while True:
        p = 7#generate_prime(keysize)
        q = 11#generate_prime(keysize)
        N = p * q
        #if (2**(keysize-1) < N < 2**keysize):
        break

    phi = (p - 1) * (q - 1)
    # Chọn e sao cho 1 < e < phi và e nguyên tố cùng nhau với phi
    e = 17#random.randrange(2, phi) #ko bao gam ca phi
    #while math.gcd(e, phi) != 1:  # Kiểm tra nếu e và phi có phải nguyên tố cùng nhau
        #e = random.randrange(2, phi)

    d = mod_inverse(e, phi) #list có thể thay đổi bên trong hàm, nhưng biến thì không

    # In các giá trị p, q, N, d, e
    print("p:", p)
    print("q:", q)
    print("N:", N)
    print("phi:",phi)
    print("e (khóa công khai):", e)
    print("d (khóa bí mật):", d)

    return (N, e), (N, d) 

# Mã hóa thông điệp
def encrypt(message, public_key):
    N, e = public_key #nhận giá trị lần lượt từ tuple
    return pow(message,e,N)#[pow(ord(char), e, N) for char in message] #lấy 1 kí tự từ chuỗi, biến về dạng ASCII dex rồi mũ e số đó và mod cho N 

# Giải mã thông điệp
def decrypt(ciphertext, private_key):
    N, d = private_key 
    return pow(ciphertext,d,N)#''.join([chr(pow(char, d, N)) for char in ciphertext]) #lấy từng phần tử trong cipher, mũ d mod N rồi biến về dạng ASCII chữ, ghép nối lại thành 1 chuỗi duy nhất
    
if __name__ == "__main__":

    # Nhập thông điệp từ người dùng
    message = int(input("Message: "))

    # Chương trình chính
    public_key, private_key = generate_keys() #tra ve 1 tuple (kieu dl chua day cac gia tri ko the bi thay doi, chua nhieu kieu dl khac nhau)

    # Mã hóa
    encrypted_message = encrypt(message, public_key)
    print("enc:", encrypted_message)

    # Giải mã
    decrypted_message = decrypt(encrypted_message, private_key)
    print("dec:", decrypted_message)
