
#* Bài toán: cho một số nguyên không âm n, chuyển đổi số trên thành dạng nhị phân

#! Approach 1: Chia cho 2 và lấy ra phần dư 
def decToBinary(n):
    binArr = []
    
    while n > 0:
        bit = n % 2
        binArr.append(bit)
        n //= 2
    
    binArr.reverse()
    
    return "".join(binArr)


#! Approach 2: cũng là Approach 1 nhưng sử dụng đệ quy
def decToBinaryRec(n, binArr):
    if n == 0:
        return
    decToBinaryRec(n // 2, binArr)
    
    binArr.append(str(n % 2))

def decToBinary(n):
    if n == 0:
        return "0"
    
    binArr = []
    decToBinaryRec(n, binArr)
    return "".join(binArr)


#! Approach 3 (efficient): sử dụng toán tử Bitwise
#* Bằng cách sử dụng toán tử Bitwise, ta có thể trích xuất ra các chữ số nhị phân bằng việc kiểm tra bit trọng số thấp (n & 1) và sau đó dịch phải đi 1 (n >> 1) để thực thi bit tiếp theo. Thuật toán này nhanh hơn cách sử dụng modulo và phép chia số học
def decToBinary(n):
    #* Khởi tạo chuỗi để lưu trữ phần nhị phân
    bin = ""
    
    while n > 0:
        #* Tìm kiếm (n % 2) bằng cách sử dụng toán tử bitwise AND
        #* n & 1 sẽ cho ra bit trọng số thấp nhất (LSB - Least Significant Bit)
        bit = n & 1
        bin += str(bit)
        
        #* Dịch phải n đi 1 (tương đương với n = n // 2)
        #* Nó sẽ loại bỏ đi bit trọng số thấp nhất ở trên
        n >>= 1
    
    return bin[::-1]  #* Đảo ngược dãy trên là xong


#! Approach 4: sử dụng built-in method `bin()`
def decToBinary(n):
    return bin(n)[2::]  #* Vì bin() nó có 2 tiền tố 0x hoặc các tiền tố khác binary form thông thường, nên ta phải bỏ qua tiền tố trên để ra được chuỗi nhị phân phù hợp
