화끈몬_체력 = 100
데미지 = 30
while 화끈몬_체력 > 0:
    화끈몬_체력 -= 데미지
    if 화끈몬_체력 < 0:
        print(f"화끈몬이 쓰러졌습니다.")
        break
    print(f"화끈몬이 공격받아 체력 {화끈몬_체력}이 남았습니다.")
