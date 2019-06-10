class Cluster:
    def __init__(self):
        self.count = 0
        self.med_length = 0.0
        self.med_distance = 0.0
        self.struct_distance = 0.0
        self.ids = []
        self.seqs = []
        self.structs = []
        self.parent = []
        self.motif_id = 0
        self.alignment = {}
        self.id_line = ""


class Hairpin:
    def __init__(self):
        self.start = 0
        self.stop = 0


class Motif:
    def __init__(self):
        self.id = ""
        self.shape = ""
        self.sequence = ""
        self.structure = ""
        self.positions = []
        self.stems_len = []


class StructureInfo:
    def __init__(self):
        self.sequence_id = ""
        self.sequence = ""
        self.structure = ""
        self.shape = ""
        self.positions = []
        self.stems_len = {}
