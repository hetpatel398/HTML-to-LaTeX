file = open("../tex/out_ast.tex","w")

def createLatexFile(self):

    def traverse_html(node):
        file.write("\\documentclass{article}\n")
        file.write("\\usepackage{hyperref}\n")
        file.write("\\usepackage{comment}\n")
        file.write('\\usepackage[utf8]{inputenc}\n')
        file.write('\\usepackage[T1]{fontenc}\n')
        file.write('\\usepackage{enumitem}\n')
        file.write('\\usepackage{graphicx}\n')
        for child in node.children:
            createLatexFile(child)
        file.write('\\end{document}')


    def traverse_head(node):
        for child in node.children:
            createLatexFile(child)
        file.write("\\begin{document}\n")
        file.write("\\maketitle\n")

    def traverse_title(node):
        child=node.children[0] if 0 < len(node.children) else None
        file.write("\\title{"+child.value+"}\n") #if child!=None

    def traverse_body(node):
        for child in node.children:
            createLatexFile(child)

    def traverse_p(node):
        file.write("\\par\n")
        for child in node.children:
            createLatexFile(child)

    def traverse_center(node):
        file.write("\\begin{center}\n")
        for child in node.children:
            createLatexFile(child)
        file.write("\\end{center}\n")

    def traverse_string(node):
        file.write(node.attributes.get('value'))

    switcher={
        'HTML':traverse_html,
        'HEAD':traverse_head,
        'TITLE':traverse_title,
        'BODY':traverse_body,
        'P':traverse_p,
        'CENTER':traverse_center,
        'STRING':traverse_string
    }

    func=switcher.get(self.value)
    func(self)
    # for child in self.children:
    #     createLatexFile(child)
