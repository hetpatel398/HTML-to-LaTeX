class Node:
    def __init__(self,type,attributes={},children=[]):
        self.type=type
        self.attributes=attributes
        self.children=children



    def __repr__(self):
        s='(%s,%s,%s)'%(self.type, str(self.attributes), str(self.children))
        return s

    def add_children(self, list_of_children):
        self.children=self.children+list_of_children

    def traverse(self):
        print(self.type)
        if self.children!=[]:
            for child in self.children:
                child.traverse()

    # def createLatexFile(self):
    #
    #     def traverse_html(node):
    #         node.file.write("\\documentclass{article}\n")
    #         node.file.write("\\usepackage{hyperref}\n")
    #         node.file.write("\\usepackage{comment}\n")
    #         node.file.write('\\usepackage[utf8]{inputenc}')
    #         node.file.write('\\usepackage[T1]{fontenc}')
    #         node.file.write('\\usepackage{enumitem}')
    #         node.file.write('\\usepackage{graphicx}')
    #         for child in node.children:
    #             child.createLatexFile()
    #         node.file.write('\\end{document}')
    #
    #
    #     def traverse_head(node):
    #         for child in node.children:
    #             child.createLatexFile()
    #         node.file.write("\\begin{document}\n")
    #         node.file.write("\\maketitle\n")
    #
    #     def traverse_title(self):
    #         None
    #     def traverse_body(self):
    #         None
    #     def traverse_p(self):
    #         None
    #     def traverse_center(self):
    #         None
    #     def traverse_string(self):
    #         None
    #     switcher={
    #         'HTML':traverse_html,
    #         'HEAD':traverse_head,
    #         'TITLE':traverse_title,
    #         'BODY':traverse_body,
    #         'P':traverse_p,
    #         'CENTER':traverse_center,
    #         'STRING':traverse_string
    #     }
    #
    #     func=switcher.get(self.type)
    #     func(self)
    #     # for child in self.children:
    #     #     child.createLatexFile()

# p=Node('HTML')
# p.createLatexFile()
# p=Node('p')
# body=Node('body')
# # print(body.children.append(body))
# print(body)
# html=Node('html')
# html.add_children([p])
# # body.add_children([p])
# print(html)
