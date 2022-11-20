from typing import Callable
import graph.tarjan as tarjan_file


def test_tarjan():
    tarjan_tester(tarjan_file.tarjan)


def tarjan_tester(tarjan: Callable[[list[list[int]]], list[set[int]]], verbose=False):
    """
    Verify that the input tarjan algorithm works correctly

    Args:
        tarjan: a tarjan algorithm, taking the graph represented as an adjacency list and returning the list of SCCs
        verbose: True to show test logs, false to show nothing
    """
    graph_1 = [
        [],
        [2],
        [0, 3],
        [1],
        [3, 2, 5],
        [4, 6],
        [3, 7],
        [6],
        [8, 7]
    ]

    sccs_1 = [
        {1, 2, 3},
        {4, 5},
        {6, 7},
        {8},
        {0}
    ]

    graph_2 = [
        [2],
        [0, 5],
        [1, 4],
        [2, 12],
        [3, 13, 5],
        [6, 7, 10],
        [8],
        [6, 9],
        [7, 9],
        [9],
        [9, 11],
        [10],
        [13],
        [14, 15],
        [15],
        [12]
    ]

    sccs_2 = [
        {0, 1, 2, 3, 4},
        {6, 7, 8},
        {9},
        {10, 11},
        {12, 13, 14, 15},
        {5}
    ]

    tests = [(graph_1, sccs_1),
             (graph_2, sccs_2)]

    for index, (arguments, results) in enumerate(tests):
        returned = tarjan(arguments)
        assert len(returned) == len(results)
        for s in results:
            assert returned.__contains__(s)
        if verbose:
            print(f"test {index} passed")
