################################################ YACC FILE IMPLEMENTATION IN PLY ################################################
########################################################### HET PATEL ###########################################################
########################################################## 2019MCS2562 ##########################################################
########################################################### IIT DELHI ###########################################################

from LEX_ply_v2 import tokens, lexer
import ply.yacc as yacc
file = open("../tex/out.tex","w")
start='document'

def p_empty(p):
     'empty :'
     p[0]=''

def p_document(p):
    '''
    document : doctype HTML_O head body HTML_E
             | empty
    '''
    if len(p)==6:
        file.write("\\documentclass{article}\n")
        file.write("\\usepackage{hyperref}\n")
        file.write("\\usepackage{comment}\n")
        file.write('\\usepackage[utf8]{inputenc}')
        file.write('\\usepackage[T1]{fontenc}')
        file.write('\\usepackage{enumitem}')
        file.write('\\usepackage{graphicx}')
        l=len(p)
        if l==6:
            file.write(p[3])
            file.write(p[4]+'\n')
            file.write("\\end{document}")
        elif l==5:
            file.write(p[2])
            file.write(p[3]+'\n')
            file.write("\\end{document}")
        elif l==4:
            file.write(p[2]+'\n')
            file.write("\\end{document}")
        else:
            file.write("\\n\\end{document}")
    else:
        p[0]=''

def p_doctype(p):
    '''
    doctype : DOCTYPE
            | empty
    '''
    p[0]=''

def p_head(p):
    '''
    head : HEAD_O head_data HEAD_E
         | empty
    '''
    if len(p)==4:
        p[0]=p[2]+"\n\\begin{document}\n\\maketitle"
    else:
        p[0]=''

def p_head_data(p):
    'head_data : head_data TITLE_O STRING TITLE_E'
    p[0]=p[1]+"\\title{"+p[3]+"}"

def p_head_data_meta(p):
    'head_data : head_data META_O'
    name=p[2][1].get('name')
    if name=='author':
        author_name=p[2][1].get('content')
        p[0]=p[1]+"\\author{"+author_name+"}"
    else:
        p[0]=''

def p_head_data_empty(p):
    'head_data : empty'
    p[0]=""

def p_body(p):
    '''
    body : BODY_O body_data BODY_E
         | empty
    '''
    if len(p)==4:
        p[0]=p[2]
    else:
        p[0]=''

def p_a(p):
    'body_data : body_data A_O body_data A_E data'
    p[0]=p[1]+"\\href{"+str(p[2][1].get('href'))+"}{"+p[3]+"}"+p[5]
    # print(p[2])

def p_font(p):
    'body_data : body_data FONT_O body_data FONT_E data'
    p[0]=p[1]+"\n{\\fontsize{"+p[2][1]['size']+"}{"+str(int(int(p[2][1]['size'])*1.2))+"}\selectfont "+p[3]+"}\n"+p[5]

def p_center(p):
    'body_data : body_data CENTER_O body_data CENTER_E data'
    p[0] = p[1]+"\n\\begin{center}"+p[3]+"\\end{center}\n"+p[5]

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
    p[0]=p[1]+"\n{\\fontsize{4}{5}\selectfont "+p[3]+"}\n"+p[5]

def p_sub(p):
    'body_data : body_data SUB_O body_data SUB_E data'
    p[0]=p[1]+"\_{"+p[3]+"}"+p[5]

def p_sup(p):
    'body_data : body_data SUP_O body_data SUP_E data'
    p[0]=p[1]+"\^{"+p[3]+"}"+p[5]

def p_special_greek_symbol(p):
    'body_data : body_data GREEK_SPECIAL_SYMBOL data'
    # print(p[2])
    p[0]=p[1]+" \\"+p[2]+" "+p[3]

def p_img(p):
    '''body_data : body_data IMG_S data
                 | body_data IMG_O data
                 | body_data IMG_O IMG_E data
    '''
    width = p[2][1].get('width')
    height = p[2][1].get('height')
    src = p[2][1].get('src')
    if len(p) ==4:
        if (width == None and height==None):
            p[0]=p[1]+"\includegraphics{"+src+"}"+p[3]
        elif (width != None and height!=None):
            p[0]=p[1]+"\includegraphics[width="+width+", height="+height+"]{"+src+"}"+p[3]
        elif (width != None and height==None):
            p[0]=p[1]+"\includegraphics[width="+width+"]{"+src+"}"+p[3]
        elif (width == None and height!=None):
            p[0]=p[1]+"\includegraphics[height="+height+"]{"+src+"}"+p[3]
    elif len(p)==5:
        if (width == None and height==None):
            p[0]=p[1]+"\includegraphics{"+src+"}"+p[4]
        elif (width != None and height!=None):
            p[0]=p[1]+"\includegraphics[width="+width+", height="+height+"]{"+src+"}"+p[4]
        elif (width != None and height==None):
            p[0]=p[1]+"\includegraphics[width="+width+"]{"+src+"}"+p[4]
        elif (width == None and height!=None):
            p[0]=p[1]+"\includegraphics[height="+height+"]{"+src+"}"+p[4]

def p_figure(p):
    'body_data : body_data FIGURE_O fig_data FIGURE_E data'
    p[0]=p[1]+"\\begin{figure}[h!]\n"+p[3]+"\\end{figure}\n"+p[5]

def p_fig_data_img(p):
    '''
    fig_data : fig_data IMG_O
             | fig_data IMG_S
             | fig_data IMG_O IMG_E
    '''
    width = p[2][1].get('width')
    height = p[2][1].get('height')
    src = p[2][1].get('src')
    if (width == None and height==None):
        p[0]=p[1]+"\includegraphics{"+src+"}\n"
    elif (width != None and height!=None):
        p[0]=p[1]+"\includegraphics[width="+width+", height="+height+"]{"+src+"}\n"
    elif (width != None and height==None):
        p[0]=p[1]+"\includegraphics[width="+width+"]{"+src+"}\n"
    elif (width == None and height!=None):
        p[0]=p[1]+"\includegraphics[height="+height+"]{"+src+"}\n"

def p_figcaption(p):
    'fig_data : fig_data FIGCAPTION_O body_data FIGCAPTION_E'
    p[0]=p[1]+"\\caption{"+p[3]+"}\n"

def p_fig_data_empty(p):
    'fig_data : empty'
    p[0]=''

def p_table(p):
    '''
    body_data : body_data TABLE_O caption table_data TABLE_E data
              | body_data TABLE_O table_data TABLE_E data
    '''
    if len(p) == 6:
        p[0]=p[1]+p[3]+p[5]
    else:
        p[0]=p[1]+p[3]+p[4]+p[6]

def p_caption(p):
    'caption : CAPTION_O body_data CAPTION_E'
    p[0]=p[2]

def p_table_data(p):
    '''
    table_data : first_row rows
               | empty
    '''
    if len(p) == 3:
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_first_row(p):
    'first_row : TR_O td_or_th TR_E'
    p[0]=p[2]

def p_td_or_th(p):
    '''
    td_or_th : td_or_th TD_O body_data TD_E
             | td_or_th TH_O body_data TH_E
             | empty
    '''
    if len(p)==5:
        p[0]=p[1]+p[3]
    else:
        p[0]=''

def p_rows(p):
    '''
    rows : rows TR_O cols TR_E
         | empty
    '''
    if len(p) == 5:
        p[0]=p[1]+p[3]
    else:
        p[0]=''

def p_cols(p):
    '''
    cols : cols TD_O body_data TD_E
         | empty
    '''
    if len(p) == 5:
        p[0]=p[1]+p[3]
    else:
        p[0]=''

def p_comment(p):
    'body_data : body_data COMMENT data'
    p[0]=p[1]+"\n\\begin{comment}\n"+p[2]+"\n\\end{comment}\n"+p[3]

def p_body_data_data(p):
    'body_data : data'
    p[0]=p[1]

def p_data(p):
    '''data : data STRING
            | data ANOTHER_STRING
            | empty
    '''
    if len(p)==3:
        p[0]=p[1]+p[2]
    else:
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
<figure>
  <figcaption>DEMO image</figcaption>
<img src="het.png" width='100' height="100"/>
</figure>
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
  <dt><a href="https://google.com/home">Coffee</a></dt>
  <dd>Black hot drink</dd>
  <dt>Milk</dt>
  <dd>White cold drink</dd>
</dl>
 <p>
    <div>Div line 1. </div>
    <div>Div line 2. </div>
    <div>Div line 3</div>
 </p>
<table border='1'>
    <tr>
        <td>1 1</td>
        <td>1 2</td>
        <td>1 3</td>
    </tr>
    <tr>
        <td>2 1</td>
        <td>2 2</td>
        <td>2 3</td>
    </tr>
    <tr>
        <td>3 1</td>
        <td>3 2</td>
        <td>3 3</td>
    </tr>
  </table>
</body>
</html>
'''

html='''
<!DOCTYPE HTML>
<html><head>
  <title>Sample document</title>
  <meta name='author' content='HET'>
  </head>
<body>


 <h1>CSS</h1>
  <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
 Nulla ut lectus id velit aliquet semper. Proin vitae erat. Duis metus. Nam
 vel nisl.Duis lobortis mi at lorem. Etiam ornare nibh quis eros. Nam magna
sem, adipiscing at,porttitor vitae, interdum vitae, elit. Sed turpis mi,
 tincidunt eget , euismod ac, molestie quis, wisi.
  </p>

  <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
 Nulla ut lectus id velit aliquet semper. Proin vitae erat. Duis metus. Nam
 vel nisl. Duis lobortis mi at lorem. Etiam ornare nibh quis eros. Nam magna
sem, adipiscing at, porttitor vitae, interdum vitae, elit. Sed turpis mi,
 tincidunt eget, euismod ac, molestie quis, wisi.
  </p>

  <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
 Nulla ut lectus id velit aliquet semper. Proin vitae erat. Duis metus. Nam
 vel nisl. Duis lobortis mi at lorem. Etiam ornare nibh quis eros. Nam magna
sem, adipiscing at, porttitor vitae, interdum vitae, elit. Sed turpis mi,
 tincidunt eget, euismod ac, molestie quis, wisi. Praesent nisl pede,
 hendrerit semper, accumsan ac, consequat id, nibh.</p>

  <p>Lorem ipsum dolor sit amet, consectetuer adipiscing.
 Nulla ut lectus id velit aliquet semper. Proin vitae erat. Duis
 vel nisl. Duis lobortis mi at lorem. Etiam ornare nibh quis eros.
sem, adipiscing at, porttitor vitae, interdum vitae, elit.</p>

 <p>
    </p><div>Div line 1. </div>
    <div>Div line 2. </div>
    <div>Div line 3</div>
 <p></p>

  <!-- little comment: <p>&#x03C0; &#960;</p> -->
  <h1>Special symbols</h1>
  <h2>Greek symbols</h2>
  <p><tt>Alpha</tt>Hi &alpha; Hello &beta; &gamma; &pi; &Alpha; </p>


  <h2>LaTeX chars</h2>
  <p>{ } _ ^ @ $ \ % ~ #</p>

  <h1>LaTeX commands in HTML</h1>
  <p>It's easy to include LaTeX commands in HTML comments.
<!-- latex:
\LaTeX{} greets you.
-->
  </p>

  <h1>Different font styles and sizes.</h1>
  <p>Lorem ipsum <font size="7">dolor</font> sit amet, <i>consectetuer</i> adipiscing elit.
 Nulla ut <strong>lectus</strong> id velit aliquet semper. <tt>Proin vitae</tt> erat. Duis metus. Nam
 vel nisl. Duis <small>lobortis</small> mi at <font size="1">lorem</font>.</p>

  <a name="img"></a>
  <h1>Images</h1>
  <p><!--latex: \LaTeX --> supports only JPG and PNG images.</p>
  <p></p><center><img src="marley.jpg"></center><p></p>
  <p><img src="logo.png"></p>

  <h1>Tables</h1>

  <table border="1">
  <tr><td>1 1</td><td>1 hgf2</td><td>hgfhf1 3</td></tr>
    <tr><td>2 1</td><td>2 2</td><td>2 3</td></tr>
    <tr><td>3 1</td><td>3 2</td><td>3 3</td></tr>
  </table>

  <br>

  <table border="0">
    <tr><td>Sparta Praha</td><td>28</td></tr>
    <tr><td>Slovan Liberec</td><td>25</td></tr>
    <tr><td>Dukla Praha</td><td>24</td></tr>
    <tr><td>Slavia Praha</td><td>20</td></tr>
  </table>

  <h1>Subscript, superscript</h1>
  <p>H<sub>2</sub>O, E = mc<sup>2</sup></p>

  <h1>Hyperlinks</h1>
  <p>I study at <a href="http://www.mff.cuni.cz/" title="MFF">UK MFF</a>. And
    what about <a href="#img">images</a>?</p>

  <h1>Some texts</h1>
<p>
</p><center>
They went in single file, running like hounds on a strong scent,
and an eager light was in their eyes. Nearly due west the broad
swath of the marching <small>Orcs tramped</small> its ugly slot; the sweet grass
of Rohan had been bruised and blackened as they passed.
</center>
<p></p>

<p>John said, I saw Lucy at lunch, she told</p>

    <h1>Lists and definitions</h1>

<dl>
  <dt>Dweeb</dt>
  <dd>young excitable person who may mature
    into a <em>Nerd</em> or <em>Geek</em></dd>
  <dt>Hacker</dt>
  <dd>a clever programmer</dd>
  <dt>Nerd</dt>
  <dd>technically bright but socially inept person</dd>
</dl>


<p>In this section, we discuss the lesser known forest elephants.
...this section continues...</p>

<h2>Habitat</h2>
<p>Forest elephants do not live in trees but among them.
...this subsection continues... </p>

<h3>Habitat</h3>
<p>Forest elephants do not live in trees but among them.
...this subsection continues...  <strong>AND A LINE FOLLOWS</strong> </p>



    <h2>List</h2>
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
&helloooooooooo
</body></html>
'''
parser.parse(html)
file.close()
