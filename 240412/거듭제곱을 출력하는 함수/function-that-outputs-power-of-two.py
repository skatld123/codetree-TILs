a, b = map(int, input().split())

def mul(a, b):
    if b == 0:
        return 1

    # 계산을 한 번만 하기 위해서 변수에 저장
    semi_result = mul(a, b // 2)
    
    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if b % 2 == 0:
        return semi_result * semi_result
    else:
        return a * semi_result * semi_result

print(mul(a, b))