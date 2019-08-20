from LEX_ply import tokens, lexer
import ply.yacc as yacc
file = open("out.tex","w")
start='init'
def p_init(p):
    'init : document'
def p_document(p):
    'document : HTML_O head body HTML_E'
    file.write("\\documentclass{article}\n")
    file.write(p[2])
    file.write(p[3]+'\n')
    file.write("\\end{document}")

def p_head(p):
    'head : HEAD_O TITLE_O STRING TITLE_E HEAD_E'
    p[0]="\\title{"+p[3]+"}\n\\begin{document}\n\\maketitle\n"

def p_body(p):
    'body : BODY_O H1_O STRING H1_E BODY_E'
    p[0]=p[3]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

html='''
<html>
<head>
<title>Het12Patel DEMO leX1</title>
</head>
<body>
<h1>This is my heading</h1>
</body>
</html>
'''
parser.parse(html)
