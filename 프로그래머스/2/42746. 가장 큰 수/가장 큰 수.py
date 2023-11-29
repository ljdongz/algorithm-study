def solution(numbers):
    # 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 사전순으로 정렬 정렬
    """
    문자열은 첫 번째 문자부터 비교.
    Case 1. '8', '80' 비교 시
    - 첫 번째 문자끼리 비교
    - '8'은 두 번째 문자가 없기에 '8'이 '80'보다 먼저 위치
    Case 2. '888', '808080' 비교 시
    - 첫 번째 문자부터 순차적으로 비교
    - 두 번째 문자 비교를 통해 '808080'이 '888'보다 먼저 위치
    """
    numbers.sort(key=lambda x: x*3, reverse=True)

    # 정렬된 numbers를 이어붙인 뒤 반환
    answer = ''.join(numbers)

    # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
    if answer[0] == '0': return '0'
    else: return answer