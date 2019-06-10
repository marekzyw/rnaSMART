from additional_classes import Cluster
from scipy.cluster.hierarchy import linkage, fcluster
import numpy as np
import warnings
warnings.filterwarnings("ignore")


class SequenceClustering:
	def __init__(self):
		self.new_motifs = []

	def clustering_by_sequence(self, matrix, motif, distance, strukt_distance):
		z_matrix = fcluster(linkage(matrix, method='single'), distance, 'distance')
		for i in range(0, max(z_matrix)+1):
			sequences = []
			structures = []
			ids = []
			lengths = []
			positions = []
			for x, j in enumerate(z_matrix):
				if j == i:
					positions.append(x)
					ids.append(motif[x].id)
					sequences.append(motif[x].sequence)
					structures.append(motif[x].structure)
					lengths.append(len(motif[x].sequence))
			if len(ids) >= 2:
				matr = self.median_distance(positions, matrix)
				c = Cluster()
				c.count = len(ids)
				c.med_length = np.median(lengths)
				c.med_distance = matr
				c.struct_distance = strukt_distance
				c.ids = ids
				c.seqs = sequences
				c.structs = structures
				self.new_motifs.append(c)
		return self.new_motifs

	def median_distance(self, pos, matrix):
		columns = matrix[pos, :][:, pos]
		columns[np.tril_indices(columns.shape[0], -1)] = np.nan
		triled_matrix = columns
		np.fill_diagonal(triled_matrix, 'nan')
		return np.round(np.nanmax(triled_matrix), 2)

