'''
활용예시
- 프린터 출력 대기열
- ROS 토픽 메시지 버퍼
- BFS
'''

# enquene : 뒤에 데이터 추가
# dequene : 앞에 데이터를 꺼냄

from collections import deque

queue = deque()
queue.append('A')   # enquene
queue.append('B')   
queue.append('C')

print(queue.popleft())  # -> 'A' 가장 먼저 넣은
print(queue.popleft())  # -> 'B'