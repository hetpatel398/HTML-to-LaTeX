"""
    document : HTML_O head body HTML_E
    head : HEAD_O head_data HEAD_E
    head_data : head_data TITLE_O STRING TITLE_E head_data | empty
"""

from LEX_ply import tokens, lexer
import ply.yacc as yacc
file = open("../tex/out.tex","w")
start='document'

def p_document(p):
    'document : HTML_O head body HTML_E'
    file.write("\\documentclass{article}\n")
    file.write("\\usepackage{hyperref}\n")
    file.write("\\usepackage{comment}\n")
    file.write('\\usepackage[utf8]{inputenc}')
    file.write('\\usepackage[T1]{fontenc}')
    file.write('\\usepackage{enumitem}')

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
    p[0]=p[1]+"\\href{"+p[2][1]['href']+"}{"+p[3]+"}"+p[5]
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
        p[0] = p[1]+"\n\\newline\n"+p[3]
    else:
        p[0] = p[1]+"\n\\newline\n"+p[4]

def p_p(p):
    '''body_data : body_data P_O body_data P_E data'''
    p[0] = p[1]+"\n\\par\n"+p[3]+"\n"+p[5]

def p_H1(p):
    'body_data : body_data H1_O body_data H1_E data'
    p[0]=p[1]+"\n\\section{"+p[3]+"}\n"+p[5]

def p_H2(p):
    'body_data : body_data H2_O body_data H2_E data'
    p[0]=p[1]+"\n\\section{"+p[3]+"}\n"+p[5]

def p_H3(p):
    'body_data : body_data H3_O body_data H3_E data'
    p[0]=p[1]+"\n\\subsection{"+p[3]+"}\n"+p[5]

def p_H4(p):
    'body_data : body_data H4_O body_data H4_E data'
    p[0]=p[1]+"\n\\subsubsection{"+p[3]+"}\n"+p[5]

def p_ordered_list(p):
    'body_data : body_data OL_O body_data OL_E data'
    p[0]=p[1]+"\n\\begin{enumerate}"+p[3]+"\n\\end{enumerate}\n"+p[5]

def p_unordered_list(p):
    'body_data : body_data UL_O body_data UL_E data'
    p[0]=p[1]+"\n\\begin{itemize}"+p[3]+"\n\\end{itemize}\n"+p[5]

def p_list_items(p):
    'body_data : body_data LI_O body_data LI_E data'
    p[0]=p[1]+"\n\\item "+p[3]+"\n"+p[5]

def p_dl(p):
    'body_data : body_data DL_O body_data DL_E data'
    p[0]=p[1]+'\\begin{description}[style=unboxed, labelwidth=\\linewidth, font =\\sffamily\\itshape\\bfseries, listparindent =0pt, before =\\sffamily]'\
         +p[3]+'\\end{description}\n'+p[5]

def p_dt(p):
    'body_data : body_data DT_O body_data DT_E data'
    p[0]=p[1]+'\\item['+p[3]+']\n'+p[5]

def p_dd(p):
    'body_data : body_data DD_O body_data DD_E data'
    p[0]=p[1]+'\n'+p[3]+'\n'+p[5]

def p_div(p):
    'body_data : body_data DIV_O body_data DIV_E data'
    p[0]=p[1]+'\n'+p[3]+'\n'+p[5]

def p_u(p):
    'body_data : body_data U_O body_data U_E data'
    p[0]=p[1]+'\\underline{'+p[3]+'}\n'+p[5]

def p_b(p):
    '''body_data : body_data B_O body_data B_E data
                 | body_data STRONG_O body_data STRONG_E data'''
    p[0]=p[1]+'\\textbf{'+p[3]+'}\n'+p[5]

def p_i(p):
    'body_data : body_data I_O body_data I_E data'
    p[0]=p[1]+'\\textit{'+p[3]+'}\n'+p[5]

def p_em(p):
    'body_data : body_data EM_O body_data EM_E data'
    p[0]=p[1]+'\\{em '+p[3]+'}\n'+p[5]

def p_tt(p):
    'body_data : body_data TT_O body_data TT_E data'
    p[0]=p[1]+'\\textt{'+p[3]+'}\n'+p[5]

def p_small(p):
    'body_data : body_data SMALL_O body_data SMALL_E data'
    p[0]=p[1]+"\n{\\fontsize{8}{9}\selectfont "+p[3]+"}\n"+p[5]

def p_comment(p):
    'body_data : body_data COMMENT data'
    p[0]=p[1]+"\n\\begin{comment}\n"+p[2]+"\n\\end{comment}\n"+p[3]

def p_body_data_data(p):
    'body_data : data'
    p[0]=p[1]

def p_data(p):
    '''data : STRING
            | empty
    '''
    p[0]=p[1]
# def p_body_data_star(p):
#     'body_data : body_data body_data'
#     p[0]=p[1]+p[2]
#
# def p_body_data_empty(p):
#     'body_data : empty'
#     p[0]=""

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

html='''<html>
<head>
<title>Het12Patel DEMO leX1</title>
</head>
<body>
<h1>This is my heading</h1>
<h3>This is subsection</h3>
<h4>This is subsubsection</h4>
<a href='http://www.het.com'>Het_title</a>
<p>before<!-- little comment: <p>&#x03C0; &#960;--> </p><br>font<font size="11">HET in Font size 10</font>after font<br /><br>
<center><a href='http://www.google.com'>Google in center</a></center>
<ul>
     <li> ... Level one, number one...</li>
     <ol>
        <li> ... Level two, number one...</li>
        <li> ... Level two, number two...</li>
        <ol>
           <li> ... Level three, number one...</li>
        </ol>
        <li> ... Level two, number three...</li>
     </ol>
     <li> ... Level one, number two...</li>
</ul>
<!-- little comment: <p>&#x03C0; &#960;</p> -->

<dl>
<h1>hi</h1>
  <u><dt><a href="https://google.com/home">Coffee</a></dt>
  <dd>Black hot drink</dd></u>
  <dt>Milk</dt>
  <dd>White cold drink</dd>
</dl>
 <p>
    <div>Div line 1. </div>
    <div>Div line 2. </div>
    <div>Div line 3</div>
 </p>
</body>
</html>
'''
parser.parse(html)
file.close()
