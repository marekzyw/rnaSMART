
lvl = 5


class Structure:
    def __init__(self):
        self.shape = ""
        self.bracket = ""
        self.shape_position = {}
        self.shape_position_hairpins = []

    def find_bracket(self, p):
        c_o = 0
        x = 0
        if self.bracket[p] == "(":
            for i in range(p, len(self.bracket)):
                if self.bracket[i] == "(":
                    c_o += 1
                elif self.bracket[i] == ")":
                    c_o = c_o - 1
                if c_o == 0:
                    x = i
                    break
        elif self.bracket[p] == ")":
            for i in list(reversed(range(0, p + 1))):
                if self.bracket[i] == ")":
                    c_o += 1
                elif self.bracket[i] == "(":
                    c_o -= 1
                if c_o == 0:
                    x = i
                    break
        return x

    def new_stem(self, a, b, a_p, b_p):
        sep = False
        for i in range(a, b + 1):
            if self.bracket[i] != ".":
                if self.bracket[i] != self.bracket[a]:
                    sep = True
                    break
        if sep is False and lvl == 4:
            m = False
            n = False
            for j in range(a, b):
                if self.bracket[j] == ".":
                    m = True
                    break
            for j in range(a_p, b_p):
                if self.bracket[j] == ".":
                    n = True
            if m is True and n is True:
                sep = True

        return sep

    def bracket_to_shape(self):
        beg = False
        cl = False
        prev_i = 0
        for i in range(0, len(self.bracket)):
            if self.bracket[i] == "(":
                if beg is False:
                    self.shape += "["
                    self.shape_position[len(self.shape) - 1] = [i]
                    beg = True
                    self.shape_position_hairpins.append(i)
                elif beg is True:
                    akt_pair = self.find_bracket(i)
                    prev_pair = self.find_bracket(prev_i)
                    if self.new_stem(akt_pair, prev_pair, prev_i, i) is True:
                        self.shape_position[len(self.shape) - 1].append(prev_i)
                        self.shape += "["
                        self.shape_position[len(self.shape) - 1] = [i]
                        self.shape_position_hairpins.append(i)
                        beg = True
                if cl is True:
                    cl = False
                    self.shape_position[len(self.shape) - 2].append(prev_i)
                    self.shape_position_hairpins.append(prev_i)
            elif self.bracket[i] == ")":
                if beg is True:
                    beg = False
                    self.shape_position[len(self.shape) - 1].append(prev_i)
                if cl is False:
                    self.shape += "]"
                    self.shape_position[len(self.shape) - 1] = [i]
                    cl = True
                elif cl is True:
                    akt_pair = self.find_bracket(i)
                    prev_pair = self.find_bracket(prev_i)
                    if self.new_stem(akt_pair, prev_pair, prev_i, i) is True:
                        self.shape_position[len(self.shape) - 1].append(prev_i)
                        self.shape_position_hairpins.append(prev_i)
                        self.shape += "]"
                        self.shape_position[len(self.shape) - 1] = [i]
                        cl = True
            if self.bracket[i] != ".":
                prev_i = i
        self.shape_position[len(self.shape) - 1].append(prev_i)
        self.shape_position_hairpins.append(prev_i)
        self.shape_position_hairpins.sort()
