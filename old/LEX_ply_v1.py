################################################# LEX FILE IMPLEMENTATION IN PLY ################################################
########################################################### HET PATEL ###########################################################
########################################################## 2019MCS2562 ##########################################################
########################################################### IIT DELHI ###########################################################


import ply.lex as lex

 # List of token names.   This is always required
tokens = (
    'STRING',       'OPENING_TAG',      'CLOSING_TAG',      'SINGLE_TAG',   'COMMENT',
    'GREEK_SPECIAL_SYMBOL',             'ANOTHER_STRING',   'DOCTYPE',

    'HTML_O',       'HEAD_O',           'TITLE_O',          'BODY_O',       'A_O',
    'FONT_O',       'CENTER_O',         'BR_O',             'P_O',          'H1_O',
    'H2_O',         'H3_O',             'H4_O',             'UL_O',         'LI_O',
    'OL_O',         'DL_O',             'DT_O',             'DD_O',         'DIV_O',
    'U_O',          'B_O',              'I_O',              'EM_O',         'TT_O',
    'STRONG_O',     'SMALL_O',          'SUB_O',            'SUP_O',        'IMG_O',
    'FIGURE_O',     'FIGCAPTION_O',     'TABLE_O',          'CAPTION_O',    'TH_O',
    'TR_O',         'TD_O',             'META_O',

    'HTML_E',       'HEAD_E',           'TITLE_E',          'BODY_E',       'A_E',
    'FONT_E',       'CENTER_E',         'BR_E',             'P_E',          'H1_E',
    'H2_E',         'H3_E',             'H4_E',             'UL_E',         'LI_E',
    'OL_E',         'DL_E',             'DT_E',             'DD_E',         'DIV_E',
    'U_E',          'B_E',              'I_E',              'EM_E',         'TT_E',
    'STRONG_E',     'SMALL_E',          'SUB_E',            'SUP_E',        'IMG_E',
    'FIGURE_E',     'FIGCAPTION_E',     'TABLE_E',          'CAPTION_E',    'TH_E',
    'TR_E',         'TD_E',

    'BR_S',         'IMG_S',
)

word = r'(\w)+'
anotherword=r'\&(\w+)'

t_DOCTYPE=r'(?i)<!doctype (.*?)>'

def t_GREEK_SPECIAL_SYMBOL(t):
    r'&\w+;'
    t.value=t.value[1:-1]
    return t

t_ANOTHER_STRING=r'\&\w+'

# Regular expression rules for simple tokens
def t_STRING(t):
    # r'^(?!&\w+;.*$).+'
    r'(\w|[ ]|\.|\,|\:|\;|\'|\"|\(|\)|\-|\_|\=|\{|\+|\}|\[|\]|\/|\\|\!|\@|\#|\$|\%|\^|\*|\?|\~|\|\`|\&(\s)+)+'
    t.value=t.value.replace('\\','\\\\')
    t.value=t.value.replace('_','\_')
    t.value=t.value.replace('#','\#')
    t.value=t.value.replace('%','\%')
    t.value=t.value.replace('~','\~')
    t.value=t.value.replace('^','\^')
    t.value=t.value.replace('{','\{')
    t.value=t.value.replace('}','\}')
    return t

def t_SINGLE_TAG(t):
    r'<(\w)+(\s\w+=[\',\"][\w,\/,\:,\.,\#,\%]+[\',\"])*\s*/>'
    # t.type=t.value[1:-2].strip().upper()+'_S'
    # t.value=[t.value[1:-2]]

    tmp=t.value[1:-2]
    tmp_split=tmp.split()
    lst=[]
    lst.append(tmp_split[0])
    t.type=tmp_split[0].upper()+'_S'
    attrs=dict()
    for s in tmp_split[1:]:
        attr=s.split('=')
        attrs[attr[0].lower()] = attr[1][1:-1]
    lst.append(attrs)
    t.value=lst

    return t

def t_OPENING_TAG(t):
    # r'<\w+([\w+ = (\'\w+\' | \"(\w+|\.|\:|\/)\")])*>'
    r'<\w+(\s\w+=[\',\"][\w,\/,\:,\.,\#,\%]+[\',\"])*\s*>'
    tmp=t.value[1:-1]
    tmp_split=tmp.split()
    lst=[]
    lst.append(tmp_split[0])
    t.type=tmp_split[0].upper()+'_O'
    attrs=dict()
    for s in tmp_split[1:]:
        attr=s.split('=')
        attrs[attr[0]] = attr[1][1:-1]
    lst.append(attrs)
    t.value=lst
    return t;

def t_CLOSING_TAG(t):
    r'</(\w)+>'
    t.type=t.value[2:-1].upper()+'_E'
    return t

def t_COMMENT(t):
    r'<!--(.|\n)*?-->'
    t.value=t.value[4:-3]
    return t

t_ignore  = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 # Error handling rule
def t_error(t):
    print("Illegal character '%s' on line %s" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

 # Build the lexer
lexer = lex.lex()

html='''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head>
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
  &theta;

</body></html>

'''
# file = open("Sample document.html","r")
 # Give the lexer some input
html='''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html><head>
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

 <p>
    </p><div>Div line 1. </div>
    <div>Div line 2. </div>
    <div>Div line 3</div>
 <p></p>

  <!-- little comment: <p>&#x03C0; &#960;</p> -->
  <h1>Special symbols</h1>
  <h2>Greek symbols</h2>
  <p><tt>Alpha</tt>&alpha; , &beta; &gamma; &pi; &Alpha; </p>


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
  <p></p><center><img src="Sample%20document_original_files/marley.jpg"></center><p></p>
  <p><img src="Sample%20document_original_files/logo.png"></p>

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
</body></html>
'''


# lexer.input(html)
#
# for token in lexer:
#     print(token)
