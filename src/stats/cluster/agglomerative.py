#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Agglomerative Clustering Algorithm

Iteratively build hierarchical cluster between all data points.
O(n^2) complexity

Author: Ryan Flynn <parseerror+agglomerative-clustering@gmail.com>

References:
 1. "Hierarchical Clustering Algorithms", http://home.dei.polimi.it/matteucc/Clustering/tutorial_html/hierarchical.html
 2. "How to Explain Hierarchical Clustering", Stephen P. Borgatti, http://www.analytictech.com/networks/hiclus.htm, Retrieved May 25, 2011
 3. Johnson,S.C. 1967, "Hierarchical Clustering Schemes" Psychometrika, 2:241-254.
"""

class Cluster:
	def __init__(self):
		pass
	def __repr__(self):
		return '(%s,%s)' % (self.left, self.right)
	def add(self, clusters, grid, lefti, righti):
		self.left = clusters[lefti]
		self.right = clusters[righti]
		# merge columns grid[row][righti] and row grid[righti] into corresponding lefti
		for r in grid:
			r[lefti] = min(r[lefti], r.pop(righti))
		grid[lefti] = map(min, zip(grid[lefti], grid.pop(righti)))
		clusters.pop(righti)
		return (clusters, grid)

def agglomerate(labels, grid):
	"""
	given a list of labels and a 2-D grid of distances, iteratively agglomerate
	hierarchical Cluster
	"""
	clusters = labels
	while len(clusters) > 1:
		# find 2 closest clusters
		print clusters
		distances = [(1, 0, grid[1][0])]
		for i,row in enumerate(grid[2:]):
			distances += [(i+2, j, c) for j,c in enumerate(row[:i+2])]
		j,i,_ = min(distances, key=lambda x:x[2])
		# merge i<-j
		c = Cluster()
		clusters, grid = c.add(clusters, grid, i, j)
		clusters[i] = c
	return clusters.pop()

if __name__ == '__main__':

	# Ref #1
	ItalyCities = ['BA','FI','MI','NA','RM','TO']
	ItalyDistances = [
		[  0, 662, 877, 255, 412, 996],
		[662,   0, 295, 468, 268, 400],
		[877, 295,   0, 754, 564, 138],
		[255, 468, 754,   0, 219, 869],
		[412, 268, 564, 219,   0, 669],
		[996, 400, 138, 869, 669,   0]]
	print agglomerate(ItalyCities, ItalyDistances)
	"""
	(((BA,(NA,RM)),FI),(MI,TO))
	   |   |  |    |    |__|
	   |   |__|    |     |
	   |____|      |     |
	     |_________|     |
	          |__________|
	"""

	# Ref 2
	USACities = ['BOS','NY','DC','MIA','CHI','SEA','SF','LA','DEN']
	USADistances = [
		[   0,  206,  429, 1504,  963, 2976, 3095, 2979, 1949],
		[ 206,    0,  233, 1308,  802, 2815, 2934, 2786, 1771],
		[ 429,  233,    0, 1075,  671, 2684, 2799, 2631, 1616],
		[1504, 1308, 1075,    0, 1329, 3273, 3053, 2687, 2037],
		[ 963,  802,  671, 1329,    0, 2013, 2142, 2054,  996],
		[2976, 2815, 2684, 3273, 2013,    0,  808, 1131, 1307],
		[3095, 2934, 2799, 3053, 2142,  808,    0,  379, 1235],
		[2979, 2786, 2631, 2687, 2054, 1131,  379,    0, 1059],
		[1949, 1771, 1616, 2037,  996, 1307, 1235, 1059,    0]]
	print agglomerate(USACities, USADistances)
	"""
	((((((BOS,NY),DC),CHI),DEN),(SEA,(SF,LA))),MIA)
               |__|   |    |    |     |   |  |      |
                |_____|    |    |     |   |  |      |
                   |       |    |     |   |__|      |
                   |_______|    |     |    |        |
                       |        |     |____|        |
                       |________|       |           |
                            |___________|           |
                                  |_________________|
	"""

