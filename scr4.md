
Thuật toán Euclid
EUCLUD ()

Kiến thức về lý thuyết số:
- Hai số nguyên tố cùng nhau nếu USCLN bằng 1. Ký hiệu. 20 và 15 có chung ước lớn nhất là 5 nên là 2 số nguyên tố cùng nhau:
    - 7.w(3) = 1 mod 10
    - 15 w(3) = 5 mod 20
- Định lý Fermat: nhỏ  

## bài tập RSA

### đề bài : P = 11 q =13 e = 11 M = 15 tính C???
- N = pq = 11x13 = 143 (2^7 = 128 < 143 < 256 = 2^8)
- n = (p-1)(q-1)= 120
- chọn e = 11 nguyên tố cùng nhau với n
- Tính nghịch đạo của e theo phep modulo n được d = 11 (11x11 = 121)
- Khóa công khai (e,N) = (11, 143) khóa bí mật (d,N) = (11,143)
- 15^11 mod 143 = 59

### đề bài : P = 5 q =11 M = 37 tính C???
- N = 55
- n = 40
- e = 7
- Tính nghịch đạo của e theo phep modulo n được d = 23 (7x23 = 161)
- Khóa công khai(e, N) = (7, 55) khóa bí mật (d,N) = (23, 55)
- M^e mod N = 37^7 mod 55 = 38
### Hàm băm
- ký hiệu $$H(x_1) = h_1$$
- Md5 và SHA-1