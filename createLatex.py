file = open("../tex/out_ast.tex","w")

def mapHTMLastToLATEXast(root):
    mapper={
        'HTML':'doucumentStart',
        'HEAD':'head',
        'TITLE':'title',
        'BODY':'begin_document',
        'A':'href',
        'FONT':'fontsize',
        'CENTER':'center',
        'BR':'newline',
        'P':'par',
        'H1':'section',
        'H2':'subsection',
        'H3':'subsubsection',
        'H4':'paragraph_bold',
        'H5':'paragraph_bold',
        'H6':'paragraph_bold',
        'OL':'enumerate',
        'UL':'itemize',
        'LI':'item_lst',
        'DL':'description',
        'DT':'item',
        'DD':'dataString',
        'DIV':'divString',
        'U':'underline',
        'B':'textbf',
        'I':'textit',
        'EM':'em',
        'TT':'textt',
        'SMALL':'fontsize4',
        'SUB':'sub',
        'SUP':'sup',
        'GREEK':'greek',
        'IMG':'includegraphics',
        'FIGURE':'figure',
        'FIGCAPTION':'caption',
        'TABLE':'table',
        'CAPTION':'table_caption',
        'FIRSTROW':'first_row',
        'TH':'heading',
        'TD':'column',
        'TR':'row',
        'COMMENT':'comment',
        'STRING':'string'
    }
    root.type=mapper.get(root.type)
    for i in range(len(root.children)):
        root.children[i]=mapHTMLastToLATEXast(root.children[i])
    return root

def createLatexFileFromLatexAst(node):


    def traverse_documentStart(node):
        file.write("\\documentclass{article}\n")
        file.write("\\usepackage{hyperref}\n")
        file.write("\\usepackage{comment}\n")
        file.write('\\usepackage[utf8]{inputenc}\n')
        file.write('\\usepackage[T1]{fontenc}\n')
        file.write('\\usepackage{enumitem}\n')
        file.write('\\usepackage{graphicx}\n')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('\\end{document}')

    def traverse_head(node):
        for child in node.children:
            createLatexFileFromLatexAst(child)

    def traverse_title(node):
        child=node.children[0] if 0 < len(node.children) else None
        if child!=None:
            file.write("\\title{"+child.attributes.get('value')+"}\n")

    def traverse_begin_document(node):
        file.write("\\begin{document}\n")
        file.write("\\maketitle\n")
        for child in node.children:
            createLatexFileFromLatexAst(child)

    def traverse_href(node):
        file.write('\\href{%s}{'%(node.attributes.get('href')))
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_fontsize(node):
        size=node.attributes.get('size')
        file.write("{\\fontsize{"+size+"}{"+str(int(int(size)*1.2))+"}\selectfont ")
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_center(node):
        file.write('\\begin{center}')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('\\end{center}')

    def traverse_newline(node):
        file.write('\\newline')

    def traverse_par(node):
        print('in par')
        file.write('\\par')
        for child in node.children:
            createLatexFileFromLatexAst(child)

    def traverse_section(node):
        file.write('\\section{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_subsection(node):
        file.write('\\subsection{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_subsubsection(node):
        file.write('\\subsubsection{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_paragraph_bold(node):
        file.write('\\par \\textbf{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_enumerate(node):
        file.write('\\begin{enumerate}')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('\\end{enumerate}')

    def traverse_itemize(node):
        file.write('\\begin{itemize}')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('\\end{itemize}')

    def traverse_item_lst(node):
        file.write('\\item')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('\n')

    def traverse_description(node):
        file.write('\\begin{description}[style=unboxed, labelwidth=\\linewidth, font =\\sffamily\\itshape\\bfseries, listparindent =0pt, before =\\sffamily]')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('\\end{description}')

    def traverse_item(node):
        file.write('\\item[')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write(']')

    def traverse_dataString(node):
        for child in node.children:
            createLatexFileFromLatexAst(child)

    def traverse_divString(node):
        for child in node.children:
            createLatexFileFromLatexAst(child)

    def traverse_underline(node):
        file.write('\\underline{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_textbf(node):
        file.write('\\textbf{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_textit(node):
        file.write('\\textit{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_em(node):
        file.write('\\emph{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_textt(node):
        file.write('\\textt{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_fontsize4(node):
        # print("in small")
        file.write("{\\fontsize{4}{4}\selectfont ")
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_sub(node):
        file.write("_{")
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_sup(node):
        file.write("^{")
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    def traverse_greek(node):
        file.write('\\'+node.attributes.get('symbol'))

    def traverse_includegraphics(node):
        width = node.attributes.get('width')
        height = node.attributes.get('height')
        src = node.attributes.get('src')
        if (width == None and height==None):
            file.write("\includegraphics{"+src+"}")
        elif (width != None and height!=None):
            file.write("\includegraphics[width="+width+", height="+height+"]{"+src+"}")
        elif (width != None and height==None):
            file.write("\includegraphics[width="+width+"]{"+src+"}")
        elif (width == None and height!=None):
            file.write("\includegraphics[height="+height+"]{"+src+"}")

    def traverse_figure(node):
        file.write('\\begin{figure}[h!]')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('end{figure}')

    def traverse_caption(node):
        file.write('\\caption{')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('}')

    # 'table':traverse_table,
    # 'table_caption':traverse_table_caption,
    # 'first_row':traverse_first_row,
    # 'heading':traverse_heading,
    # 'column':traverse_column,
    # 'row':traverse_row,

    def traverse_comment(node):
        file.write('\\begin{comment}')
        for child in node.children:
            createLatexFileFromLatexAst(child)
        file.write('end{figure}')

    def traverse_string(node):
        file.write(node.attributes.get('value'))

    switcher={
        'doucumentStart':traverse_documentStart,
        'head':traverse_head,
        'title':traverse_title,
        'begin_document':traverse_begin_document,
        'href':traverse_href,
        'fontsize':traverse_fontsize,
        'center':traverse_center,
        'newline':traverse_newline,
        'par':traverse_par,
        'section':traverse_section,
        'subsection':traverse_subsection,
        'subsubsection':traverse_subsubsection,
        'paragraph_bold':traverse_paragraph_bold,
        # 'subparagraph_bold':traverse_subparagraph_bold,
        # 'subsubparagraph_bold':traverse_subsubparagraph_bold,
        'enumerate':traverse_enumerate,
        'itemize':traverse_itemize,
        'item_lst':traverse_item_lst,
        'description':traverse_description,
        'item':traverse_item,
        'dataString':traverse_dataString,
        'divString':traverse_divString,
        'underline':traverse_underline,
        'textbf':traverse_textbf,
        'textit':traverse_textit,
        'em':traverse_em,
        'textt':traverse_textt,
        'fontsize4':traverse_fontsize4,
        'sub':traverse_sub,
        'sup':traverse_sup,
        'greek':traverse_greek,
        'includegraphics':traverse_includegraphics,
        'figure':traverse_figure,
        'caption':traverse_caption,
        # 'table':traverse_table,
        # 'table_caption':traverse_table_caption,
        # 'first_row':traverse_first_row,
        # 'heading':traverse_heading,
        # 'column':traverse_column,
        # 'row':traverse_row,
        'comment':traverse_comment,
        'string':traverse_string
    }

    func=switcher.get(node.type)
    func(node)

# def createLatexFile_from_HTMLast(self):
#
#     def traverse_html(node):
#         file.write("\\documentclass{article}\n")
#         file.write("\\usepackage{hyperref}\n")
#         file.write("\\usepackage{comment}\n")
#         file.write('\\usepackage[utf8]{inputenc}\n')
#         file.write('\\usepackage[T1]{fontenc}\n')
#         file.write('\\usepackage{enumitem}\n')
#         file.write('\\usepackage{graphicx}\n')
#         for child in node.children:
#             createLatexFile_from_HTMLast(child)
#         file.write('\\end{document}')
#
#
#     def traverse_head(node):
#         for child in node.children:
#             createLatexFile_from_HTMLast(child)
#
#     def traverse_title(node):
#         child=node.children[0] if 0 < len(node.children) else None
#         file.write("\\title{"+child.attributes.get('value')+"}\n") #if child!=None
#
#     def traverse_body(node):
#         file.write("\\begin{document}\n")
#         file.write("\\maketitle\n")
#         for child in node.children:
#             createLatexFile_from_HTMLast(child)
#
#     def traverse_p(node):
#         file.write("\\par\n")
#         for child in node.children:
#             createLatexFile_from_HTMLast(child)
#
#     def traverse_center(node):
#         file.write("\\begin{center}\n")
#         for child in node.children:
#             createLatexFile_from_HTMLast(child)
#         file.write("\\end{center}\n")
#
#     def traverse_string(node):
#         file.write(node.attributes.get('value'))
#
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
    # for child in self.children:
    #     createLatexFile(child)
