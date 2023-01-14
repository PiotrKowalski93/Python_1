import math
import os
import random
import re
import sys
    

def find(parent, i):
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]

def union(parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

def kruskals(g_nodes, g_from, g_to, g_weight):

    graph = [(a,b,wt) for a,b,wt in zip(g_from,g_to,g_weight)]  
    graph.sort(key = lambda e: e[2])
    graph.remove((0,0,0))

    print("Graph:")
    print(graph)
    print("")

    result_graph = []

    parent = []
    rank = []

    # wszystkie wierzchołki i oznaczneie czy je odwiedziliśmy
    for node in range(g_nodes):
        parent.append(node)
        rank.append(0)

    print("Parents:")
    print(parent)
    print("")

    print("Rank:")
    print(rank)
    print("")

    i = 0
    
    visited_edges = 0

    # maksymalnie moze byc o jeden mniej polaczen niz wierzchołków
    while visited_edges < g_nodes - 1 and i < len(graph):
        edge = graph[i]
        i += 1
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        print("X | Y:")
        print(str(x) + " " + str(y))
        print("")

        if x != y:
            visited_edges += 1
            result_graph.append(edge)
            union(parent, rank, x, y)

            print("Parents:")
            print(parent)
            print("")

            print("Rank:")
            print(rank)
            print("")
    
    print(result_graph)

    total_weight = 0
    for edge in result_graph:
        total_weight += edge[2]
    
    return total_weight

if __name__ == '__main__':
    #g_nodes = 1000
    #g_edges = 10000

    g_nodes = 5
    g_edges = 6

    #g_nodes = 5
    #g_edges = 7

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    #with open("Input.txt", 'r') as f:
    #with open("Input2.txt", 'r') as f:
    with open("Input3.txt", 'r') as f:
        i = 0
        for line in f:
            g_from[i], g_to[i], g_weight[i] = map(int, line.rstrip().split(" "))
            i += 1

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    print(res)
