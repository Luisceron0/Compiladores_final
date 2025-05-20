# Generated from EmployeeDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EmployeeDSLParser import EmployeeDSLParser
else:
    from EmployeeDSLParser import EmployeeDSLParser

# This class defines a complete listener for a parse tree produced by EmployeeDSLParser.
class EmployeeDSLListener(ParseTreeListener):

    # Enter a parse tree produced by EmployeeDSLParser#program.
    def enterProgram(self, ctx:EmployeeDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#program.
    def exitProgram(self, ctx:EmployeeDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#statement.
    def enterStatement(self, ctx:EmployeeDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#statement.
    def exitStatement(self, ctx:EmployeeDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#loadStatement.
    def enterLoadStatement(self, ctx:EmployeeDSLParser.LoadStatementContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#loadStatement.
    def exitLoadStatement(self, ctx:EmployeeDSLParser.LoadStatementContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#filterStatement.
    def enterFilterStatement(self, ctx:EmployeeDSLParser.FilterStatementContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#filterStatement.
    def exitFilterStatement(self, ctx:EmployeeDSLParser.FilterStatementContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#operator.
    def enterOperator(self, ctx:EmployeeDSLParser.OperatorContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#operator.
    def exitOperator(self, ctx:EmployeeDSLParser.OperatorContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#value.
    def enterValue(self, ctx:EmployeeDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#value.
    def exitValue(self, ctx:EmployeeDSLParser.ValueContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#aggregateStatement.
    def enterAggregateStatement(self, ctx:EmployeeDSLParser.AggregateStatementContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#aggregateStatement.
    def exitAggregateStatement(self, ctx:EmployeeDSLParser.AggregateStatementContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#aggregateFunction.
    def enterAggregateFunction(self, ctx:EmployeeDSLParser.AggregateFunctionContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#aggregateFunction.
    def exitAggregateFunction(self, ctx:EmployeeDSLParser.AggregateFunctionContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#sortStatement.
    def enterSortStatement(self, ctx:EmployeeDSLParser.SortStatementContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#sortStatement.
    def exitSortStatement(self, ctx:EmployeeDSLParser.SortStatementContext):
        pass


    # Enter a parse tree produced by EmployeeDSLParser#printStatement.
    def enterPrintStatement(self, ctx:EmployeeDSLParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by EmployeeDSLParser#printStatement.
    def exitPrintStatement(self, ctx:EmployeeDSLParser.PrintStatementContext):
        pass



del EmployeeDSLParser