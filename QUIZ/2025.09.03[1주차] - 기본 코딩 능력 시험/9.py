#202311388 김민상
def add_matrices_3x3(A, B):
    C = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    for i in range(3):
        for j in range(3):
            C[i][j] = A[i][j] + B[i][j]
    return C

A = []
B = []

for i in range(3):    
    # 엔터 입력 전까지 띄어쓰기로 숫자 구분하여 이차원 리스트의 한 열에 추가
	A.append(list(map(int, input().split())))
print(A)
for i in range(3):    
	B.append(list(map(int, input().split())))
print(B)
print(add_matrices_3x3(A, B))