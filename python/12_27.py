print("="*33)
print("="*8, "20223175 문정은", "="*8)
print("="*8, "2일차 과제 결과", "="*8)
print("="*33)

while True:
    print('몇단까지 출력할까요?(2~9단, 나머지 정수 값 입력시 종료됨)')
    num = int(input('>>'))
    if 2 <= num <= 9:
        for i in range(2, num+1,4):
            for j in range(1, 10):
                for k in range(4):
                    if i+k > num:
                        continue
                    
                    else:
                        print('%d X %d = %d'%(i+k, j, (i+k)*j), end='\t')
                print()
            print()

    else:
        print('이용해 주셔서 감사합니다.')
        print('개발자 : 문정은(20223175)')
        break
