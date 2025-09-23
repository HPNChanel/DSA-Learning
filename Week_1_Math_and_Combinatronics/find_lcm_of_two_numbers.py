
#* Bài toán: Cho 2 số nguyên dương a và b. Tìm bội chung nhỏ nhất (LCM) của a và b

#! Note: LCM (Least Common Multiple) - bội chung nhỏ nhất của 2 số a và b là số nhỏ nhất có thể chia hết cho cả 2 số a và b đó

#? Hướng tiếp cận thông thường: Sử dụng vòng lặp có điều kiện

#* Hướng tiếp cận này tính toán LCM bằng việc bắt đầu từ số lớn hơn trong 2 số và kiểm tra nếu số lớn hơn đó chia hết cho số còn lại. Tiến hành lặp nhiều lần ở bội số của số lớn hơn, tăng dần bởi chính số lớn hơn đó ở mỗi bước. Bội số đầu tiên mà chia hết cho số nhỏ hơn thì đó là LCM. Phương thức này thì đơn giản và trực quan, tuy nhiên nó không hiệu quả, đặc biệt là đối với các số lớn, vì nó cứ liên tục kiểm tra giá trị bội số cho đến khi tìm được

def lcm(a, b):
    #* Lấy giá trị lớn hơn
    g = max(a, b)
    
    #* Lấy giá trị nhỏ hơn
    s = min(a, b)
    
    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    
    return a * b    

#? Hướng tiếp cận hiệu quả hơn: Sử dụng công thức GCD LCM

#* Hướng tiếp cận này hiệu quả hơn, vì nó dựa vào công thức tính bội chung nhỏ nhất

#* Cụ thể:
#* GCD(a, b) * LCM(a, b) = a * b
#* --> LCM(a, b) = (a * b) / GCD(a, b)

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b
