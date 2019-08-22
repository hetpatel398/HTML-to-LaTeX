import ply.lex as lex

 # List of token names.   This is always required
tokens = (
    'STRING',       'OPENING_TAG',      'CLOSING_TAG',      'SINGLE_TAG',   'COMMENT',

    'HTML_O',       'HEAD_O',           'TITLE_O',          'BODY_O',       'A_O',
    'FONT_O',       'CENTER_O',         'BR_O',             'P_O',          'H1_O',
    'H2_O',         'H3_O',             'H4_O',             'UL_O',         'LI_O',
    'OL_O',         'DL_O',             'DT_O',             'DD_O',         'DIV_O',
    'U_O',          'B_O',              'I_O',              'EM_O',         'TT_O',
    'STRONG_O',     'SMALL_O',          'SUB_O',            'SUP_O',        'IMG_O',
    'TABLE_O',      'CAPTION_O',        'TH_O',             'TR_O',         'TD_O',
    'TBODY_O',

    'HTML_E',       'HEAD_E',           'TITLE_E',          'BODY_E',       'A_E',
    'FONT_E',       'CENTER_E',         'BR_E',             'P_E',          'H1_E',
    'H2_E',         'H3_E',             'H4_E',             'UL_E',         'LI_E',
    'OL_E',         'DL_E',             'DT_E',             'DD_E',         'DIV_E',
    'U_E',          'B_E',              'I_E',              'EM_E',         'TT_E',
    'STRONG_E',     'SMALL_E',          'SUB_E',            'SUP_E',        'IMG_E',
    'TABLE_E',      'CAPTION_E',        'TH_E',             'TR_E',         'TD_E',
    'TBODY_E',

    'BR_S'
)

word = r'(\w)+'

# Regular expression rules for simple tokens
def t_STRING(t):
    r'(\w|[ ]|\.|\,|\:|\;|\'|\"|\(|\)|\-|\_|\=|\{|\+|\}|\[|\]|\/|\\|\!|\@|\#|\$|\%|\^|\&|\*|\?|\~|\`)+'
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
    r'<(\w)+\s*/>'
    t.type=t.value[1:-2].strip().upper()+'_S'
    # t.value=[t.value[1:-2]]
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

# html='''<hTmL>
# <head>
#     <title>Het12Patel DEMO leX1</title>
# </head>
# <body>
#     <h1>This is my heading</h1>
#     <a href="https://google.com/home/login">Google Search</a>
#     <br/>
# </body>
# </html>
# '''
# # file = open("Sample document.html","r")
#  # Give the lexer some input
# lexer.input(file.read())
#
# for token in lexer:
#     print(token)
