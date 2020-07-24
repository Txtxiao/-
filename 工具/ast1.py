import astunparse as astunparse

import ast

class CodeVisitor(ast.NodeVisitor):
    tree='('
    def append(self, expr):
        self.tree += expr
    def generic_visit(self, node):
        self.append(type(node).__name__ )

        ast.NodeVisitor.generic_visit(self, node)


'''
class CodeVisitor(ast.NodeVisitor):
    tree = ''

    def append(self, expr):
        self.tree += expr

    def visit_And(self, node):
        self.append("and ")

    def visit_Lt(self, node):
        self.append("< ")

    def visit_Gt(self, node):
        self.append("> ")

    def visit_Eq(self, node):
        self.append("== ")

    def visit_Num(self, node):
        self.append("value: %s " % node.n)

    def visit_Name(self, node):
        self.append("variable: %s " % node.id)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        self.append("(")
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)
            elif isinstance(value, ast.AST):
                self.visit(value)
        self.append(")")
       
'''

if __name__ == '__main__':
    file = open(r"E:\大二下自学\数据科学基础\datatest\在排序数组中查找元素的第一个和最后一个位置_1580449475334\.mooctest\answer.py")
    func_def = file.read()
    #cm = compile(func_def, '<string>', 'exec')


    r_node = ast.parse(func_def)
    v=CodeVisitor()
    v.visit(r_node)
    print(v.tree)



    result= astunparse.dump(r_node)
    print(result)



