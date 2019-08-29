class node:
    def __init__(self,value,children,attributes):
        self.value=value
        self.children=children
        self.attributes=attributes
    def __repr__(self):
        s='(%s,%s,%s)'%(self.value, str(self.children), str(self.attributes))
        return s

p=node('p',[],{})
body=node('body',[p],{})
html=node('html',[body],{})
print(html)
