
#* Thuật toán Sieve of Eratosthenes (Sàng Nguyên Tố) là một thuật toán tối ưu hơn để tìm tất cả các số nguyên tố đến 1 số n cho trước
#! Nó nhanh hơn việc kiểm tra mỗi số đơn lẻ

def sieve(n):
    #* Tạo một danh sách dạng boolean để track trạng thái nguyên tố của các số
    prime = [True] * (n + 1)
    p = 2  #* Bắt đầu từ 2
    
    #* Thuật toán sàng nguyên tố
    while p * p <= n:
        if prime[p]:
            #* Ta đánh dấu rằng tất cả bội số của p là non-prime (tức là không phải nguyên số)
            for i in range(p * p, n + 1, p):
                prime[i] = False
        
        p += 1

    #* Lúc này thu thập các phần tử nguyên tố
    res = []
    
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)
    
    return res

