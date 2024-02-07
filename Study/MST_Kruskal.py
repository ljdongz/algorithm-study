"""
MST: 그래프상에 존재하는 모든 노드들을 최소비용으로 연결

<< Kruskal 알고리즘 구현 방법 >>
1. 그래프 간선들을 배열에 추가하여 비용의 오름차순으로 정렬
2. Union-Find 알고리즘 구현 및 부모(루트) 노드 정보 초기화
    (초기 부모 노드 정보는 각 노드 번호로 초기화)
3. 순차적으로 간선에 접근
    4. 사이클을 형성하지 않는 간선인 경우
        5. 비용 업데이트 및 부모 노드 정보 업데이트 (Union-Find 알고리즘 사용)
6. 비용 출력
"""

def mst_kruskal():

    # 1. 그래프 간선들을 배열에 추가하여 비용의 오름차순으로 정렬
    edges = []
    for cur_node, next_nodes in graph.items():
        for cost, next_node in next_nodes:
            edges.append((cost, (cur_node, next_node))) # 간선들을 배열에 추가
    edges.sort()


    result = 0
    
    # 2. Union-Find 알고리즘 구현 및 부모(루트) 노드 정보 초기화
    parent = [0] + [i for i in range(1, len(graph)+1)] # (노드 번호에 맞춰서) 부모 노드 초기화

    # 노드 X의 루트 노드를 찾음
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    # 연결된 두 노드의 루트 노드를 일치시킴
    def union(x, y):
        rootX = find_parent(x)
        rootY = find_parent(y)
        parent[rootY] = rootX # 순서 상관 X


    for cost, (xNode, yNode) in edges: # 3. 순차적으로 간선에 접근
        if parent[xNode] != parent[yNode]: # 4. 사이클을 형성하지 않는 간선인 경우
            # 5. 비용 업데이트 및 부모 노드 정보 업데이트 (Union-Find 알고리즘 사용)
            result += cost  
            union(xNode, yNode)
    
    # 6. 비용 출력
    print(result)



# (비용, 노드)
# 양방향 그래프를 표현한 것이지만 단방향 그래프로 정의됨
graph = {
    1: [(2,2), (1,4), (2,3)],
    2: [(2,4), (3,3)],
    3: [(1,5), (5,6), (3,4)],
    4: [(1,5)],
    5: [(2,6)],
    6: []
}

mst_kruskal()
