def tarjan(graph: list[list[int]]) -> list[set[int]]:
    """
    Compute the list of Strongly Connected Components (SCCs) of the graph.

    Args:
        graph: A directed graph represented as an adjacency list

    Returns:
        The list of strongly connected components
    """
    n = len(graph)
    visited = n * [False]
    stack = []
    indexes = [-1] * n
    index = 0
    low_link = [float('inf')] * n

    sccs = []

    def dfs(node: int):
        nonlocal index
        indexes[node] = index
        index += 1

        stack.append(node)

        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                dfs(child)
                low_link[node] = min(low_link[node], low_link[child], indexes[child])
            else:
                if stack.__contains__(child):
                    low_link[node] = min(low_link[node], indexes[child])

        if low_link[node] <= indexes[node]:
            scc = set()
            while s := stack.pop != node:
                scc.add(s)
            sccs.append(scc)

    for start in range(n):
        if not visited[start]:
            dfs(start)

    return sccs
