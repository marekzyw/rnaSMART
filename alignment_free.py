import numpy as np
import itertools


class AlignmentFree:
	def __init__(self, seq, ids, length):
		self.sequences_list = seq
		self.headers_list = ids
		self.length = length
		self.seqs_number = 0
		self.result = []

	def main(self):
		occurrences_list = self.calculate_occurrences()
		self.seqs_number = occurrences_list.shape[0]
		self.result = self.euclidean(occurrences_list)

	def calculate_occurrences(self):
		d = self.get_motifs()
		rows_num = len(self.sequences_list)
		cols_num = len(d)
		data = np.zeros(shape=(rows_num, cols_num))
		for row_idx, sequence in enumerate(self.sequences_list):
			for i in range(0, len(sequence)-self.length+1):
				word = sequence[i:i+self.length]
				col_idx = d[word]
				data[row_idx, col_idx] += 1
		return data

	def get_motifs(self):
		(d, index) = ({}, 0)
		for sequence in self.sequences_list:
			for i in range(0, len(sequence)-self.length+1):
				word = sequence[i:i+self.length]
				if word not in d:
					d[word] = index
					index += 1
		return d

	def euclidean(self, occurrences_list):
		return self.minkowski(occurrences_list, 2)

	def minkowski(self, list_, exponent):
		matrix = np.zeros([self.seqs_number, self.seqs_number])
		for i, j in itertools.combinations(range(0, self.seqs_number), 2):
			matrix[i][j] = matrix[j][i] = (np.sum((np.absolute(list_[i, :] - list_[j, :]))**exponent))**(1.0/float(exponent))
		return matrix


if __name__ == '__main__':
	large_dataset_sizes = np.arange(1, 16) * 4000
	sequences = ["AC", '', '']
	identificators = ['>a', '>b', '>c']
	af = AlignmentFree(sequences, identificators, 2)
	af.main()
