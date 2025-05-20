# Generated from EmployeeDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EmployeeDSLParser import EmployeeDSLParser
else:
    from EmployeeDSLParser import EmployeeDSLParser

# This class defines a complete generic visitor for a parse tree produced by EmployeeDSLParser.

class EmployeeDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EmployeeDSLParser#program.
    def visitProgram(self, ctx:EmployeeDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#statement.
    def visitStatement(self, ctx:EmployeeDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#loadStatement.
    def visitLoadStatement(self, ctx:EmployeeDSLParser.LoadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#filterStatement.
    def visitFilterStatement(self, ctx:EmployeeDSLParser.FilterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#operator.
    def visitOperator(self, ctx:EmployeeDSLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#value.
    def visitValue(self, ctx:EmployeeDSLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#aggregateStatement.
    def visitAggregateStatement(self, ctx:EmployeeDSLParser.AggregateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#aggregateFunction.
    def visitAggregateFunction(self, ctx:EmployeeDSLParser.AggregateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#sortStatement.
    def visitSortStatement(self, ctx:EmployeeDSLParser.SortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EmployeeDSLParser#printStatement.
    def visitPrintStatement(self, ctx:EmployeeDSLParser.PrintStatementContext):
        return self.visitChildren(ctx)



del EmployeeDSLParser