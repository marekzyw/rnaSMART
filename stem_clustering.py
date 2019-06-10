from additional_classes import Motif
import fastcluster
import scipy.cluster.hierarchy as sch
import numpy as np


class StemClustering:
	def __init__(self):
		self.new_motifs = {}
		self.distances = {}

	def clustering_by_stems(self, matrix, motif, shape, distance):
		linkage = fastcluster.linkage(matrix, method="single")
		z_matrix = sch.fcluster(linkage, distance, criterion='distance')
		for i in range(0, max(z_matrix)+1):
			self.new_motifs[i] = []
			pos = []
			for x, j in enumerate(z_matrix):
				if j == i:
					pos.append(x)
					m = Motif()
					m.id = motif[x].id
					m.sequence = motif[x].sequence
					m.structure = motif[x].structure
					m.shape = shape
					m.positions = motif[x].positions
					self.new_motifs[i].append(m)
			self.distances[i] = self.median_distance(pos, matrix)

	def median_distance(self, pos, matrix):
		columns = matrix[pos, :][:, pos]
		columns[np.tril_indices(columns.shape[0], -1)] = np.nan
		triled_matrix = columns
		np.fill_diagonal(triled_matrix, 'nan')
		if triled_matrix != []:
			return np.round(np.nanmax(triled_matrix), 2)
		else:
			return -1
