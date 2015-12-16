"""
Plot degree distribution of randomly selected article network
"""

import csv
import random
import networkx as nx
import matplotlib.pyplot as plt

N = 1

# initialize dictionary of articles
article_editors = {}
with open("wiki.csv", "r", encoding="utf-8") as f:
	csvreader = csv.reader(f)
	for row in csvreader:
		if row[0]=='Editor':
			continue
		editor = row[0]
		article = row[1]
		num_edits = row[2]
		if article not in article_editors.keys():
			article_editors[article] = [editor]
		else:	
			article_editors[article].append(editor)

# construct network
G = nx.Graph()
rand = random.sample(article_editors.keys(), 100)
G.add_nodes_from(rand)
for key1 in rand:
	for key2 in rand:
		if key1 != key2:
			int_sec = set(article_editors[key1]).intersection( set(article_editors[key2]) )
			if (len(int_sec) >= N):
				G.add_edge(key1, key2)	

print("Number of nodes in the graph: ", G.number_of_nodes())
print("Number of edges in the graph: ", G.number_of_edges())

# plot degree distribution
degree_dist = {}
for val in G.degree().values():
	if val not in degree_dist:
		degree_dist[val] = 0
	degree_dist[val] += 1
plt.plot( list(degree_dist.keys()), list(degree_dist.values()), marker='+', color='b', linewidth=2, markersize=15 )
plt.title("Degree distribution (N={})".format(N))
plt.xlabel("Degree")
plt.ylabel("Number of nodes")
plt.savefig("deg_dist_{}.png".format(N))