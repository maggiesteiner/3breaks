import construct_graphs_2 as cg
import count_components as cc
from itertools import combinations
import sys


def get_k_breaks(k, nodes):
    result = []
    if len(nodes) != 2 * k:
        print("Error in number of nodes.")
        return []
    if k == 1:
        return [[nodes[0], nodes[1]]]
    else:
        ind = nodes[0]
        for i in nodes:
            if i != ind:
                nodes_temp = list(nodes)
                nodes_temp.remove(i)
                nodes_temp.remove(ind)
                new_result = get_k_breaks(k - 1, nodes_temp)
                for l in new_result:
                    if k == 2:
                        l = [l]
                    l.append([i, ind])
                    result.append(l)
        return result


def difference_vector(x, y):
    d = []
    for j in range(len(x)):
        d.append(x[j] - y[j])
    return d


def apply_k_breaks(G, k, edges_in, outcomes):
    breaks = get_k_breaks(k, [edges_in[0][0], edges_in[0][1], edges_in[1][0], edges_in[1][1], edges_in[2][0],
                              edges_in[2][1]])
    for b in breaks:
        G.remove_edges_from(edges_in)
        G.add_edges_from(b, col="P")
        result = difference_vector(cc.count_cycles_paths(G), [3, 3, 3, 3, 3, 3, 3, 3])
        if result not in outcomes:
            outcomes.append(result)
            print(edges_in)
            print(b)
            print(result)
        for x in b:
            if len(G.get_edge_data(x[0], x[1])) > 1:  # possible due to trivial cycles (bug fix)
                G.remove_edge(x[0], x[1], 1)
            else:
                G.remove_edge(x[0], x[1])
        G.add_edges_from(edges_in, col="P")
        if cc.count_cycles_paths(G) != [3, 3, 3, 3, 3, 3, 3, 3]:
            print("Error in genome")
            print(edges_in)
            print(b)
            sys.exit()


def doJob():
    f = open("output_3breaks_new.txt", 'w')
    G = cg.create_genome()
    edge_tuples = list(combinations(cg.get_p_edges(G), 3))
    outcomes = []
    i = 0
    for t in edge_tuples:
        if i % 100 == 0:
            print("Tuple: " + str(i))
        apply_k_breaks(G, 3, t, outcomes)
        i += 1
    print(cc.count_cycles_paths(G))
    for a in outcomes:
        f.write(str(a) + '\n')
    f.write("Number of results\n")
    f.write(str(len(outcomes)) + '\n')


if __name__ == "__main__":
    doJob()
