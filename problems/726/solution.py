class Solution:
    def is_digit(self, char):
        return "0" <= char <= "9"

    def is_upper(self, char):
        return "A" <= char <= "Z"

    def is_lower(self, char):
        return "a" <= char <= "z"

    def stack_element_count(self, atoms):
        atom_counts = list()

        for atom in atoms:
            if len(atom) == 1:
                atom_counts.append((atom[0:2], len(atom)))
                continue

            a1 = ord(atom[0])
            a2 = ord(atom[1])
            if (a1 >= 65 and a1 <= 91) and (a2 >= 97 and a2 <= 123):
                alen = 2
                sym = atom[0:2]
            else:
                alen = 1
                sym = atom[0]

            atom_counts.append((sym, len(atom) // alen))

        return atom_counts

    def make_atom_dict(self, atom_counts):
        unique_atoms = dict()

        for atom in atom_counts:
            unique_atoms[atom[0]] = unique_atoms.get(atom[0], 0) + atom[1]

        return unique_atoms

    def countOfAtoms(self, formula: str) -> str:
        atom_stack = list()
        n = len(formula)
        formula += " "

        i = 0
        while i < n:
            ascii_val = ord(formula[i])
            if formula[i] == "(":
                atom_stack.append(formula[i])
            elif self.is_upper(formula[i]):
                atom_stack.append(formula[i])
            elif self.is_lower(formula[i]):
                atom_stack[-1] += formula[i]
            elif self.is_digit(formula[i]):
                mul = 0
                while self.is_digit(formula[i]):
                    mul = mul * 10 + int(formula[i])
                    i += 1
                    if i == n:
                        break
                i -= 1
                atom_stack[-1] *= mul
            elif formula[i] == ")":
                mul = 0
                while self.is_digit(formula[i + 1]):
                    mul = mul * 10 + int(formula[i + 1])
                    i += 1
                    if i == n - 1:
                        break
                if mul == 0:
                    mul = 1

                temp = list()
                while atom_stack[-1] != "(":
                    temp.append(atom_stack.pop() * mul)
                atom_stack.pop()
                while temp:
                    atom_stack.append(temp.pop())
            i += 1

        atom_counts = self.stack_element_count(atom_stack)
        atom_dict = self.make_atom_dict(atom_counts)
        for k, v in atom_dict.items():
            if v == 1:
                atom_dict[k] = ""
            else:
                atom_dict[k] = str(v)
        return "".join(sorted(map("".join, atom_dict.items())))
