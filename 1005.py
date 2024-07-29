import sys
input = sys.stdin.readline

from collections import deque

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())                                 # 건물 수(N) 및 간선(규칙) 수(K)

    time_info = ['건설시간:']                                         # 건물별 건설시간 리스트
    for time in list(map(int, input().split())):
        time_info.append(time)

    build_info = [[] for _ in range(N+1)]                             # 인접 리스트 빈 판 만들기
    in_degree = [0] * (N + 1)                                         # 진입 차수 기록할 리스트
    for _ in range(K):
        start, end = map(int, input().split())                        # 선행, 후행 건물을 뽑아

        in_degree[end] += 1                                           # 후행 건물 진입 차수 1 증가
        build_info[start].append(end)                                 # 간선정보 입력하기(일방향)

    destination = int(input())                                        # 목표 건물 입력

    queue = deque()                                                   # 선행 건물 순서로 들어갈 큐
    time_cnt = [0] * (N+1)                                            # 건물별 최종 건설소요시간이 기록될 리스트

    for i in range(1, N + 1):                                         # 모든 건물 돌며
        if not in_degree[i]:                                          # 최초 리프노드 탐색하여
            queue.append(i)                                           # 큐에 산입
            time_cnt[i] = time_info[i]                                # 그들의 최종 건설시간은 자기 건설시간 자체

    while queue:                                                      # 큐가 빌 때까지
        cur = queue.popleft()                                         # 하나씩 왼쪽에서 꺼내서
        cur_time = time_cnt[cur]                                      # 시간 기록

        if cur == destination:                                        # 목표 건물 나오면
            ans = cur_time                                            # 정답 기록하고
            break                                                     # break

        for nxt in build_info[cur]:                                   # 다음 탐색
            in_degree[nxt] -= 1                                       # 진입차수 하나씩 깎고
            time_cnt[nxt] = max(time_cnt[nxt], (cur_time + time_info[nxt]))     # 시간 갱신

            if not in_degree[nxt]:                                    # 진입 차수가 0이 되면
                queue.append(nxt)                                     # 큐에 추가
    
    print(ans)