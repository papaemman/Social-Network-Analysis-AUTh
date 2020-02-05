import heapq
# from src.functions.GeneralGreedy import independent_cascade
from src.functions.IC import independent_cascade

def celf(graph, k, prob=0.1, n_iters=1000):

    gains = []
    for node in range(len(graph.nodes)):
        spread = monte_carlo(graph, [], node, R=n_iters)
        heapq.heappush(gains, (-spread, node))

    # we pop the heap to get the node with the best spread,
    # when storing the spread to negate it again to store the actual spread
    spread, node = heapq.heappop(gains)
    solution = [node]
    spread = -spread
    spreads = [spread]

    # record the number of times the spread is computed
    lookups = [len(graph.nodes)]

    for _ in range(k - 1):
        node_lookup = 0
        matched = False

        while not matched:
            node_lookup += 1

            # here we need to compute the marginal gain of adding the current node
            # to the solution, instead of just the gain, i.e. we need to subtract
            # the spread without adding the current node
            _, current_node = heapq.heappop(gains)
            spread_gain = monte_carlo(
                graph, solution, current_node, R=n_iters) - spread

            # check if the previous top node stayed on the top after pushing
            # the marginal gain to the heap
            heapq.heappush(gains, (-spread_gain, current_node))
            matched = gains[0][1] == current_node

        # spread stores the cumulative spread
        spread_gain, node = heapq.heappop(gains)
        spread -= spread_gain
        solution.append(node)
        spreads.append(spread)
        lookups.append(node_lookup)

    return solution, spreads, lookups


def monte_carlo(graph, seed_set, node, R):
    from copy import deepcopy
    seed_set_new = deepcopy(seed_set)
    seed_set_new.append(node)

    total = 0
    for i in range(R):
        spread = independent_cascade(graph, seed_set_new)
        for j in spread:
            total += len(j)

    return total / R