print('Nhập các dòng văn bản (nhập "done" để kết thúc):')
lines = []
while True:
    line = input()
    if line == "done":
        break
    lines.append(line)
print("\nCác dòng đã nhập sau chuyển thành chữ in hoa :")
for line in lines:
    print(line.upper())