"""
    document : HTML_O head body HTML_E
    head : HEAD_O head_data HEAD_E
    head_data : head_data TITLE_O STRING TITLE_E head_data | empty
"""

from LEX_ply import tokens, lexer
import ply.yacc as yacc
file = open("out.tex","w")
start='document'

def p_document(p):
    'document : HTML_O head body HTML_E'
    file.write("\\documentclass{article}\n")
    file.write("\\usepackage{hyperref}\n")
    file.write(p[2])
    file.write(str(p[3])+'\n')
    file.write("\\end{document}")

def p_empty(p):
     'empty :'
     p[0]=''

def p_head(p):
    'head : HEAD_O head_data HEAD_E'
    p[0]=p[2]+"\n\\begin{document}\n\\maketitle"

def p_head_data(p):
    'head_data : head_data TITLE_O STRING TITLE_E'
    p[0]=p[1]+"\\title{"+p[3]+"}"

def p_head_data_empty(p):
    'head_data : empty'
    p[0]=""

def p_body(p):
    'body : BODY_O body_data BODY_E'
    p[0]=p[2]

def p_a(p):
    'body_data : body_data A_O body_data A_E data'
    p[0]=p[1]+"\\href{"+p[2][1]['href']+"}{"+p[3]+"}\n"+p[5]
    # print(p[2])

def p_font(p):
    'body_data : body_data FONT_O body_data FONT_E data'
    p[0]=p[1]+"\n{\\fontsize{"+p[2][1]['size']+"}{"+str(int(int(p[2][1]['size'])*1.2))+"}\selectfont "+p[3]+"}\n"+p[5]

def p_center(p):
    'body_data : body_data CENTER_O body_data CENTER_E data'
    p[0] = p[1]+"\n\\centerline{"+p[3]+"}\n"+p[5]

def p_br(p):
    '''body_data : body_data BR_S data
                 | body_data BR_O data
                 | body_data BR_O BR_E data'''
    if len(p) == 4:
        p[0] = p[1]+"\n\\newline"+p[3]
    else:
        p[0] = p[1]+"\n\\newline"+p[4]

def p_p(p):
    '''body_data : body_data P_O body_data P_E data'''
    p[0] = p[1]+"\n\\par\n"+p[3]+"\n"+p[5]

def p_H1(p):
    'body_data : body_data H1_O body_data H1_E data'
    p[0]=p[1]+"\n\\section{"+p[3]+"}\n"+p[5]

def p_body_data_data(p):
    'body_data : data'
    p[0]=p[1]

def p_data(p):
    '''data : STRING
            | empty
    '''
    p[1]=p[1]
    p[1]=p[1].replace('\\','\\\\')
    p[1]=p[1].replace('_','\_')
    p[1]=p[1].replace('#','\#')
    p[1]=p[1].replace('%','\%')
    p[1]=p[1].replace('~','\~')
    p[1]=p[1].replace('^','\^')
    p[1]=p[1].replace('{','\{')
    p[1]=p[1].replace('}','\}')
    p[0]=p[1]
# def p_body_data_star(p):
#     'body_data : body_data body_data'
#     p[0]=p[1]+p[2]

def p_body_data_empty(p):
    'body_data : empty'
    p[0]=""

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
<a href='http://www.het.com'>Het_title</a>
<p>beforefont<font size="11">HET in Font size 10</font>after font<br /><br></p>
<center><a href='http://www.google.com'>Google in center</a></center>
</body>
</html>
'''
parser.parse(html)
file.close()
