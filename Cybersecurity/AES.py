import base64
import copy
#Sbox
sbox = [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B,
    0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0,
    0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26,
    0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2,
    0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0,
    0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84, 0x53, 0xD1, 0x00, 0xED,
    0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F,
    0x50, 0x3C, 0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5,
    0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 0x13, 0xEC,
    0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14,
    0xDE, 0x5E, 0x0B, 0xDB, 0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C,
    0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D,
    0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F,
    0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E,
    0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11,
    0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F,
    0xB0, 0x54, 0xBB, 0x16]

inv_sbox = [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]

def Rotword(word):
    temp = word[0]
    word[0] = word[1]
    word[1] = word[2]
    word[2] = word[3]
    word[3] = temp
    return word

def subBytesKey(word):
    for i in range(4):  # Duyệt qua từng hàng
            # Chuyển đổi chuỗi hex sang int
            byte = int(word[i], 16)
            # Thay thế bằng byte từ S-box
            word[i] = hex(sbox[byte])  # Chuyển đổi trở lại thành hex
    return word

def KeyExpansion(key):
    Nk = 4  # Số lượng từ trong khóa (16 byte / 4 byte mỗi từ)
    Nr = 10  # Số lượng vòng trong AES (cho AES-128)
    Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x00]
    k=0

    for i in range(Nk):
        for j in range(4):
            roundKeys[0][i][j] = key[(i * 4) + j] # Chuyển đổi sang hex
    #khoa con
    for round in range(1, Nr+1):
        for i in range(4):
            temp = [0] * 4
            #lay cot cuoi
            for row in range(4):
                temp[row]=roundKeys[round-1][row][3]
            if i % 4 == 0:
                temp = Rotword(temp) #xoay
                
                temp = subBytesKey(temp)  # Hoán S-box
                temp[0] = int(temp[0], 16) #chuyen thanh int
                temp[0] ^= Rcon[k] #  XOR Rcon
                temp[0] = hex(temp[0])  #chuyen ve hex
                k += 1
                #Wi
                for row in range(4):
                    roundKeys[round][row][i] = hex(int(roundKeys[round - 1][row][i], 16) ^ int(temp[row], 16))
            else:
               for row in range(4):
                    roundKeys[round][row][i] = hex(int(roundKeys[round][row][i - 1], 16) ^ int(roundKeys[round - 1][row][i], 16)) 
    return roundKeys

def GF_mult(a, b):
    p = 0  # Kết quả
    for i in range(8):
        if b & 0x01:
            p ^= a  # Nếu bit thấp nhất của b là 1, XOR với a
        hi_bit_set = a & 0x80  # Kiểm tra bit cao nhất của a
        a <<= 1  # Nhân a với 2
        if hi_bit_set:
            a ^= 0x11B  # Nếu bit cao nhất bị set, XOR với 0x1B
        b >>= 1  # Chia b cho 2
    return p

def isBase64(chuoi):
    for char in chuoi:
          if not (char.isalnum() or char in ('+', '/', '=')):
            return False  # Không phải base64
    return True  # Là base64

def texttoByte(chuoi):
    # Chuyển chuỗi thành danh sách ký tự
    chuoi_hex = [hex(ord(c)) for c in chuoi]  # Chuyển các ký tự gốc thành hex

    # Bổ sung thêm '0x00' vào cuối nếu chuỗi ngắn hơn 16 ký tự
    while len(chuoi_hex) < 16:
        chuoi_hex.append('0x00')

    # Khởi tạo mảng 4x4 cho ciphertext và điền giá trị
    ciphertext = [[chuoi_hex[i * 4 + j] for j in range(4)] for i in range(4)]
    return ciphertext

def bytetoText(decrypt_2D):
    #khoi tao chuoi van ban
    text = ''.join(chr(int(value, 16)) for row in decrypt_2D for value in row)
    return text

def AddRoundKey(state, roundKeys):
     # Thực hiện phép XOR giữa state và roundKey
    for i in range(4):
        for j in range(4):
            state[i][j] = hex(int(state[i][j], 16) ^ int(roundKeys[i][j], 16))  # XOR với roundKey
    return state
def SubBytes(state):
    for i in range(4):
        for j in range(4):
            byte = int(state[i][j], 16)
            state[i][j] = hex(sbox[byte])
    return state

def InvSubBytes(state):
    for i in range(4):
        for j in range(4):
            byte = int(state[i][j], 16)
            state[i][j] = hex(inv_sbox[byte])
    return state

def ShiftRow(state):
    temp = [[0 for _ in range(4)] for _ in range(4)]
    #hang 0 giu nguyen
    #hang 1
    temp = state[1][0]
    state[1][0] = state[1][1]
    state[1][1] = state[1][2]
    state[1][2] = state[1][3]
    state[1][3] = temp

    #Hang 2
    temp = state[2][0]
    state[2][0] = state[2][2]
    state[2][2] = temp
    temp = state[2][1]
    state[2][1] = state[2][3]
    state[2][3] = temp

    # Hang 3
    temp = state[3][0]
    state[3][0] = state[3][3]
    state[3][3] = state[3][2]
    state[3][2] = state[3][1]
    state[3][1] = temp

    return state

def InvShiftRow(state):
    # Khởi tạo ma trận tạm
    temp = [[0 for _ in range(4)] for _ in range(4)]
    
    # Chuyển đổi hàng 1
    temp = state[1][3]
    state[1][3] = state[1][2]
    state[1][2] = state[1][1]
    state[1][1] = state[1][0]
    state[1][0] = temp
    
    # Hàng 2
    temp = state[2][0]
    state[2][0] = state[2][2]
    state[2][2] = temp
    temp = state[2][1]
    state[2][1] = state[2][3]
    state[2][3] = temp
    
    # Hàng 3
    temp = state[3][0]
    state[3][0] = state[3][1]
    state[3][1] = state[3][2]
    state[3][2] = state[3][3]
    state[3][3] = temp

    return state

def MixColumn(state):
    state = [[int(i, 16) for i in row] for row in state]
    for i in range(4):
        a = [state[j][i] for j in range(4)]
        state[0][i] = GF_mult(0x02, a[0]) ^ GF_mult(0x03, a[1]) ^ a[2] ^ a[3]
        state[1][i] = a[0] ^ GF_mult(0x02, a[1]) ^ GF_mult(0x03, a[2]) ^ a[3]
        state[2][i] = a[0] ^ a[1] ^ GF_mult(0x02, a[2]) ^ GF_mult(0x03, a[3])
        state[3][i] = GF_mult(0x03, a[0]) ^ a[1] ^ a[2] ^ GF_mult(0x02, a[3])

    state =[[hex(i) for i in row] for row in state]
    return state

def InvMixColumn(state):
    state = [[int(i, 16) for i in row] for row in state]
    for i in range(4):
        a = [state[j][i] for j in range(4)]
        state[0][i] = GF_mult(0x0E, a[0]) ^ GF_mult(0x0B, a[1]) ^ GF_mult(0x0D, a[2]) ^ GF_mult(0x09, a[3])
        state[1][i] = GF_mult(0x09, a[0]) ^ GF_mult(0x0E, a[1]) ^ GF_mult(0x0B, a[2]) ^ GF_mult(0x0D, a[3])
        state[2][i] = GF_mult(0x0D, a[0]) ^ GF_mult(0x09, a[1]) ^ GF_mult(0x0E, a[2]) ^ GF_mult(0x0B, a[3])
        state[3][i] = GF_mult(0x0B, a[0]) ^ GF_mult(0x0D, a[1]) ^ GF_mult(0x09, a[2]) ^ GF_mult(0x0E, a[3])
    state = [[hex(i) for i in row] for row in state]
    return state
    
def AES_encrypt(in_data, roundKeys):
    Nr = 10 #10 vong lap
    # Khởi tạo state với mảng 4x4
    state = [[0 for _ in range(4)] for _ in range(4)]
    # Chuyển đổi dữ liệu từ mảng 1D thành mảng 4x4
    for i in range(4):
        for j in range(4):
            state[i][j] = in_data[i * 4 + j]
    
    state = AddRoundKey(state, roundKeys[0])
    
    #9 vong lap
    for round in range(1, Nr):
        state = SubBytes(state)
        state = ShiftRow(state)
        state = MixColumn(state)
        state = AddRoundKey(state, roundKeys[round])
    #vong lap cuoi
    state = SubBytes(state)
    state = ShiftRow(state)
    state = AddRoundKey(state, roundKeys[Nr])

    
    for i in range(4):
        for j in range(4):
            encrypt[i * 4 + j] = state[i][j]
    return encrypt

def AES_decrypt(in_data, roundKeys):
    Nr = 10
    state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            state[i][j] = in_data[i * 4 + j]
    state = AddRoundKey(state, roundKeys[Nr])
    
    for round in range(Nr -1, 0, -1):
        state = InvShiftRow(state)
        state = InvSubBytes(state)
        state = AddRoundKey(state, roundKeys[round])
        state = InvMixColumn(state)
    state = InvShiftRow(state)
    state = InvSubBytes(state)
    state = AddRoundKey(state, roundKeys[0])
    for i in range(4):
        for j in range(4):
            decrypt[j * 4 + i] = state[i][j] 
    return decrypt

def encoded_base64(encrypt):
     # Chuyển đổi các giá trị hex từ chuỗi sang số nguyên
    byte_data = bytes(int(x, 16) for x in encrypt)

    # Bước 3: Chuyển đổi hex sang Base64
    encrypted = base64.b64encode(byte_data).decode('utf-8')

    return encrypted

def decoded_base64(chuoitemp, output_length):
    output_length = (len(chuoitemp) / 4 ) * 3
    if (chuoitemp[len(chuoitemp) - 1] == "="): 
        output_length -= 1
    if (chuoitemp[len(chuoitemp) - 2] == "="):
        output_length -= 1
    byte_data = base64.b64decode(chuoitemp)
    hex_string = byte_data.hex()
    
    return hex_string, output_length
    
if __name__ == "__main__":
    # Tạo list 3 chiều 11x4x4, tất cả phần tử là 0
    roundKeys = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(11)] #List Comprehension
    ciphertextArray = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(10)] #list chua toi da 10 mang 4x4
    ciphertextCount = 0
    matrices = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(10)]
    matrixCount = 0
    chuoi = input("Chuoi: ").strip()  # Loại bỏ ký tự newline

    #while True:
    key = input("Key: ").strip()
    key = [hex(ord(c)) for c in key] #doi Key thanh list hex
    while len(key) < 16:
        key.append('0x00') #them 0x00 neu nho hon 16
    
    roundKeys = KeyExpansion(key)

    if isBase64(chuoi):
        sokhoi = len(chuoi)//24
        chuoitemp = []
        output = []
        output_length = 0
        for i in range(sokhoi):
            start_index = i * 24  # Tính chỉ số bắt đầu
            end_index = start_index + 24  # Tính chỉ số kết thúc
            chuoitemp.append(chuoi[start_index:end_index])  # Thêm phần vào danh sách
        tempoutput =[]
        real_length = 0
        # Giải mã từng phần base64 và lưu kết quả
        for i in range(sokhoi):
            tempoutput, output_length = decoded_base64(chuoitemp[i], output_length)
            output.append(tempoutput)
            real_length+=int(output_length)
        
        # Tạo một chuỗi hex từ danh sách
        hex_string = ''.join(output)
        # Chia thành các byte
        output = ' '.join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))
        output = output.split()
        # Khởi tạo ma trận 4x4
        matrix = [[0 for _ in range(4)] for _ in range(4)]
        # Lưu các giá trị từ output vào matrix
        for i in range(0, real_length, 16):  # Bước 16
            for j in range(4):  # 4 hàng
                for k in range(4):  # 4 cột
                    index = i + j * 4 + k
                    if index < real_length:  # Kiểm tra để tránh lỗi chỉ số ngoài giới hạn
                        matrix[j][k] = f"0x{int(output[index], 16):02x}"

            #luu vao mang Matrices
            if (matrixCount<10):
                matrices[matrixCount] = copy.deepcopy(matrix) #sao chep ra 1 matrix rieng biet, li do thi no giong nhu ca gia dinh xai chung 1 vi tien
                matrixCount+=1
        #giai ma
        base64_decoded = [[0 for _ in range(32)] for _ in range(100)]
        for i in range(matrixCount):
            decrypt = [0] * 16
            in_data = [matrices[i][j][k] for j in range(4) for k in range(4)]
            decrypt = AES_decrypt(in_data, roundKeys)
            
            # Chuyển sang list 2D
            decrypt_2D = [[0 for _ in range(4)] for _ in range(4)]
            for row in range(4):
                for col in range(4):
                    decrypt_2D[row][col] = decrypt[col * 4 + row]

            # Gán kết quả vào base64_decoded
            base64_decoded[i] = bytetoText(decrypt_2D)

        if (len(chuoi) > 24):
            fntext = []
            for i in range(sokhoi):
                fntext.append(base64_decoded[i])
            # Ghép các phần tử trong fntext thành một chuỗi duy nhất
            joined_text = ''.join(fntext)
            print("Text:",joined_text)
        else:
            for i in range(sokhoi):
                print("Text:",base64_decoded[i])

    else:
        startIndex = 0
        while startIndex < len(chuoi):
            # Tạo một chuỗi con cho phần hiện tại
            subString = chuoi[startIndex:startIndex + 16]  # Cắt chuỗi 16 ký tự
            ciphertext = texttoByte(subString)
             # Lưu ciphertext vào ciphertextArray
            for i in range(4):
                for j in range(4):
                    ciphertextArray[ciphertextCount][i][j] = ciphertext[i][j]
            ciphertextCount+=1
            # Cập nhật startIndex để chuyển đến đoạn tiếp theo
            startIndex += 16  # Di chuyển chỉ số lên 16 để tiếp tục vòng lặp
        # Tạo list 2 chiều với kích thước [100][32], tất cả giá trị đều là 0
        base64_encoded = [[0 for _ in range(32)] for _ in range(100)] #kytu _ dc dung de biet day chi la 1 bien tam thoi, vong dau tien la de tao 32 cot voi gia tri 0, vong lap 2 de tao 100 hang (lap lai vong dau tien 32 lan)
        for i in range(ciphertextCount):
            encrypt = [0] * 16
            # Lấy khối 4x4 từ ciphertextArray
            in_data = [ciphertextArray[i][j][k] for j in range(4) for k in range(4)] # Chuyển đổi khối 4x4 thành danh sách 1D
            encrypt = AES_encrypt(in_data, roundKeys)
            base64_encoded[i] = encoded_base64(encrypt) #chuyen thanh base64
        if len(chuoi) <=16 :
            for i in range(ciphertextCount):
                print("Ciphertext in Base64:",base64_encoded[i])
        else:
            fnciphertext = []  # Khởi tạo fnciphertext bên ngoài vòng lặp
            for i in range(ciphertextCount):
                fnciphertext.append(base64_encoded[i])  # Thêm từng chuỗi Base64 vào danh sách

            # Sau khi hoàn thành vòng lặp, nối tất cả các phần tử lại thành một chuỗi duy nhất
            print("Ciphertext in Base64:", "".join(fnciphertext))

            





   

    
    
    

            
