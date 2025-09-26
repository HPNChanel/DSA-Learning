
#* Cho một số nguyên dương n, tìm căn bậc hai của nó. Nếu n không phải là số chính phương, thì trả về `floor` của căn bậc hai của n


#? Hướng tiếp cận 1: sử dụng vòng lặp | Độ phức tạp: O(sqrt(n)) Time + O(1) Space
#* Bắt đầu từ 1 và bình phương mỗi số lên cho đến khi bình phương vượt quá số đã cho, số cuối cùng là số mà bình phương của nó bé hơn hoặc bằng n sẽ là kết quả

def floorSqrt(n):
    #* Bắt đầu duyệt từ 1 cho đến khi kết quả bình phương vượt quá n
    res = 1
    while res * res <= n:
        res += 1
    
    #* Trả về số nguyên lớn nhất mà bình phương của nó nhỏ hơn hoặc bằng n
    return res - 1

    """
    !Ở đây sẽ có thắc mắc là tại sao lại trả về res - 1 mà sao không trả về res
    
    ! Giả sử n = 9, tức là bình phương của 3, tại điều kiện res * res <= n thì res đã đạt đến 3, nhưng theo logic thì res phải vượt quá rồi mới lấy số sát nhất, nên res sẽ vẫn tiếp tục được tăng lên 1, nhưng khi lần kiểm tra tiếp theo, 4 * 4 > n --> trả về res = 4 - 1 = 3
    """


#? Hướng tiếp cận 2: sử dụng Binary Search (tìm kiếm nhị phân) | Độ phức tạp: O(log(n)) Time và O(1) Space

#* Bình phương của một số tăng lên khi số đó tăng lên, vì vậy căn bậc hai của n phải nằm trong một phạm vi được sắp xếp (đơn điệu). Nếu bình phương của một số lớn hơn n, căn bậc hai của nó phải nó hơn. Nếu nó nhỏ hơn hoặc bằng n, căn bậc hai có thể là chính số đó hoặc lớn hơn. Bởi vì nó hoạt động theo mô hình đó, ta có thể áp dụng `tìm kiếm nhị phân` trong khoảng từ 1 đến n để tìm kiếm căn bậc hai hiệu quả

def floorSqrt(n):
    #* Khởi tạo không gian tìm kiếm
    low = 1
    high = n
    res = 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        #* Nếu bình phương của mid nhỏ hơn hoặc bằng n thì cập nhật kết quả và tìm kiếm nửa lớn hơn
        if mid * mid <= n:
            res = mid
            low = mid + 1
        
        #* Nếu bình phương của mid vượt quá n, tìm kiếm ở nửa nhỏ hơn
        else:
            high = mid - 1
    
    return res


#? Hướng tiếp cận 3: sử dụng công thức sử dụng bởi máy tính bỏ túi | Độ phức tạp - O(1) Time và O(1) Space

#* Ý tưởng ở đây là sử dụng công thức toán học: sqrt(n) = e^(1/2 * log(n))
#! Bởi vì cách tính toán được thực hiện trong máy tính trong trường hợp số thập phân, nên kết quả từ biểu thức trên có thể ít hơn một chút so với căn bậc hai thực tế. Vì vậy, ta sẽ coi như số nguyên TIẾP THEO sau kết quả tính toán được là kết quả

import math

def floorSqrt(n):
    
    #* Công thức
    res = int(math.exp(0.5 * math.log(n)))
    
    #* Nếu bình phương của res + 1 nhỏ hơn hoặc bằng n, nó sẽ là kết quả của bài toán
    if (res + 1)**2 <= n:
        res += 1
    
    return res
    

#? Hướng tiếp cận 4: sử dụng hàm tích hợp | O(log(n)) Time and O(1) Space
import math

def floorSqrt(n):
    res = int(math.sqrt(n))
    return res
