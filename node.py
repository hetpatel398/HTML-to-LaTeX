################################################# AST NODE IMPLEMENTATION CLASS #################################################
########################################################### HET PATEL ###########################################################
########################################################## 2019MCS2562 ##########################################################
########################################################### IIT DELHI ###########################################################

#In this file I have created a new class Node which will be used to generate AST
#Every node will have three major fields
    # 1. type(STRING)
    # 2. attributes(DICTIONARY)
    # 3. children(LIST)
#
#I have stored type of a node in type value of a jonde
class Node:
    def __init__(self,type,attributes={},children=[]):
        self.type=type
        self.attributes=attributes
        self.children=children

    def __repr__(self):
        s='(%s,%s,%s)'%(self.type, str(self.attributes), str(self.children))
        return s

    def add_children(self, list_of_children):
        self.children=self.children+list_of_children

    def traverse(self):
        print(self.type)
        if self.children!=[]:
            print('-'*10+'>START Children of :'+self.type)
            for child in self.children:
                child.traverse()
            print('-'*10+'>FINISH Children of :'+self.type)
