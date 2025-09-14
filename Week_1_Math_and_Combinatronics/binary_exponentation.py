
def powMod(x, n, M):
    res = 1
    
    #* Ta lặp liên tục cho đến khi lũy thừa về 0
    while n >= 1:
        #* n là số lẻ, nhân kết quả với số x hiện tại và lấy ra phần dư
        if n % 2 != 0:
            res = (res * x) % M
            
            #* Biến đổi n về số chẵn
            n -= 1
        else:
            #* n là số chẵn, bình phương cơ số và chia đôi số mũ
            x = (x * x) % M
            n //= 2

    return res

