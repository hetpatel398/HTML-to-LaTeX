################################################ YACC FILE IMPLEMENTATION IN PLY ################################################
########################################################### HET PATEL ###########################################################
########################################################## 2019MCS2562 ##########################################################
########################################################### IIT DELHI ###########################################################


#HERE is my grammer for YACC file

# S' -> start
# empty -> <empty>
# start -> document
# document -> comment HTML_O head body HTML_E comment
# document -> empty
#
# comment -> COMMENT
# comment -> empty
#
# head -> comment HEAD_O head_data HEAD_E comment
# head -> empty
# head_data -> head_data TITLE_O data TITLE_E comment
# head_data -> head_data META_O comment
# head_data -> comment
# body -> BODY_O body_data BODY_E comment
# body -> empty
    # body_data -> body_data A_O body_data A_E data
    # body_data -> body_data FONT_O body_data FONT_E data
    # body_data -> body_data CENTER_O body_data CENTER_E data
    #
    # body_data -> body_data BR_S data
    # body_data -> body_data BR_O data
    # body_data -> body_data BR_O BR_E data
    #
    # body_data -> body_data P_O body_data P_E data
    #
    # body_data -> body_data H1_O body_data H1_E data
    # body_data -> body_data H2_O body_data H2_E data
    # body_data -> body_data H3_O body_data H3_E data
    # body_data -> body_data H4_O body_data H4_E data
    # body_data -> body_data H5_O body_data H5_E data
    # body_data -> body_data H6_O body_data H6_E data
    #
    # body_data -> body_data OL_O body_data OL_E data
    # body_data -> body_data UL_O body_data UL_E data
    # body_data -> body_data LI_O body_data LI_E data
    # body_data -> body_data DL_O body_data DL_E data
    # body_data -> body_data DT_O body_data DT_E data
    # body_data -> body_data DD_O body_data DD_E data
    #
    # body_data -> body_data DIV_O body_data DIV_E data
    #
    # body_data -> body_data U_O body_data U_E data
    # body_data -> body_data B_O body_data B_E data
    # body_data -> body_data STRONG_O body_data STRONG_E data
    # body_data -> body_data I_O body_data I_E data
    # body_data -> body_data EM_O body_data EM_E data
    # body_data -> body_data TT_O body_data TT_E data
    # body_data -> body_data SMALL_O body_data SMALL_E data
    #
    # body_data -> body_data SUB_O body_data SUB_E data
    # body_data -> body_data SUP_O body_data SUP_E data
    # body_data -> body_data GREEK_SPECIAL_SYMBOL data
    #
    # body_data -> body_data IMG_S data
    # body_data -> body_data IMG_O data
    # body_data -> body_data IMG_O IMG_E data
    # body_data -> body_data FIGURE_O fig_data FIGURE_E data
        # fig_data -> fig_data IMG_O
        # fig_data -> fig_data IMG_S
        # fig_data -> fig_data IMG_O IMG_E
        # fig_data -> fig_data FIGCAPTION_O body_data FIGCAPTION_E
        # fig_data -> empty
    #
    # body_data -> body_data TABLE_O caption table_data TABLE_E data
    # body_data -> body_data TABLE_O table_data TABLE_E data
        # caption -> CAPTION_O body_data CAPTION_E
        # table_data -> first_row rows
        # table_data -> empty
        # first_row -> TR_O td_or_th TR_E
        # td_or_th -> td_or_th TD_O body_data TD_E
        # td_or_th -> td_or_th TH_O body_data TH_E
        # td_or_th -> empty
        # rows -> rows TR_O cols TR_E
        # rows -> empty
        # cols -> cols TD_O body_data TD_E
        # cols -> empty
    #
    # body_data -> body_data COMMENT data
    # body_data -> body_data OPENING_TAG data
    # body_data -> body_data CLOSING_TAG data
    # body_data -> body_data SINGLE_TAG data
    # body_data -> data
# data -> data STRING
# data -> data ANOTHER_STRING
#data -> empty


from LEX_ply import tokens, lexer        #importing tokens and lexer which we declared in LEX_ply.py file
import ply.yacc as yacc #YACC implementation from ply
from node import Node   #Out AST Node representation class

start='start'

def p_empty(p):     #Defining empty production
     'empty :'
     p[0]=[]

def p_start(p):
    'start : document'
    node=Node('ROOT',{},p[1])
    p[0]=node

def p_document(p):  #This is our main production
    '''
    document : comment HTML_O head body HTML_E comment
             | empty
    '''
    if len(p)==7:
        root=Node('HTML')
        root.add_children(p[3])
        root.add_children(p[4])
        p[0]=sum([p[1],[root],p[6]],[])
    else:
        p[0]=p[1]

def p_comment_alone(p):
    'comment : COMMENT'
    node=Node("COMMENT",{'value':'%'+(p[1].replace('\n','\n%'))})
    p[0]=[node]

def p_comment_empty(p):
    'comment : empty'
    p[0]=p[1]

def p_head(p):
    '''
    head : comment HEAD_O head_data HEAD_E comment
         | empty
    '''
    if len(p)==6:
        node=Node("HEAD")
        node.add_children(p[3])
        p[0]=sum([p[1],[node],p[5]],[])
    else:
        p[0]=p[1]

def p_head_data(p):
    'head_data : head_data TITLE_O data TITLE_E comment'
    node=Node("TITLE")
    node.add_children(p[3])
    p[0]=sum([p[1],[node],p[5]],[])

def p_head_data_meta(p):
    'head_data : head_data META_O comment'
    name=p[2][1].get('name')
    if name=='author':
        author_name=p[2][1].get('content')
        node=Node('AUTHOR',{'value':author_name})
        p[0]=sum([p[1],[node],p[3]],[])
    else:
        p[0]=sum([p[1],p[3]],[])

def p_head_data_comment(p):
    '''
    head_data : comment
    '''
    p[0]=p[1]

def p_body(p):
    '''
    body : BODY_O body_data BODY_E comment
         | empty
    '''
    if len(p)==5:
        node=Node("BODY")
        node.add_children(p[2])
        p[0]=sum([[node],p[4]],[])
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
    '''
    first_row : TR_O td_or_th TR_E
    '''
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

def p_body_comment(p):
    'body_data : body_data COMMENT data'
    node=Node("COMMENT",{'value':'%'+(p[2].replace('\n','\n%'))})
    p[0]=sum([p[1],[node],p[3]],[])


def p_opening_tag(p):
    'body_data : body_data OPENING_TAG data'
    node=Node("OPENING_TAG",{'value':'\\textless '+p[2][0]+'\\textgreater '})
    p[0]=sum([p[1],[node],p[3]],[])

def p_closing_tag(p):
    'body_data : body_data CLOSING_TAG data'
    node=Node("CLOSING_TAG",{'value':p[2]})
    p[0]=sum([p[1],[node],p[3]],[])

def p_single_tag(p):
    'body_data : body_data SINGLE_TAG data'
    node=Node("SINGLE_TAG",{'value':'\\textless '+p[2][0]+'\\textgreater '})
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

# def p_body_data_star(p):                                   #Uncomment this function to to SR and RR conflicts in output
#     'body_data : body_data body_data'
#     p[0]=p[1]+p[2]
#
# def p_body_data_empty(p):
#     'body_data : empty'
#     p[0]=""

def p_error(p):                 #Defines error
    print("Syntax error in input!")

parser = yacc.yacc()
