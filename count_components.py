import networkx as nx
import construct_graphs as cg


def get_color_counts(G, comp):
    edges = G.edges(comp)
    p = 0
    q = 0
    for e in edges:
        if G.get_edge_data(*e)[next(iter(G.get_edge_data(*e)))]['col']=="P":
            p += 1
        elif G.get_edge_data(*e)[next(iter(G.get_edge_data(*e)))]['col']=="Q":#G.get_edge_data(*e)[0]['col'] == 'Q':
            q += 1
        else: print("ERROR: edge color")
    return [p, q, p+q]


def get_cycle_or_path(G, comp):
    is_cycle = True
    for l in comp:
        if G.degree(l) == 1:
            is_cycle = False
            break
    return is_cycle


def get_double_inf(G, comp):
    is_double_inf = False
    inf = 0
    if len(comp) == 2:
        for l in comp:
            if "inf" in str(l):
                inf += 1
        if inf == 2:
            is_double_inf = True
    return is_double_inf


def count_cycles_paths(G):
    cyc0 = 0
    cyc2 = 0
    pq0 = 0
    pq2 = 0
    pp1 = 0
    pp3 = 0
    qq1 = 0
    qq3 = 0
    components = nx.connected_components(G)
    for c in components:
        if get_double_inf(G, c) is False:
            if get_cycle_or_path(G, c) is True:
                if get_color_counts(G, c)[2] % 4 == 0:
                    cyc0 += 1
                else:
                    cyc2 += 1
            else:
                if get_color_counts(G, c)[0] == get_color_counts(G, c)[1]:
                    if get_color_counts(G, c)[2] % 4 == 0:
                        pq0 += 1
                    else:
                        pq2 += 1
                elif get_color_counts(G,c)[0] > get_color_counts(G,c)[1]:
                    if get_color_counts(G, c)[2] % 4 == 1:
                        pp1 += 1
                    else:
                        pp3 += 1
                else:
                    if get_color_counts(G, c)[2] % 4 == 1:
                        qq1 += 1
                    else:
                        qq3 += 1
    return [cyc0,cyc2,pq0,pq2,pp1,pp3,qq1,qq3]


def doJob():
    G = cg.create_genome()
    print(count_cycles_paths(G))


if __name__ == "__main__":
    doJob()