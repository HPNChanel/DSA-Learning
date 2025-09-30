
#* Bài toán: Kiểm tra số nguyên tố

#? Hướng tiếp cận 1: Phương pháp chia thử nghiệm (CƠ BẢN) | Độ phức tạp: O(n) Time và O(1) Space
#* Về cơ bản, ta kiểm tra nếu số đó bé hơn 2 --> ko phải số nguyên tố. Ngược lại, lặp từ 2 đến n - 1, nếu n chia hết bất cứ một số nào --> ko phải số nguyên tố. Trường hợp còn lại sẽ là số nguyên tố (n ko chia hết bất cứ một số nào)

def isPrime(n):
    if n <= 1:
        return False 
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True


#? Hướng tiếp cận 2: Phương pháp chia thử nghiệm (NÂNG CAO) | Độ phức tạp: O(sqrt(n)) Time và O(1) Space
#* Về cơ bản, khi tìm kiếm ước số của một số, nó sẽ luôn luôn xuất hiện theo cặp. Ví dụ, nếu 4 là ước số của 28, thì 28 / 4 = 7 cũng là một ước số của 28 --> cặp (4, 7) là cặp ước số. Điều này có nghĩa là mỗi một ước số d của n, nó sẽ có một ước số cặp khác là n / d -> Nếu d <= sqrt(n), thì n / d >= sqrt(n). Vì vậy, ta chỉ cần kiểm tra các ước số đến sqrt(n). Nếu n có một ước số lớn hơn sqrt(n), ước số cặp của nó đã được kiểm tra bên dưới sqrt(n)

import math

def isPrime(n):
    
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True


#? Hướng tiếp cận 3: Phương pháp chia thử nghiệm được tối ưu hóa | Độ phức tạp: sqrt(n) Time và O(1) Space
#* Về cơ bản, mỗi số nguyên có thể được viết dưới dạng thức: 6k+i khi mà i từ 0 đến 5. Trong số này, dạng thức 6k, 6k+2, 6k+3 và 6k+4 đều chia hết cho 2 và 3, vì vậy nó không thể nào là số nguyên tố (trừ 2 và 3). Chính vì như thế, toàn bộ các số nguyên tố lớn hơn 3 phải là dạng thức 6k+1 hoặc 6k+5. Vì vậy, trong khi kiểm tra các ước số đến sqrt(n), ta có thể bỏ qua các số KHÔNG CÙNG CÁC DẠNG THỨC KỂ TRÊN --> giảm bớt số lần kiểm tra

import math

def isPrime(n):
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
