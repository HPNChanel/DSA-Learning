
#* Cho 2 số nguyên dương a và b, tìm GCD của 2 số trên

#! Lưu ý: GCD (Greatest Common Divisor) hoặc còn gọi là HCF(Highest Common Factor) - ước chung lớn nhất - của 2 số là số lớn nhất mà cả 2 số a và b đều chia hết

#* Hướng tiếp cận 1: Sử dụng vòng lặp - Độ phức tạp thời gian O(min(a, b)), độ phức tạp không gian O(1)

#* Ý tưởng là tìm số nhỏ nhất giữa 2 số và tìm ước lớn nhất của số này cũng đồng thời là của số kia

def gcd(a, b):
    
    result = min(a, b)  #* Tìm số nào nhỏ hơn giữa a và b
    
    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    
    #* Ý tưởng, chọn ra số nhỏ hơn giữa 2 số a và b, gán cho result là biến điểm dừng, cho duyệt result giảm dần, nếu đồng thời cả a và b đều chia hết cho result, dừng ngay vòng lặp --> result là kết quả cuối cùng
    
    return result


#* Hướng tiếp cận 2: Thuật toán Euclide ALgorithm bằng phép trừ

#* Ý tưởng: ước số chung lớn nhất của 2 số KHÔNG ĐỔI nếu số nhỏ hơn được trừ đi từ số lớn hơn. Đây chính là thuật toán EUCLIDE ALGORITHM bằng phép trừ. Nó là một tiến trình lặp lại phép trừ, tiếp cận kết quả `rel` sau mỗi lần cho đến khi kết quả BẰNG VỚI BẤT KỲ SỐ NÀO được trừ đi


""" 
pseudo code:

gcd(a, b):
    if a = b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
"""

def gcd(a, b):
    #* Mọi thứ đều chia hết cho 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    
    #* Base case (đệ quy)
    if a == b:
        return a
    
    #* Nếu trường hợp a lớn hơn
    if a > b:
        return gcd(a - b, b)  #* Call stack recursion
    
    return gcd(a, b - a)


"""
Giải thích:
    - Ta sẽ sử dụng thuật toán Hiệu Euclide vào cả 2 số, sử dụng result bằng chính con số còn lại sau mỗi lần trừ (bằng cách gọi đệ quy). Ta sẽ tiến hành trừ đi lần lượt 2 số (mặc định sẽ là số b lớn hơn a), nếu trường hợp a > b thì trừ đi a cho b, quá trình này lặp lại cho đến khi 1 số về 0, kết quả sẽ là số còn lại
    
    Ví dụ: a = 20, b = 28
    
    - Lần 1: gọi đệ quy - gcd(20, 28 - 20 = 8) - a = 20, b = 8
    - Lần 2: a > b --> gọi đệ quy - gcd(20 - 8 = 12, 8) - a = 12, b = 8
    - Lần 3: a > b --> gọi đệ quy - gcd(12 - 8, 8) - a = 4, b = 8
    - Lần 4: a < b --> gọi đệ quy - gcd(4, 8 - 4 = 4) - a = 4, b = 4
    - Lần 5: a = b --> trả về a = 4 --> rel = 4 ==> Ước chung lớn nhất của 20 và 28 là 4
"""

#* Hướng tiếp cận 3: Biến thể Hiệu Euclide bằng kiểm tra tính chia hết

#* Phương pháp này được tối ưu hơn so với thuật toán Hiệu Euclide gốc

#* Chúng ta nhìn lại ở một vài điểm, một số trở thành một ước số của một số khác vì vậy thay vì việc trừ lặp lại đến khi cả 2 số bằng nhau, ta có thể kiểm tra nếu nó là 1 ước số của số còn lại

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    if a == b:
        return a
    
    if a > b:
        if a % b == 0:
            return b
        return gcd(a - b, b)
    
    if b % a == 0:
        return a
    
    return gcd(a, b - a)

"""
Nhìn lại ví dụ: a = 20, b = 28
    
    - Lần 1: gọi đệ quy - gcd(20, 28 - 20 = 8) - a = 20, b = 8
    - Lần 2: a > b --> gọi đệ quy - gcd(20 - 8 = 12, 8) - a = 12, b = 8
    - Lần 3: a > b --> gọi đệ quy - gcd(12 - 8, 8) - a = 4, b = 8
    - Lần 4: vì b chia hết cho a, nên sẽ trả về a ngay lập tức --> a = 4 ==> Ước chung lớn nhất của 20 và 28 là 4
"""

#* Hướng tiếp cận 4: Biến thể Hiệu Euclide bằng kiểm tra số dư

#* Thay vì sử dụng thuật toán Hiệu Euclide, một hướng tiếp cận tốt hơn có thể được sử dụng. Chúng ta không triển khai phép trừ ở đây, ta liên tục chia số lớn hơn cho số nhỏ hơn và lấy ra phần dư

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


"""
Mỗi lần gọi đệ quy làm giảm đi kích thước của các số bằng cách sử dụng toán tử modulo, nó làm co lại đầu vào nhanh hơn phép trừ
Trường hợp xấu nhất cho số bước đó là khi đầu vào là số Fibonacci liên tiếp (consecutive), giống như (21, 13) --> điều này sẽ làm tối đa hóa lần gọi đệ quy
Bởi vì số Fibonacci tăng trưởng theo lũy thừa hóa, và số các bước tăng lên tuyến tính theo vị trí của n --> độ phức tạp thời gian là O(log(min(a, b)))
"""

#* Hướng tiếp cận 5: sử dụng built-in function

import math

def gcd(a, b):
    return math.gcd(a, b)
