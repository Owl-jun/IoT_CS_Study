import heapq

def dijkstra(graph, start):
    # 거리 초기화 (무한대로 설정)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 노드 거리: 0
    queue = [(0, start)]  # (거리, 노드)

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        # 이미 최적 경로를 찾은 경우 무시
        if distances[current_node] < current_dist:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            # 더 짧은 경로 발견 시 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# ✅ 수정된 그래프 (인접 리스트 + 가중치)
graph = {
    1: [(2, 2), (3, 5)],
    2: [(1, 2), (3, 1), (4, 3)],
    3: [(1, 5), (2, 1), (4, 2)],
    4: [(2, 3), (3, 2)]
}

# 실행 (시작 노드: 1)
distances = dijkstra(graph, 1)
for node, distance in distances.items():
    print(f"1번 노드 → {node}번 노드 최단 거리: {distance}")
