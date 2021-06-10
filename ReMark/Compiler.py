
class Compiler:

    def __init__(self, tokens):

        self.tokens = tokens

    def compile(self):

        text = ''

        bold_open = False
        italics_open = False
        underline_open = False
        crossthrough_open = False
        code_open = False
        codeblock_open = False

        for i, token in enumerate(self.tokens):

            new_paragraph_open = True

            if token.type == 'newline':

                text += '<br/>'

            elif token.type == 'comment':

                text += '<a hidden>' + token.value[0] + '</a>'

            elif token.type == 'nullstring':

                text += '<a class="remark-nullstring">' + token.value + '</a>'

            elif token.type == 'hyperlink':

                text += '<a class="remark-hyperlink" style="color: blue;" href="' + token.value[1] + '">' + token.value[0] + '</a>'

            elif token.type == 'spoiler':

                text += '<details class="remark-spoiler-details"> <summary class="remark-spoiler-summary">' + token.value[0] + '</summary>' + token.value[1] + '</details>'

            elif token.type == 'imagelink':

                text += '<img class="remark-imagelink" style="max-width: 250px;max-height: 250px;" alt="' + token.value[0] + '" title=' + token.value[0] + '" src="' + token.value[1] + '"/>'

            # FONT

            elif token.type == 'bold':

                if not bold_open:

                    bold_open = True
                    text += '<b class="remark-bold">'

                else:

                    bold_open = False
                    text += '</b>'

            elif token.type == 'italics':

                if not italics_open:

                    italics_open = True
                    text += '<i class="remark-italics">'

                else:

                    italics_open = False
                    text += '</i>'

            elif token.type == 'underline':

                if not underline_open:

                    underline_open = True
                    text += '<u class="remark-underline">'

                else:

                    underline_open = False
                    text += '</u>'

            elif token.type == 'crossthrough':

                if not crossthrough_open:

                    crossthrough_open = True
                    text += '<s class="remark-crossthrough">'

                else:

                    crossthrough_open = False
                    text += '</s>'

            elif token.type == 'code':

                if not code_open:

                    code_open = True
                    text += '<code class="remark-code">'

                else:

                    code_open = False
                    text += '</code>'

            elif token.type == 'codeblock':

                if codeblock_open:

                    codeblock_open = False

                    text += '</div>'

                else:

                    codeblock_open = True

                    text += '<div class="remark-codeblock">'

            elif token.type == 'rule':

                text += '<hr/>'

            elif token.type == 'html':

                text += token.value[0].lstrip()

            elif token.type == 'css':

                text += '<style>' + token.value[0].lstrip() + '</style>'

            elif token.type == 'noremark':

                text += token.value[0].lstrip()

            elif token.type == 'colour':

                text += '<a style="color:#' + token.value[0] + ';">' + token.value[1] + '</a>'

        return text
