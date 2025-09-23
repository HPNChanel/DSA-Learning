
#* Bài toán: cho một số `s` được thể hiện dưới dạng chuỗi, xác định nếu dạng số nguyên của nó có chia hết cho 13 hay không?

#* Nhìn qua thì bài toán này khá dễ, nhưng phân tích sâu hơn thì sẽ có những cách tối ưu hơn so với hướng tiếp cận thông thường

#? Hướng tiếp cận 1: Sử dụng phép chia lấy dư

#* Lưu ý: nếu số đã cho nhỏ, ta có thể dễ dàng kiểm tra nếu số đó có chia hết cho 13 hay không bằng cách sử dụng toán tử %

def divBy13(s):
    num = int(s)
    
    return num % 13 == 0

#! Tuy nhiên, phương thức này chỉ hoạt động với số phù hợp với kiểu dữ liệu số nguyên chuẩn. Với các số rất lớn, hướng tiếp cận này có thể sẽ bị tràn bộ nhớ hoặc không hỗ trợ


#? Hướng tiếp cận 2: Tổng xen kẽ của các khối 3 chữ số

#* Một số chia hết cho 13 nếu và chỉ nếu tổng xen kẽ của các khối 3 chữ số của nó, bắt đầu từ phải sang trái, đều chia hết cho 13

#* Các bước làm:
#* Thêm vào các số sao cho ĐỘ DÀI của nó là bội số của 3: nếu số các chữ số của một số không phải bội số của 3, thêm số 0 vào bên phải sao cho mỗi khối có đúng chính xác 3 chữ số. Ví dụ: "2911285" -> "291128500" (sau khi thêm vào 2 chữ số 0)
#* Chia thành các khối có 3 chữ số bắt đầu từ phải qua trái: "291128500" -> blocks: 500,128,291
#* Áp dụng các dấu xen kẽ bắt đầu với `+` từ khối phải ngoài cùng:
#* -> + block, - block, + block
#* -> +500 - 128 + 291
#* Tính tổng kết quả: 500 - 128 + 291 = 663
#* Nếu tổng đó chia hết cho 13, thì số gốc sẽ chia hết cho 13
#* 663 % 13 == 0

def divBy13(s):
    length = len(s)
    
    #* Trường hợp đặc biệt: nếu số đó là "0"
    if length == 1 and s[0] == '0':
        return True
    
    if length % 3 == 1:
        s += "00"
        length += 2
    elif length % 3 == 2:
        s += "0"
        length += 1
    
    sum_ = 0
    p = 1
    
    #* Duyệt từ phải sang trái theo các bước 3 chữ số
    i = length - 1
    while i >= 0:
        group = 0
        group += int(s[i])
        i -= 1
        group += int(s[i]) * 10
        i -= 1
        group += int(s[i]) * 100
        i -= 1
        
        sum_ += group * p
        p *= -1
    
    sum_ = abs(sum_)
    return sum_ % 13 == 0

#? Hướng tiếp cận 3: Modulo dựa trên chuỗi (tối ưu)
#* Ta xử lý các chữ số theo từng chữ số từ trái sang phải, duy trì phần còn lại theo modulo 13 ở mỗi bước sử dụng công thức: rem = (rem * 10 + digit) % 13

"""
Ví dụ: n = "2911285"
-> rem = 0
Bắt đầu xử lý mỗi chữ số:
-> '2': rem = (0 * 10 + 2) % 13 = 2
-> '9': rem = (2 * 10 + 9) % 13 = 29 % 13 = 3
-> '1': rem = (3 * 10 + 1) % 13 = 31 % 13 = 5
-> '1': rem = (5 * 10 + 1) % 13 = 51 % 13 = 12
-> '2': rem = (12 * 10 + 2) % 13 = 122 % 13 = 5
-> '8': rem = (5 * 10 + 8) % 13 = 58 % 13 = 6
-> '5': rem = (6 * 10 + 5) % 13 = 65 % 13 = 0

--> Bởi vì rem đã = 0, số 2911285 chia hết cho 13
"""
def divBy13(s):
    rem = 0
    
    for ch in s:
        rem = (rem * 10 + int(ch)) % 13
    
    return rem == 0
