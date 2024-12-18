'''
1. build_frame을 순회하며 각 프레임별로 설치, 삭제가 가능한지 체크하는 함수 만들기
2. 일단 해당 프레임을 answer 리스트에 먼저 넣고 해당 프레임의 유효성을 판단하여 불가능 answer 리스트에서 다시 제거하는 방식으로 구현
3. check_frame은 answer에 있는 전체 프레임들을 순회하며 설치가 가능한지 확인하는 함수
'''

def check_frame(answer):
    for x,y,stuff in answer:

        # 보의 경우
        if stuff == 1:
            if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue

       # 기둥의 경우
        elif stuff == 0:
            if y == 0 or (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer:
                continue
        return False
    return True

def solution(n, build_frame):
    answer = set()
    for x,y,stuff,status in build_frame:

        # 설치의 경우
        if status == 1:
            answer.add((x,y,stuff))  # 일단 설치 했다고 치고 answer에 넣기
            if not check_frame(answer): # 설치가 불가능할 경우
                answer.remove((x,y,stuff))      # answer에서 다시 제거

        # 제거의 경우
        else:
            answer.remove((x, y, stuff)) # 일단 제거 했다고 치고 answer에 빼기
            if not check_frame(answer): # 제거가 불가능할 경우
                answer.add((x, y, stuff)) # answer에 다시 넣기

    return sorted(list(answer))