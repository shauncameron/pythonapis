import re


class Token:

    def __repr__(self):

        if type(self.value) == str:

            value = self.value.replace('\n', '$NEWLINE')

        else:

            value = self.value

        return f"""<TOKEN(type={self.token}, value='{value}')>"""

    def __init__(self, token, value):

        self.token = self.type = token
        self.value = value


class Lexer:

    def __init__(self, grammar_dictionary):

        self.grammar = grammar_dictionary
        self.tokens = {x: re.compile(y) for x, y in self.grammar.items()}

    def tokenize(self, string):

        tokens = []
        char = 0

        while len(string) and char < len(string):

            match = False
            for token, reg in self.tokens.items():

                if ma := reg.match(string):

                    match = True

                    matches = ma.groups()
                    if not len(matches): matches = ma.group()

                    string = reg.sub('', string)

                    tokens.append(Token(token, matches))
                    break

            if not match:

                echar = 0
                ematch = False
                nullstring = ''

                while not ematch and echar < len(string):

                    for token, reg in self.tokens.items():

                        if reg.match(string[echar:]):

                            ematch = True
                            break

                    if not ematch:

                        nullstring += string[echar]
                        echar += 1

                    else:
                        break

                tokens.append(Token('nullstring', nullstring))
                string = string[echar:]

        return tokens