
#* Bài toán: Cho một số n, tìm tất cả các số nguyên tố bé hơn hoặc bằng n

#? Hướng tiếp cận 1: Sử dụng vòng lặp | Độ phức tạp: O(n*sqrt(n)) Time và O(1) Space
#* Cách này sẽ tìm tất cả các số nguyên tố từ 1 đến n bằng cách kiểm tra mỗi số đơn lẻ nó có nguyên tố hay không
#* Các bước như sau:
#* Lặp qua tất cả các số i từ 2 đến n
#* Ở mỗi số i, kiểm tra nếu nó chia hết cho số nào từ 2 đến i - 1
#* Nếu nó chia hết, i ko phải là số nguyên tố
#* Ngược lại, i là số nguyên tố

#* CODE THÌ GIỐNG CÁCH CŨ

#? Hướng tiếp cận 2: Sàng Nguyên Tố Eratosthenes
#* Sàng nguyên tố Eratosthenes là một cách hiệu quả hơn, nó tìm kiếm các số nguyên tố đến n bằng cách lặp lại việc đánh dấu bội số của mỗi số nguyên tố là phi nguyên tố, bắt đầu từ 2. Điều này làm tránh đi việc kiểm tra dư thừa và nhanh chóng lọc ra tất cả các hợp số
#* Khởi tạo một mảng nguyên tố Boolean từ [0...n] và set toàn bộ các entries thành true, ngoại trừ 0 và 1 (vì nó không phải là nguyên tố)
#* Bắt đầu từ 2, số nguyên tố nhỏ nhất
#* Cho mỗi một số p từ 2 đến sqrt(n)
#* Nếu p được đánh dấu là nguyên tố --> true
#* Đánh dấu tất cả bội số của p là không phải nguyên tố (set thành false), bắt đầu từ p * p (bởi vì bội số nhỏ hơn đã được đánh dấu bởi số nguyên tố nhỏ hơn)
#* Sau khi kết thúc vòng lặp, tất cả các entries `true` còn lại trong prime sẽ đại diện cho các số nguyên tố

def sieve(n):
    prime = [True] * (n + 1)
    p = 2
    
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)
    
    return res
