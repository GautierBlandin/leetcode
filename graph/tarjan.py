def tarjan(graph: list[list[int]], debug=False) -> list[set[int]]:
    """
    Compute the list of Strongly Connected Components (SCCs) of the graph.

    Args:
        graph: A directed graph represented as an adjacency list
        debug: debug mode for logging

    Returns:
        The list of strongly connected components
    """
    n = len(graph)
    visited = n * [False]
    stack = []
    on_stack = n * [False]
    indexes = [-1] * n
    index = 0
    low_link = [float('inf')] * n

    sccs = []

    def dfs(node: int):
        if debug:
            print(f'node: {node}')
            print(f'stack: {stack}')
            print(f'visited: {visited}')
            print(f'indexes: {indexes}')
            print(f'low_link: {low_link}')

        nonlocal index
        indexes[node] = index
        low_link[node] = index
        index += 1

        stack.append(node)
        on_stack[node] = True

        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                dfs(child)
                low_link[node] = min(low_link[node], low_link[child])
            else:
                if on_stack[child]:
                    low_link[node] = min(low_link[node], indexes[child])

        if low_link[node] == indexes[node]:
            scc = set()
            s = stack.pop()
            while True:
                scc.add(s)
                on_stack[s] = False

                if s == node:
                    break
                else:
                    s = stack.pop()

            sccs.append(scc)
            if debug:
                print(f'new scc: {scc}')
                print(f'sccs: {sccs}')

    for start in range(n):
        if not visited[start]:
            visited[start] = True
            dfs(start)

    if debug:
        print(f'sccs: {sccs}')
    return sccs
