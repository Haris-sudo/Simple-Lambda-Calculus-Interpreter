class Name:
    def __init__(self, ID):
        self.ID = ID
    def makeSub(self, oldName, newExpr):
        if self.ID == oldName.ID:
            return newExpr
        else:
            return self   
    def __str__(self):
        return self.ID
    
class Function:
    def __init__(self, variable, body):
        self.variable = variable
        self.body = body
    
    def makeSub(self, oldName, newExpr):
        return Function(self.variable, self.body.makeSub(oldName, newExpr))
    
    def eval(self, argument):
        return self.body.makeSub(self.variable, argument)
    
    def __str__(self):
        return f"LAMBDA {self.variable}.{self.body}"
    

class Application:
    def __init__(self, operator, argument):
        self.operator = operator
        self.argument = argument

    def makeSub(self, oldName, newExpr):
        return Application(self.operator.makeSub(oldName, newExpr), self.argument.makeSub(oldName, newExpr))
    
    def eval(self):
        return self.operator.eval(self.argument)
    
    def __str__(self):
        return f"({self.operator}){self.argument}"
    


x = Name("x")
y = Name("y")

xy = Function(x,y)
application = Application(xy, y)

print(application.eval())

