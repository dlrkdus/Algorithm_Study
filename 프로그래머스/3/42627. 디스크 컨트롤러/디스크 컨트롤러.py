import heapq

def solution(jobs):
    # 결과 값
    total_wait_time = 0
    now = 0  # 현재 시각
    waitings = []  # 대기열
    jobs.sort(key=lambda x: x[0])  # 요청 시각 기준으로 정렬
    num_jobs = len(jobs)

    # 프로그램이 모두 처리될 때까지 반복
    while jobs or waitings:
        # 현재 시각 기준으로 대기열에 넣기
        while jobs and jobs[0][0] <= now:
            job = jobs.pop(0)
            heapq.heappush(waitings, (job[1], job[0]))  # 실행 시간 기준으로 대기열에 추가

        # 대기열이 비어있다면 시간을 요청 시각으로 이동
        if not waitings and jobs:
            now = jobs[0][0]
            continue

        # 대기열에서 작업 처리
        if waitings:
            duration, request_time = heapq.heappop(waitings)
            now += duration  # 현재 시각을 작업 실행 시간만큼 증가
            total_wait_time += (now - request_time)  # 대기 시간 계산

    # 평균 대기 시간 반환
    return total_wait_time // num_jobs