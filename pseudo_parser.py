# -*- coding: utf-8 -*-

import re


class Parser:
    def __init__(self, input_file):
        """
        :param input_file: path to .txt file with PseudoCode
        """
        self.input_file = input_file
        self.lines = self.read_input_file()
        self.pseudos = {"then": ":",
                        "[1...n]": " = [None] * (n-1)",
                        "<-": "=",
                        "do": ":",
                        ";": "",
                        "≥": ">=",
                        "≤": "<=",
                        "∧": "and",
                        "∨": "or",
                        "++": "+= 1",
                        "--": "-= 1",
                        "else if": "elif",
                        "/": "//",
                        "fi": "#fi",
                        "od": "do",
                        "Null": "None"}

    def read_input_file(self):
        lines = []
        with open(self.input_file) as f:
            txt_lines = list(f)
        lines += txt_lines
        return lines

    def make_out_file(self):
        with open("output_file.py", "w") as output_file:
            for line in self.lines:
                line = line.replace("\n", "")
                line = line.replace("=", "==")
                line = line.replace("//", "#")
                if re.match(r"[A-Za-z]_i = \d", line):
                    index_number = re.match(r"[A-Za-z]_i = \d", line).group(0)
                    index_pseudo = re.findall(r"\d", str(index_number))[0]
                    index_python = int(index_pseudo) - 1
                    line = line.replace(index_pseudo, str(index_python))
                if re.match(r"[A-Z] <-> [A-Z]", line):
                    lists = re.findall(r"[A-Z]", line)
                    line = lists[0] + "," + lists[1] + " = " + lists[1] + "," + lists[0]
                for sign in self.pseudos.keys():
                    line = line.replace(sign, self.pseudos[sign])
                output_file.write(line + "\n")


if __name__ == '__main__':
    parser = Parser(input_file="input_file.txt")
    parser.make_out_file()
