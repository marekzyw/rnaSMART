import os
from subprocess import check_output
import shutil


class Alignment:
    def __init__(self, fasta, path, thread_num):
        self.fasta_to_aln = fasta
        self.path = path
        self.fasta_ids = []
        self.aln_dict = {}
        self.structure = ""
        self.ident = str(thread_num)
        self.out_file = ""

    def write_aln_fasta(self):
        with open(os.path.join("aln_fasta_" + self.ident + ".fa"), 'w') as output:
            output.write(self.fasta_to_aln)
        self.run_alignment()

    def run_alignment(self):
        p = check_output(['java', '-jar', 'foursale.jar',
                          '-in', os.path.join("aln_fasta_" + self.ident + ".fa"),
                          '-out', os.path.join("aln_fasta_out_" + self.ident + ".txt")])
        shutil.rmtree(os.path.join("aln_fasta_" + self.ident + ".out"), ignore_errors=True)
        self.out_file = os.path.join("aln_fasta_out_" + self.ident + ".txt")
        os.remove(os.path.join("aln_fasta_" + self.ident + ".fa"))

    def parse_alignment_result_locarna(self, aln_result):

        aln_result_tab = str(aln_result).split('\\n')  # python 3
        id = 0
        for i in range(len(aln_result_tab)):
            if aln_result_tab[i].startswith(self.fasta_ids[id][1:]):
                if self.fasta_ids[id] in self.aln_dict:
                    self.aln_dict[self.fasta_ids[id]] += aln_result_tab[i].split()[1]
                else:
                    self.aln_dict[self.fasta_ids[id]] = aln_result_tab[i].split()[1]
                id += 1
                if id == len(self.fasta_ids):
                    id = 0
            if aln_result_tab[i].startswith("alifold"):
                self.structure += aln_result_tab[i].split()[1]
                t = i + 1
                while "(" in aln_result_tab[t] or ")" in aln_result_tab[t] or "." in aln_result_tab[t]:
                    self.structure += aln_result_tab[t].strip().split(" ")[0]
                    t += 1
