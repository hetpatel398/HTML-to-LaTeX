################################################# LEX FILE IMPLEMENTATION IN PLY ################################################
########################################################### HET PATEL ###########################################################
########################################################## 2019MCS2562 ##########################################################
########################################################### IIT DELHI ###########################################################


import ply.lex as lex
import re               #Used to extract attributes of tags

# tuple of token types that can be generated via this lexer

tokens = (
    'STRING',       'OPENING_TAG',      'CLOSING_TAG',      'SINGLE_TAG',   'COMMENT',
    'DOCTYPE',      'ANOTHER_STRING',   'GREEK_SPECIAL_SYMBOL',

    'HTML_O',       'HEAD_O',           'TITLE_O',          'BODY_O',       'A_O',
    'FONT_O',       'CENTER_O',         'BR_O',             'P_O',          'H1_O',
    'H2_O',         'H3_O',             'H4_O',             'H5_O',         'H6_O',
    'UL_O',         'LI_O',             'OL_O',             'DL_O',         'DT_O',
    'DD_O',         'DIV_O',            'U_O',              'B_O',          'I_O',
    'EM_O',         'TT_O',             'STRONG_O',         'SMALL_O',      'SUB_O',
    'SUP_O',        'IMG_O',            'FIGURE_O',         'FIGCAPTION_O', 'TABLE_O',
    'CAPTION_O',    'TH_O',             'TR_O',             'TD_O',         'META_O',

    'HTML_E',       'HEAD_E',           'TITLE_E',          'BODY_E',       'A_E',
    'FONT_E',       'CENTER_E',         'BR_E',             'P_E',          'H1_E',
    'H2_E',         'H3_E',             'H4_E',             'H5_E',         'H6_E',
    'UL_E',         'LI_E',             'OL_E',             'DL_E',         'DT_E',
    'DD_E',         'DIV_E',            'U_E',              'B_E',          'I_E',
    'EM_E',         'TT_E',             'STRONG_E',         'SMALL_E',      'SUB_E',
    'SUP_E',        'IMG_E',            'FIGURE_E',         'FIGCAPTION_E', 'TABLE_E',
    'CAPTION_E',    'TH_E',             'TR_E',             'TD_E',

    'BR_S',         'IMG_S',
)

def t_DOCTYPE(t):
    r'(?i)<!doctype (.*?)>'   #Token for DOCTYPE
    pass

def t_GREEK_SPECIAL_SYMBOL(t):      #Token for Greek Symbols
    r'&\w+;'
    t.value=t.value[1:-1]
    return t

t_ANOTHER_STRING=r'\&\w+'           #Token for another string, I created this token in addition to STRING token to handle a case when word is starting with & but it isn't a greek word i.e. It starts with & but don't have ; at the end

# Regular expression for STRING
def t_STRING(t):
    r'(\w|[ ]|\.|\,|\:|\;|\'|\"|\(|\)|\-|\_|\=|\{|\+|\}|\[|\]|\/|\\|\!|\@|\#|\$|\%|\^|\*|\?|\~|\|\`|\&(\s)+)+'
    t.value=t.value.replace('\\','\\textbackslash')                         #Replacing Latex special characters to their corrosponding value
    t.value=t.value.replace('_','\\_')                                      #
    t.value=t.value.replace('#','\\#')                                      #
    t.value=t.value.replace('%','\\%')                                      #
    t.value=t.value.replace('$','\\$')                                      #
    t.value=t.value.replace('&','\\&')                                      #
    t.value=t.value.replace('~','\\sim')                                    #
    t.value=t.value.replace('{','\\{')                                      #
    t.value=t.value.replace('}','\\}')                                      #
    t.value=t.value.replace('^','\\hat{}')                                  #
    t.value=t.value.replace('<','\\textless')                               #
    t.value=t.value.replace('>','\\textgreater')                            #

    return t

def t_SINGLE_TAG(t):
    r'<(\w)+(\s\w+=[\',\"][\w,\/,\:,\(,\),\?,\&,\@,\$,\^,\*,\[,\],\{,\},\;,\,,\.,\#,\%,\s]+[\',\"])*\s*/>'

    tmp=t.value[1:-2]                                   #removed first and last two characters i.e. < and />
    tmp_split=tmp.split()                               #Splitting them with space to get tag's name
    lst=[]                                              #Creating a empty list which will contain out token's return value i.e. [TOKEN_NAME, {dict_of_token_attributes}]
    lst.append(tmp_split[0])                            #Appending TOKEN_NAME
    if tmp_split[0].upper()+'_S' in tokens:             #Checking if out tag is in the token's tuple if it is not there we can say that we don't know this tag and print it as it is
        t.type=tmp_split[0].upper()+'_S'
    attrs=dict()                                        #Creating empty Dictionary for attributes
    attrs_string=' '.join(tmp_split[1:])                #Removing tag's name and joining remianing
    attrs_regex=r'\w+=[\',\"][\w,\/,\:,\(,\),\?,\&,\@,\$,\^,\*,\[,\],\{,\},\;,\,,\.,\#,\%,\s]+[\',\"]' #Regex that will match every attributes one by one
    reg=re.compile(attrs_regex)                         #Compiling RE
    match=reg.match(attrs_string)                       #Getting the first match
    while match != None:
        s=attrs_string[match.start():match.end()]       #Getting the matched substring
        s1=s.split('=')                                 #Splitting it by = as it is of form attribute_name=attribute_value
        attrs[s1[0]]=s1[1][1:-1]                        #removing quots from the value part and assigning it to it's name in dictionary
        attrs_string=attrs_string[match.end():].strip() #Getting the string that is after our matched substring to check for the next attribute
        match=reg.match(attrs_string.strip())           #Finding the next attribute and loop continues if match is found
    lst.append(attrs)                                   #adding attributes' dictionary to list
    t.value=lst                                         #setting value of token to the list that we have generated
    return t

def t_OPENING_TAG(t):
    r'<\w+(\s\w+=[\',\"][\w,\/,\:,\(,\),\?,\&,\@,\$,\^,\*,\[,\],\{,\},\;,\,,\.,\#,\%,\s]+[\',\"])*\s*>'
    tmp=t.value[1:-1]                                   #removed first and last characters i.e. < and >
    tmp_split=tmp.split()                               #Splitting them with space to get tag's name
    lst=[]                                              #Creating a empty list which will contain out token's return value i.e. [TOKEN_NAME, {dict_of_token_attributes}]
    lst.append(tmp_split[0])                            #Appending TOKEN_NAME
    if tmp_split[0].upper()+'_O' in tokens:             #Checking if out tag is in the token's tuple if it is not there we can say that we don't know this tag and print it as it is
        t.type=tmp_split[0].upper()+'_O'
    attrs=dict()                                        #Creating empty Dictionary for attributes
    attrs_string=' '.join(tmp_split[1:])                #Removing tag's name and joining remianing
    attrs_regex=r'\w+=[\',\"][\w,\/,\:,\(,\),\?,\&,\@,\$,\^,\*,\[,\],\{,\},\;,\,,\.,\#,\%,\s]+[\',\"]' #Regex that will match every attributes one by one
    reg=re.compile(attrs_regex)                         #Getting the first match
    match=reg.match(attrs_string)
    while match != None:
        s=attrs_string[match.start():match.end()]       #Getting the matched substring
        s1=s.split('=')                                 #Splitting it by = as it is of form attribute_name=attribute_value
        attrs[s1[0]]=s1[1][1:-1]                        #removing quots from the value part and assigning it to it's name in dictionary
        attrs_string=attrs_string[match.end():].strip() #Getting the string that is after our matched substring to check for the next attribute
        match=reg.match(attrs_string.strip())           #Finding the next attribute and loop continues if match is found
    lst.append(attrs)                                   #adding attributes' dictionary to list
    t.value=lst                                         #setting value of token to the list that we have generated
    return t

def t_CLOSING_TAG(t):
    r'</(\w)+>'
    if t.value[2:-1].upper()+'_E' in tokens:
        t.type=t.value[2:-1].upper()+'_E'
    return t

def t_COMMENT(t):                           #Regular Expression to detect comments
    r'<!--(.|\n)*?-->'
    t.value=t.value[4:-3]
    return t

t_ignore  = ' \t'                           #ignoring all tabs and spaces

# tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s' on line %s" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

lexer = lex.lex()
