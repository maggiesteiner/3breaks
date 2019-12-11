import networkx as nx
import count_components as cc


def create_path(G, len, first_color="P", start_index=0):
    if first_color == "P":
        for i in range(start_index, start_index + len):
            if i % 2 == 0:
                G.add_edge(i, i + 1, col="P")
            else:
                G.add_edge(i, i + 1, col="Q")
    if first_color == "Q":
        for i in range(start_index, start_index + len):
            if i % 2 == 0:
                G.add_edge(i, i + 1, col="Q")
            else:
                G.add_edge(i, i + 1, col="P")


def get_opposite_color(x):
    if x == "P": return "Q"
    if x == "Q": return "P"


def add_inf_edges(G, start_index, end_index):
    G.add_edge(start_index, "inf" + str(start_index),
               col=get_opposite_color(G.get_edge_data(start_index, start_index + 1)[0]['col']))
    G.add_edge(end_index, "inf" + str(end_index),
               col=get_opposite_color(G.get_edge_data(end_index, end_index - 1)[0]['col']))


def create_pq_0_path(G, start_index, n=1):
    for i in range(n):
        create_path(G, 10, "P", start_index + i * 11)
        add_inf_edges(G, start_index + i * 11, start_index + i * 11 + 10)


def create_pq_2_path(G, start_index, n=1):
    for i in range(n):
        create_path(G, 12, "P", start_index + i * 13)
        add_inf_edges(G, start_index + i * 13, start_index + i * 13 + 12)


def create_qq_1_path(G, start_index, n=1):
    for i in range(n):
        create_path(G, 7, "P", start_index + i * 8)
        add_inf_edges(G, start_index + i * 8, start_index + i * 8 + 7)


def create_qq_3_path(G, start_index, n=1):
    for i in range(n):
        create_path(G, 9, "P", start_index + i * 10)
        add_inf_edges(G, start_index + i * 10, start_index + i * 10 + 9)


def create_pp_1_path(G, start_index, n=1):
    for i in range(n):
        create_path(G, 7, "Q", start_index + i * 8)
        add_inf_edges(G, start_index + i * 8, start_index + i * 8 + 7)


def create_pp_3_path(G, start_index, n=1):
    for i in range(n):
        create_path(G, 9, "Q", start_index + i * 10)
        add_inf_edges(G, start_index + i * 10, start_index + i * 10 + 9)


def create_cycle_0(G, start_index, n=1):
    for i in range(n):
        create_path(G, 11, "P", start_index + i * 12)
        G.add_edge(start_index + i * 12, start_index + i * 12 + 11, col=get_opposite_color(
            G.get_edge_data(start_index + i * 12 + 11, start_index + i * 12 + 10)[0]['col']))


def create_cycle_2(G, start_index, n=1):
    for i in range(n):
        create_path(G, 13, "P", start_index + i * 14)
        G.add_edge(start_index + i * 14, start_index + i * 14 + 13, col=get_opposite_color(
            G.get_edge_data(start_index + i * 14 + 13, start_index + i * 14 + 12)[0]['col']))


def create_genome():
    G = nx.MultiGraph()
    create_cycle_0(G, 0, n=3)
    create_cycle_2(G, 36, n=3)
    create_pq_0_path(G, 78, n=3)
    create_pq_2_path(G, 111, n=3)
    create_pp_1_path(G, 150, n=3)
    create_pp_3_path(G, 174, n=3)
    create_qq_1_path(G, 204, n=3)
    create_qq_3_path(G, 228, n=3)
    G.add_edge("inf_test_1", "inf_test_2", col="P")
    return G


def get_p_edges(G):
    pedges = []
    for e in G.edges():
        if G.get_edge_data(*e)[next(iter(G.get_edge_data(*e)))]['col'] == "P":
            pedges.append(e)
    return pedges


def doJob():
    G = create_genome()
    print(G.edges())
    print(len(G.edges()))
    for x in nx.connected_components(G):
        print(x)
    print(cc.count_cycles_paths(G))
    print(len(get_p_edges(G)))


if __name__ == "__main__":
    doJob()
