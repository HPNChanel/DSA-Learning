
#* Cho một số nguyên dương n, tìm tất cả các ước số riêng biệt của n

#? Hướng tiếp cận 1: Lặp đến n | Độ phức tạp: O(n) Time và O(1) Space
#* Ý tưởng là lặp qua tất cả các số từ 1 đến n, ở mỗi số, kiểm tra xem n có chia hết hay không, nếu có thì đó là ước số

def printDivisors(n):
    divisors = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    return divisors 


#? Hướng tiếp cận 2: Tìm tất cả các cặp ước số | Độ phức tạp: O(sqrt(n)) Time và O(1) Space
#* Ta thấy được toàn bộ các ước số của 1 số đều xuất hiện theo cặp. Ví dụ: n = 100, thì toàn bộ các cặp ước số của nó sẽ là: (1, 100), (2, 50), (4, 25), (5, 20), (10, 10) 
#* Thay vì lặp từ 1 đến n, ta chỉ lần lặp từ 1 đến căn bậc 2 của n. Vì mỗi một ước số a của n, thì ước số b tương ứng sẽ bằng n / a và được nhóm theo cặp (a, b). Ít nhất một trong 2 giá trị trong cặp sẽ nằm trong khoảng từ 1 đến căn bậc 2 của n
#* Ta có thể
#* Lặp từ 1 đến căn bậc 2 của n để tìm tất cả các ước số bé hơn hoặc bằng sqrt(n)
#* Tại mỗi một ước số d, ta cũng thêm vào một phần tử ước số cặp tương ứng là n / d
#* Không được sao chép số chia căn bậc 2 nếu n là số chính phương

import math

def printDivisors(n):
    divisors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                divisors.append(i)  #! Đây chính là trường hợp số chính phương, tức là trong cặp 2 số đều bằng nhau, chỉ lấy 1 số
            else:
                divisors.append(i)
                divisors.append(n // i)
    
    return divisors
