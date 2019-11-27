import networkx as nx
from itertools import combinations

f = open("output_3breaks_3.txt",'w')

### difference_vector(x,y): function to calculate the result vector

def difference_vector(x,y):
    d = []
    for j in range(len(x)):
        d.append(x[j]-y[j])
    return d

### make_X(G,t): functions to make components with starting node t

def make_cycle0(G,t):
    G.add_edge(t,t+1,col='P')
    G.add_edge(t+1, t + 2, col='Q')
    G.add_edge(t+2, t + 3, col='P')
    G.add_edge(t+3, t + 4, col='Q')
    G.add_edge(t+4, t + 5, col='P')
    G.add_edge(t+5, t + 6, col='Q')
    G.add_edge(t+6, t+7, col='P')
    G.add_edge(t+7, t, col='Q')

def make_cycle2(G,t):
    G.add_edge(t,t+1,col='P')
    G.add_edge(t+1, t + 2, col='Q')
    G.add_edge(t+2, t + 3, col='P')
    G.add_edge(t+3, t + 4, col='Q')
    G.add_edge(t+4, t + 5, col='P')
    G.add_edge(t+5, t + 6, col='Q')
    G.add_edge(t+6, t+7, col='P')
    G.add_edge(t+7, t+8, col='Q')
    G.add_edge(t+8, t+9, col='P')
    G.add_edge(t+9, t, col='Q')

def make_path_pq2(G,t): #12
    G.add_edge(t,t+1,col='P')
    G.add_edge(t+1, t + 2, col='Q')
    G.add_edge(t+2, t + 3, col='P')
    G.add_edge(t+3, t + 4, col='Q')
    G.add_edge(t+4, t + 5, col='P')
    G.add_edge(t+5, t + 6, col='Q')
    G.add_edge(t+6,t+7,col='P')
    G.add_edge(t+7, t + 8, col='Q')
    G.add_edge(t+8, t + 9, col='P')
    G.add_edge(t+9, t + 10, col='Q')
    G.add_edge(t+10, t + 11, col='P')
    G.add_edge(t+11, t + 12, col='Q')
    G.add_edge(t + 12, t + 13, col='P')
    G.add_edge(t + 13, t + 14, col='Q')

def make_path_pq0(G,t): #16
    G.add_edge(t,t+1,col='P')
    G.add_edge(t+1, t + 2, col='Q')
    G.add_edge(t+2, t + 3, col='P')
    G.add_edge(t+3, t + 4, col='Q')
    G.add_edge(t+4, t + 5, col='P')
    G.add_edge(t+5, t + 6, col='Q')
    G.add_edge(t+6, t + 7, col='P')
    G.add_edge(t+7, t + 8, col='Q')
    G.add_edge(t+8, t + 9, col='P')
    G.add_edge(t + 9, t + 10, col='Q')
    G.add_edge(t + 10, t + 11, col='P')
    G.add_edge(t + 11, t + 12, col='Q')
    G.add_edge(t + 12, t + 13, col='P')
    G.add_edge(t + 13, t + 14, col='Q')
    G.add_edge(t + 14, t + 15, col='P')
    G.add_edge(t + 15, t + 16, col='Q')

def make_path_pp3(G,t): #14
    G.add_edge(t,t+1,col='P')
    G.add_edge(t+1, t + 2, col='Q')
    G.add_edge(t+2, t + 3, col='P')
    G.add_edge(t+3, t + 4, col='Q')
    G.add_edge(t+4, t + 5, col='P')
    G.add_edge(t+5, t + 6, col='Q')
    G.add_edge(t+6, t + 7, col='P')
    G.add_edge(t+7, t + 8, col='Q')
    G.add_edge(t + 8, t + 9, col='P')
    G.add_edge(t + 9, t + 10, col='Q')
    G.add_edge(t + 10, t + 11, col='P')
    G.add_edge(t + 11, t + 12, col='Q')
    G.add_edge(t + 12, t + 13, col='P')
    G.add_edge(t + 13, t + 14, col='Q')
    G.add_edge(t + 14, t + 15, col='P')


def make_path_pp1(G,t): #18
    G.add_edge(t,t+1,col='P')
    G.add_edge(t+1, t + 2, col='Q')
    G.add_edge(t+2, t + 3, col='P')
    G.add_edge(t+3, t + 4, col='Q')
    G.add_edge(t+4, t + 5, col='P')
    G.add_edge(t+5, t + 6, col='Q')
    G.add_edge(t+6, t + 7, col='P')
    G.add_edge(t+7, t + 8, col='Q')
    G.add_edge(t+8, t + 9, col='P')
    G.add_edge(t + 9, t + 10, col='Q')
    G.add_edge(t+10, t + 11, col='P')
    G.add_edge(t+11, t + 12, col='Q')
    G.add_edge(t+12, t + 13, col='P')
    G.add_edge(t+13, t + 14, col='Q')
    G.add_edge(t+14, t + 15, col='P')
    G.add_edge(t+15, t + 16, col='Q')
    G.add_edge(t+16, t + 17, col='P')

def make_path_qq3(G,t): #14
    G.add_edge(t,t+1,col='Q')
    G.add_edge(t+1, t + 2, col='P')
    G.add_edge(t+2, t + 3, col='Q')
    G.add_edge(t+3, t + 4, col='P')
    G.add_edge(t+4, t + 5, col='Q')
    G.add_edge(t+5, t + 6, col='P')
    G.add_edge(t+6, t + 7, col='Q')
    G.add_edge(t+7, t + 8, col='P')
    G.add_edge(t+8, t + 9, col='Q')
    G.add_edge(t+9, t + 10, col='P')
    G.add_edge(t+10, t + 11, col='Q')
    G.add_edge(t+11, t + 12, col='P')
    G.add_edge(t+12, t + 13, col='Q')
    G.add_edge(t + 13, t + 14, col='P')
    G.add_edge(t + 14, t + 15, col='Q')

def make_path_qq1(G,t): #18
    G.add_edge(t, t + 1, col='Q')
    G.add_edge(t + 1, t + 2, col='P')
    G.add_edge(t + 2, t + 3, col='Q')
    G.add_edge(t + 3, t + 4, col='P')
    G.add_edge(t + 4, t + 5, col='Q')
    G.add_edge(t + 5, t + 6, col='P')
    G.add_edge(t + 6, t + 7, col='Q')
    G.add_edge(t + 7, t + 8, col='P')
    G.add_edge(t + 8, t + 9, col='Q')
    G.add_edge(t + 9, t + 10, col='P')
    G.add_edge(t + 10, t + 11, col='Q')
    G.add_edge(t + 11, t + 12, col='P')
    G.add_edge(t + 12, t + 13, col='Q')
    G.add_edge(t + 13, t + 14, col='P')
    G.add_edge(t + 14, t + 15, col='Q')
    G.add_edge(t + 15, t + 16, col='P')
    G.add_edge(t + 16, t + 17, col='Q')

### make_graph(): function to make the starting graph
### (three of each component type)

def make_graph():
    t=0
    G = nx.MultiGraph()
    for i in range(3):
        make_cycle0(G,t)
        t+=8
        make_cycle2(G,t)
        t+=10
        make_path_pq0(G,t)
        t+=17
        make_path_pq2(G,t)
        t+=15
        make_path_pp1(G,t)
        t+=18
        make_path_pp3(G,t)
        t+=16
        make_path_qq1(G,t)
        t+=18
        make_path_qq3(G,t)
        t+=16
    return G


### count_cycles_paths(G): function to count cycles and paths in a graph

def count_cycles_paths(G):
    cyc0 = 0
    cyc2 = 0
    pq0 = 0
    pq2 = 0
    pp1 = 0
    pp3 = 0
    qq1 = 0
    qq3 = 0
    #find all connected components
    components = list(nx.connected_components(G))
    for c in components: #for each component
        l = list(c)
        #print(l)
        bool_temp = True
        for i in range(len(l)):
            x = G.degree(l[i])
            if x==1: #if there is a degree 1 node (i.e. if it is a path)
                bool_temp = False
        #print(bool_temp)
        if bool_temp == True: # if cycle (all nodes degree 2)
            edges = G.edges(l)
            p_count=0
            for e in edges:
                if len(l)>2:
                    if G.get_edge_data(*e)[0]['col']=='P': #count P edges
                        #print((G.get_edge_data(*e)[0]['col']))
                        p_count+=1
                        #print("yes")
                    if len(G.get_edge_data(*e))>1:
                        if G.get_edge_data(*e)[1]['col'] == 'P':  # count P edges
                            #print((G.get_edge_data(*e)[0]['col']))
                            #print("MORE THAN 1 MADE IT")
                            p_count += 1
                else: p_count=1
            if (2*p_count)%4==0: #determine length
                cyc0+=1
            if (2*p_count)%4==2: #determine length
                cyc2+=1
        else: #only paths
            p_count=0
            q_count=0
            edges_list = G.edges(l)
            for i in edges_list:
                    if G.get_edge_data(*i)[0]['col']=='P': #count P edges
                        p_count+=1
                    if G.get_edge_data(*i)[0]['col']=='Q': #count Q edges
                        q_count+=1
            if p_count==q_count: #if PQ path
                if (p_count+q_count)%4==0:
                    pq0+=1
                if (p_count+q_count)%4==2:
                    pq2+=1
            if p_count>q_count: #if PP path
                if (p_count+q_count)%4==1:
                    pp1+=1
                if (p_count+q_count)%4==3:
                    pp3+=1
            if p_count<q_count: #if QQ path
                if (p_count+q_count)%4==1:
                    qq1+=1
                if (p_count+q_count)%4==3:
                    qq3+=1
    return [cyc0,cyc2,pq0,pq2,pp1,pp3,qq1,qq3]


### return_pairs(nodes): return all 15 edge pairings (distinct) for a set of 6 nodes

def return_pairs(nodes):
    pairs = []
    a=nodes[0]
    b=nodes[1]
    c=nodes[2]
    d=nodes[3]
    e=nodes[4]
    f=nodes[5]
    #15 options
    pairs.append([[a, b], [c, d], [e, f]])
    pairs.append([[a, b], [c, e], [d, f]])
    pairs.append([[a, b], [c, f], [d, e]])
    pairs.append([[a, c], [b, d], [e, f]])
    pairs.append([[a, c], [b, e], [d, f]])
    pairs.append([[a, c], [b, f], [d, e]])
    pairs.append([[a, d], [b, c], [e, f]])
    pairs.append([[a, d], [b, e], [c, f]])
    pairs.append([[a, d], [b, f], [c, e]])
    pairs.append([[a, e], [b, c], [d, f]])
    pairs.append([[a, e], [b, d], [c, f]])
    pairs.append([[a, e], [b, f], [c, d]])
    pairs.append([[a, f], [b, c], [d, e]])
    pairs.append([[a, f], [b, d], [c, e]])
    pairs.append([[a, f], [b, e], [c, d]])
    return pairs


### construct tuples
G = make_graph()

pedges = []
for e in G.edges():
    if G.get_edge_data(*e)[0]['col']=='P':
        pedges.append(e)
edge_tuples = list(combinations(pedges,3))

all_results = []

for t in edge_tuples: #iterate over triples
    #print(t)
    #record chosen edges
    e1 = t[0]
    e2 = t[1]
    e3 = t[2]
    #record nodes
    n1 = e1[0]
    n2 = e1[1]
    n3 = e2[0]
    n4 = e2[1]
    n5 = e3[0]
    n6 = e3[1]
    #remove the 3 edges
    #construct 3 new edges from the 6 vertices in old edges
    nodes = [n1,n2,n3,n4,n5,n6]
    nodes_tuples = return_pairs(nodes)
    #print("here")
    for n in nodes_tuples: #iterate over 15 pairings
        #print(t)
        #print(n)
        G = make_graph()
        #remove the 3 edges
        G.remove_edge(n1, n2)
        G.remove_edge(n3, n4)
        G.remove_edge(n5, n6)
        new1 = n[0]
        new2 = n[1]
        new3 = n[2]
        #add the new edges
        G.add_edge(new1[0], new1[1], col='P')
        G.add_edge(new2[0], new2[1], col='P')
        G.add_edge(new3[0], new3[1], col='P')
        #use difference_vector to determine result
        d = difference_vector(count_cycles_paths(G),[3,3,3,3,3,3,3,3])

        if d not in all_results: #if result has not been found already
            print(d)
            all_results.append(d)

#print results
for a in all_results:
    f.write(str(a)+'\n')
#print number of results
f.write("Number of results\n")
f.write(str(len(all_results))+'\n')