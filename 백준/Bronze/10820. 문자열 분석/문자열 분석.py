import sys

try:
    while True:
        st = input()  # 문자열 입력
        lower_count = 0
        upper_count = 0
        digit_count = 0
        space_count = 0

        # 각 문자를 체크하며 카운트
        for s in st:
            if s.islower():  # 소문자 체크
                lower_count += 1
            elif s.isupper():  # 대문자 체크
                upper_count += 1
            elif s.isdigit():  # 숫자 체크
                digit_count += 1
            elif s == " ":  # 공백 체크
                space_count += 1
        
        # 결과 출력
        print(lower_count, upper_count, digit_count, space_count)
except EOFError:
    pass  # 입력이 끝났을 때 예외 처리
