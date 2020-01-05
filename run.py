from YACC_ply import parser
import sys              #To get command ine arguments
from createLatex import mapHTMLastToLATEXast, createLatexFileFromLatexAst  #Importing functions which will map HTML AST to Latex AST and then will generate output file using that

input_file_name=sys.argv[1]
output_file_name=sys.argv[2]

output_file=open(output_file_name, 'w' ,encoding='utf8')
input_file=open(input_file_name, encoding='utf8')

html_input=input_file.read()                            #Reading inpit file
input_file.close()

rootOfHTMLast=parser.parse(html_input)                    #Parsing html
latexAST=mapHTMLastToLATEXast(rootOfHTMLast)                 #Converting HTML AST to LaTeX AST
createLatexFileFromLatexAst(latexAST, output_file)  #Generating the output file using LaTeX AST
