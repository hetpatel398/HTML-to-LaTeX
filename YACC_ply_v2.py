################################################ YACC FILE IMPLEMENTATION IN PLY ################################################
########################################################### HET PATEL ###########################################################
########################################################## 2019MCS2562 ##########################################################
########################################################### IIT DELHI ###########################################################

from LEX_ply_v2 import tokens, lexer
# from createLatex import createLatexFile_from_HTMLast
from createLatex import mapHTMLastToLATEXast, createLatexFileFromLatexAst
import ply.yacc as yacc
from node import Node
# file = open("../tex/out.tex","w")
start='document'

def p_empty(p):
     'empty :'
     p[0]=[]

def p_document(p):
    '''
    document : doctype HTML_O head body HTML_E
             | empty
    '''
    if len(p)==6:
        root=Node('HTML')
        root.add_children(p[3])
        root.add_children(p[4])
        # root.traverse()
        # print(root)
        latexAST=mapHTMLastToLATEXast(root)
        createLatexFileFromLatexAst(latexAST)
        latexAST.traverse()
        p[0]=root
    else:
        p[0]=p[1]

def p_doctype(p):
    '''
    doctype : DOCTYPE
            | empty
    '''
    p[0]=[]

def p_head(p):
    '''
    head : HEAD_O head_data HEAD_E
         | empty
    '''
    if len(p)==4:
        node=Node("HEAD")
        node.add_children(p[2])
        p[0]=[node]
    else:
        p[0]=p[1]

def p_head_data(p):
    'head_data : head_data TITLE_O data TITLE_E'
    node=Node("TITLE")
    node.add_children(p[3])
    p[0]=sum([p[1],[node]],[])

# def p_head_data_meta(p):
#     'head_data : head_data META_O'
#     name=p[2][1].get('name')
#     if name=='author':
#         author_name=p[2][1].get('content')
#         p[0]=p[1]+"\\author{"+author_name+"}"
#     else:
#         p[0]=''

def p_head_data_empty(p):
    'head_data : empty'
    p[0]=p[1]

def p_body(p):
    '''
    body : BODY_O body_data BODY_E
         | empty
    '''
    if len(p)==4:
        node=Node("BODY")
        node.add_children(p[2])
        p[0]=[node]
    else:
        p[0]=p[1]

def p_a(p):
    'body_data : body_data A_O body_data A_E data'
    node=Node("A",p[2][1])
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_font(p):
    'body_data : body_data FONT_O body_data FONT_E data'
    node=Node("FONT",p[2][1])
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_center(p):
    'body_data : body_data CENTER_O body_data CENTER_E data'
    node=Node("CENTER")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_br(p):
    '''body_data : body_data BR_S data
                 | body_data BR_O data
                 | body_data BR_O BR_E data'''
    if len(p) == 4:
        node=Node("BR")
        p[0]=sum([p[1],[node],p[3]],[])
    else:
        node=Node("BR")
        p[0]=sum([p[1],[node],p[4]],[])

def p_p(p):
    '''body_data : body_data P_O body_data P_E data'''
    node=Node("P")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_H1(p):
    'body_data : body_data H1_O body_data H1_E data'
    node=Node("H1")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_H2(p):
    'body_data : body_data H2_O body_data H2_E data'
    node=Node("H2")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_H3(p):
    'body_data : body_data H3_O body_data H3_E data'
    node=Node("H3")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_H4(p):
    'body_data : body_data H4_O body_data H4_E data'
    node=Node("H4")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_H5(p):
    'body_data : body_data H5_O body_data H5_E data'
    node=Node("H5")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_H6(p):
    'body_data : body_data H6_O body_data H6_E data'
    node=Node("H6")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_ordered_list(p):
    'body_data : body_data OL_O body_data OL_E data'
    node=Node("OL")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_unordered_list(p):
    'body_data : body_data UL_O body_data UL_E data'
    node=Node("UL")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_list_items(p):
    'body_data : body_data LI_O body_data LI_E data'
    node=Node("LI")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_dl(p):
    'body_data : body_data DL_O body_data DL_E data'
    node=Node("DL")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_dt(p):
    'body_data : body_data DT_O body_data DT_E data'
    node=Node("DT")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_dd(p):
    'body_data : body_data DD_O body_data DD_E data'
    node=Node("DD")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_div(p):
    'body_data : body_data DIV_O body_data DIV_E data'
    node=Node("DIV")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_u(p):
    'body_data : body_data U_O body_data U_E data'
    node=Node("U")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_b(p):
    '''body_data : body_data B_O body_data B_E data
                 | body_data STRONG_O body_data STRONG_E data'''
    node=Node("B")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_i(p):
    'body_data : body_data I_O body_data I_E data'
    node=Node("I")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_em(p):
    'body_data : body_data EM_O body_data EM_E data'
    node=Node("EM")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_tt(p):
    'body_data : body_data TT_O body_data TT_E data'
    node=Node("TT")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_small(p):
    'body_data : body_data SMALL_O body_data SMALL_E data'
    node=Node('SMALL')
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_sub(p):
    'body_data : body_data SUB_O body_data SUB_E data'
    node=Node("SUB")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_sup(p):
    'body_data : body_data SUP_O body_data SUP_E data'
    node=Node("SUP")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_special_greek_symbol(p):
    'body_data : body_data GREEK_SPECIAL_SYMBOL data'
    node=Node("GREEK", {'symbol':p[2]})
    p[0]=sum([p[1],[node],p[3]],[])

def p_img(p):
    '''body_data : body_data IMG_S data
                 | body_data IMG_O data
                 | body_data IMG_O IMG_E data
    '''
    node=Node("IMG", p[2][1])
    if len(p)==4:
        p[0]=sum([p[1],[node],p[3]],[])
    else:
        p[0]=sum([p[1],[node],p[4]],[])
#     width = p[2][1].get('width')
#     height = p[2][1].get('height')
#     src = p[2][1].get('src')
#     if len(p) ==4:
#         if (width == None and height==None):
#             p[0]=p[1]+"\includegraphics{"+src+"}"+p[3]
#         elif (width != None and height!=None):
#             p[0]=p[1]+"\includegraphics[width="+width+", height="+height+"]{"+src+"}"+p[3]
#         elif (width != None and height==None):
#             p[0]=p[1]+"\includegraphics[width="+width+"]{"+src+"}"+p[3]
#         elif (width == None and height!=None):
#             p[0]=p[1]+"\includegraphics[height="+height+"]{"+src+"}"+p[3]
#     elif len(p)==5:
#         if (width == None and height==None):
#             p[0]=p[1]+"\includegraphics{"+src+"}"+p[4]
#         elif (width != None and height!=None):
#             p[0]=p[1]+"\includegraphics[width="+width+", height="+height+"]{"+src+"}"+p[4]
#         elif (width != None and height==None):
#             p[0]=p[1]+"\includegraphics[width="+width+"]{"+src+"}"+p[4]
#         elif (width == None and height!=None):
#             p[0]=p[1]+"\includegraphics[height="+height+"]{"+src+"}"+p[4]

def p_figure(p):
    'body_data : body_data FIGURE_O fig_data FIGURE_E data'
    node=Node("FIGURE")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_fig_data_img(p):
    '''
    fig_data : fig_data IMG_O
             | fig_data IMG_S
             | fig_data IMG_O IMG_E
    '''
    node=Node("IMG", p[2][1])
    p[0]=sum([p[1],[node]],[])
#     width = p[2][1].get('width')
#     height = p[2][1].get('height')
#     src = p[2][1].get('src')
#     if (width == None and height==None):
#         p[0]=p[1]+"\includegraphics{"+src+"}\n"
#     elif (width != None and height!=None):
#         p[0]=p[1]+"\includegraphics[width="+width+", height="+height+"]{"+src+"}\n"
#     elif (width != None and height==None):
#         p[0]=p[1]+"\includegraphics[width="+width+"]{"+src+"}\n"
#     elif (width == None and height!=None):
#         p[0]=p[1]+"\includegraphics[height="+height+"]{"+src+"}\n"

def p_figcaption(p):
    'fig_data : fig_data FIGCAPTION_O body_data FIGCAPTION_E'
    node=Node("FIGCAPTION")
    node.add_children(p[3])
    p[0]=sum([p[1],[node]],[])

def p_fig_data_empty(p):
    'fig_data : empty'
    p[0]=p[1]

def p_table(p):
    '''
    body_data : body_data TABLE_O caption table_data TABLE_E data
              | body_data TABLE_O table_data TABLE_E data
    '''
    node=Node("TABLE",p[2][1])
    if len(p)==7:
        node.add_children(p[3])
        node.add_children(p[4])
        p[0]=sum([p[1],[node],p[6]],[])
    else:
        node.add_children(p[3])
        p[0]=sum([p[1],[node],p[5]],[])

def p_caption(p):
    'caption : CAPTION_O body_data CAPTION_E'
    node=Node("CAPTION")
    node.add_children(p[2])
    p[0]=[node]

def p_table_data(p):
    '''
    table_data : first_row rows
               | empty
    '''
    if len(p) == 3:
        p[0]=sum([p[1],p[2]],[])
    else:
        p[0]=p[1]

def p_first_row(p):
    'first_row : TR_O td_or_th TR_E'
    node=Node("FIRSTROW")
    node.add_children(p[2])
    p[0]=[node]

def p_td_or_th(p):
    '''
    td_or_th : td_or_th TD_O body_data TD_E
             | td_or_th TH_O body_data TH_E
             | empty
    '''
    if len(p)==5:
        if p[2][0]=="th" or p[2][0]=="TH" or p[2][0]=="Th" or p[2][0]=="tH":
            node=Node("TH")
            node.add_children(p[3])
            p[0]=sum([p[1],[node]],[])
        else:
            node=Node("TD")
            node.add_children(p[3])
            p[0]=sum([p[1],[node]],[])
    else:
        p[0]=p[1]

def p_rows(p):
    '''
    rows : rows TR_O cols TR_E
         | empty
    '''
    if len(p) == 5:
        node=Node("TR")
        node.add_children(p[3])
        p[0]=sum([p[1],[node]],[])
    else:
        p[0]=p[1]

def p_cols(p):
    '''
    cols : cols TD_O body_data TD_E
         | empty
    '''
    if len(p) == 5:
        node=Node("TD")
        node.add_children(p[3])
        p[0]=sum([p[1],[node]],[])
    else:
        p[0]=p[1]

def p_comment(p):
    'body_data : body_data COMMENT data'
    node=Node("COMMENT",{'value':p[2]})
    p[0]=sum([p[1],[node],p[3]],[])

def p_body_data_data(p):
    'body_data : data'
    p[0]=p[1]

def p_data(p):
    '''data : data STRING
            | data ANOTHER_STRING
            | empty
    '''
    if len(p)==3:
        node=Node("STRING",{'value':p[2]})
        p[0]=sum([p[1],[node]],[])
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

html='''

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
  <head>
  <title>Sample document</title>

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

 <div>
    <p>Div line 1. </p>
 </div>

 <div>
  <p>Div line 2. </p>
 </div>

 <div>
  <p>Div line 3.</p>
</div>


  <!-- little comment: <p>&#x03C0; &#960;</p> -->
  <h1>Special symbols</h1>
  <h2>Greek symbols</h2>


  <h2>LaTeX chars</h2>


  <h1>LaTeX commands in HTML</h1>
  <p>It's easy to include LaTeX commands in HTML comments.
<!-- latex:
\LaTeX{} greets you.
-->
  </p>

  <h1>Different font styles and sizes.</h1>
  <p>Lorem ipsum <font size='7'>dolor</font> sit amet, <i>consectetuer</i> adipiscing elit.
 Nulla ut <strong>lectus</strong> id velit aliquet semper. <tt>Proin vitae</tt> erat. Duis metus. Nam
 vel nisl. Duis <small>lobortis</small> mi at <font size='1'>lorem</font>.</p>

  <a name="img"></a>
  <h1>Images</h1>
  <p><!--latex: \LaTeX --> supports only JPG and PNG images.</p>
  <p><center><img src='marley.jpg' /></center></p>
  <p><img src='logo.png' /></p>

  <h1>Tables</h1>


  <h1>Subscript, superscript</h1>
  <p>H<sub>2</sub>O, E = mc<sup>2</sup></p>

  <h1>Hyperlinks</h1>
  <p>I study at <a href="http://www.mff.cuni.cz" title='MFF'>UK MFF</a>. And
    what about <a href="#img">images</a>?</p>

  <h1>Some texts</h1>
<p>
<center>
They went in single file, running like hounds on a strong scent,
and an eager light was in their eyes. Nearly due west the broad
swath of the marching <small>Orcs tramped</small> its ugly slot; the sweet grass
of Rohan had been bruised and blackened as they passed.
</center>
</p>

<p>John said, I saw Lucy at lunch, she told</p>

    <h1>Lists and definitions</h1>

<DL>
  <DT>Dweeb</DT>
  <DD>young excitable person who may mature
    into a <EM>Nerd</EM> or <EM>Geek</EM></DD>
  <DT>Hacker</DT>
  <DD>a clever programmer</DD>
  <DT>Nerd</DT>
  <DD>technically bright but socially inept person</DD>
</DL>


<P>In this section, we discuss the lesser known forest elephants.
...this section continues...</p>

<H2>Habitat</H2>
<P>Forest elephants do not live in trees but among them.
...this subsection continues... </p>

<H3>Habitat</H3>
<P>Forest elephants do not live in trees but among them.
...this subsection continues...  <strong>AND A LINE FOLLOWS</strong> </p>



    <h2>List</h2>
<UL>
     <LI> ... Level one, number one...</li>
     <OL>
        <LI> ... Level two, number one...</li>
        <LI> ... Level two, number two...</li>
        <OL>
           <LI> ... Level three, number one...</li>
        </OL>
        <LI> ... Level two, number three...</li>
     </OL>
     <LI> ... Level one, number two...</li>
</UL>

  </body>
</html>

'''
parser.parse(html)
# file.close()
