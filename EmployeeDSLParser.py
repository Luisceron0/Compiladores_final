# Generated from EmployeeDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,9,3,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,65,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,0,1,6,10,0,2,4,6,8,
        10,12,14,16,18,0,3,1,0,12,18,1,0,9,11,1,0,7,8,82,0,21,1,0,0,0,2,
        32,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,57,1,0,0,0,10,64,1,0,0,0,
        12,66,1,0,0,0,14,72,1,0,0,0,16,74,1,0,0,0,18,80,1,0,0,0,20,22,3,
        2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,
        25,1,0,0,0,25,26,5,0,0,1,26,1,1,0,0,0,27,33,3,4,2,0,28,33,3,6,3,
        0,29,33,3,12,6,0,30,33,3,18,9,0,31,33,3,16,8,0,32,27,1,0,0,0,32,
        28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,
        0,34,35,5,1,0,0,35,36,5,22,0,0,36,37,5,23,0,0,37,5,1,0,0,0,38,39,
        6,3,-1,0,39,40,5,2,0,0,40,41,5,3,0,0,41,42,5,22,0,0,42,43,3,8,4,
        0,43,44,3,10,5,0,44,45,5,23,0,0,45,54,1,0,0,0,46,47,10,2,0,0,47,
        48,5,19,0,0,48,53,3,6,3,3,49,50,10,1,0,0,50,51,5,20,0,0,51,53,3,
        6,3,2,52,46,1,0,0,0,52,49,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,
        55,1,0,0,0,55,7,1,0,0,0,56,54,1,0,0,0,57,58,7,0,0,0,58,9,1,0,0,0,
        59,65,5,21,0,0,60,65,5,22,0,0,61,62,5,21,0,0,62,63,5,19,0,0,63,65,
        5,21,0,0,64,59,1,0,0,0,64,60,1,0,0,0,64,61,1,0,0,0,65,11,1,0,0,0,
        66,67,5,4,0,0,67,68,3,14,7,0,68,69,5,3,0,0,69,70,5,22,0,0,70,71,
        5,23,0,0,71,13,1,0,0,0,72,73,7,1,0,0,73,15,1,0,0,0,74,75,5,6,0,0,
        75,76,5,3,0,0,76,77,5,22,0,0,77,78,7,2,0,0,78,79,5,23,0,0,79,17,
        1,0,0,0,80,81,5,5,0,0,81,82,5,23,0,0,82,19,1,0,0,0,5,23,32,52,54,
        64
    ]

class EmployeeDSLParser ( Parser ):

    grammarFileName = "EmployeeDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'filter'", "'column'", "'aggregate'", 
                     "'print'", "'sort'", "'asc'", "'desc'", "'count'", 
                     "'sum'", "'average'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'between'", "'and'", "'or'", "<INVALID>", 
                     "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "FILTER", "COLUMN", "AGGREGATE", 
                      "PRINT", "SORT", "ASC", "DESC", "COUNT", "SUM", "AVERAGE", 
                      "GT", "LT", "GTE", "LTE", "EQ", "NEQ", "BETWEEN", 
                      "AND", "OR", "NUMBER", "STRING_LITERAL", "SEMICOLON", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loadStatement = 2
    RULE_filterStatement = 3
    RULE_operator = 4
    RULE_value = 5
    RULE_aggregateStatement = 6
    RULE_aggregateFunction = 7
    RULE_sortStatement = 8
    RULE_printStatement = 9

    ruleNames =  [ "program", "statement", "loadStatement", "filterStatement", 
                   "operator", "value", "aggregateStatement", "aggregateFunction", 
                   "sortStatement", "printStatement" ]

    EOF = Token.EOF
    LOAD=1
    FILTER=2
    COLUMN=3
    AGGREGATE=4
    PRINT=5
    SORT=6
    ASC=7
    DESC=8
    COUNT=9
    SUM=10
    AVERAGE=11
    GT=12
    LT=13
    GTE=14
    LTE=15
    EQ=16
    NEQ=17
    BETWEEN=18
    AND=19
    OR=20
    NUMBER=21
    STRING_LITERAL=22
    SEMICOLON=23
    WS=24
    COMMENT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EmployeeDSLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmployeeDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(EmployeeDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = EmployeeDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 118) != 0)):
                    break

            self.state = 25
            self.match(EmployeeDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStatement(self):
            return self.getTypedRuleContext(EmployeeDSLParser.LoadStatementContext,0)


        def filterStatement(self):
            return self.getTypedRuleContext(EmployeeDSLParser.FilterStatementContext,0)


        def aggregateStatement(self):
            return self.getTypedRuleContext(EmployeeDSLParser.AggregateStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(EmployeeDSLParser.PrintStatementContext,0)


        def sortStatement(self):
            return self.getTypedRuleContext(EmployeeDSLParser.SortStatementContext,0)


        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = EmployeeDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.loadStatement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.filterStatement(0)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.aggregateStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.printStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.sortStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(EmployeeDSLParser.LOAD, 0)

        def STRING_LITERAL(self):
            return self.getToken(EmployeeDSLParser.STRING_LITERAL, 0)

        def SEMICOLON(self):
            return self.getToken(EmployeeDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_loadStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStatement" ):
                listener.enterLoadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStatement" ):
                listener.exitLoadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStatement" ):
                return visitor.visitLoadStatement(self)
            else:
                return visitor.visitChildren(self)




    def loadStatement(self):

        localctx = EmployeeDSLParser.LoadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(EmployeeDSLParser.LOAD)
            self.state = 35
            self.match(EmployeeDSLParser.STRING_LITERAL)
            self.state = 36
            self.match(EmployeeDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(EmployeeDSLParser.FILTER, 0)

        def COLUMN(self):
            return self.getToken(EmployeeDSLParser.COLUMN, 0)

        def STRING_LITERAL(self):
            return self.getToken(EmployeeDSLParser.STRING_LITERAL, 0)

        def operator(self):
            return self.getTypedRuleContext(EmployeeDSLParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(EmployeeDSLParser.ValueContext,0)


        def SEMICOLON(self):
            return self.getToken(EmployeeDSLParser.SEMICOLON, 0)

        def filterStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EmployeeDSLParser.FilterStatementContext)
            else:
                return self.getTypedRuleContext(EmployeeDSLParser.FilterStatementContext,i)


        def AND(self):
            return self.getToken(EmployeeDSLParser.AND, 0)

        def OR(self):
            return self.getToken(EmployeeDSLParser.OR, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_filterStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStatement" ):
                listener.enterFilterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStatement" ):
                listener.exitFilterStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStatement" ):
                return visitor.visitFilterStatement(self)
            else:
                return visitor.visitChildren(self)



    def filterStatement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = EmployeeDSLParser.FilterStatementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_filterStatement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(EmployeeDSLParser.FILTER)
            self.state = 40
            self.match(EmployeeDSLParser.COLUMN)
            self.state = 41
            self.match(EmployeeDSLParser.STRING_LITERAL)
            self.state = 42
            self.operator()
            self.state = 43
            self.value()
            self.state = 44
            self.match(EmployeeDSLParser.SEMICOLON)
            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = EmployeeDSLParser.FilterStatementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_filterStatement)
                        self.state = 46
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 47
                        self.match(EmployeeDSLParser.AND)
                        self.state = 48
                        self.filterStatement(3)
                        pass

                    elif la_ == 2:
                        localctx = EmployeeDSLParser.FilterStatementContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_filterStatement)
                        self.state = 49
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 50
                        self.match(EmployeeDSLParser.OR)
                        self.state = 51
                        self.filterStatement(2)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(EmployeeDSLParser.GT, 0)

        def LT(self):
            return self.getToken(EmployeeDSLParser.LT, 0)

        def GTE(self):
            return self.getToken(EmployeeDSLParser.GTE, 0)

        def LTE(self):
            return self.getToken(EmployeeDSLParser.LTE, 0)

        def EQ(self):
            return self.getToken(EmployeeDSLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(EmployeeDSLParser.NEQ, 0)

        def BETWEEN(self):
            return self.getToken(EmployeeDSLParser.BETWEEN, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = EmployeeDSLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 520192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(EmployeeDSLParser.NUMBER)
            else:
                return self.getToken(EmployeeDSLParser.NUMBER, i)

        def STRING_LITERAL(self):
            return self.getToken(EmployeeDSLParser.STRING_LITERAL, 0)

        def AND(self):
            return self.getToken(EmployeeDSLParser.AND, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = EmployeeDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(EmployeeDSLParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(EmployeeDSLParser.STRING_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(EmployeeDSLParser.NUMBER)
                self.state = 62
                self.match(EmployeeDSLParser.AND)
                self.state = 63
                self.match(EmployeeDSLParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATE(self):
            return self.getToken(EmployeeDSLParser.AGGREGATE, 0)

        def aggregateFunction(self):
            return self.getTypedRuleContext(EmployeeDSLParser.AggregateFunctionContext,0)


        def COLUMN(self):
            return self.getToken(EmployeeDSLParser.COLUMN, 0)

        def STRING_LITERAL(self):
            return self.getToken(EmployeeDSLParser.STRING_LITERAL, 0)

        def SEMICOLON(self):
            return self.getToken(EmployeeDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_aggregateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStatement" ):
                listener.enterAggregateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStatement" ):
                listener.exitAggregateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStatement" ):
                return visitor.visitAggregateStatement(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStatement(self):

        localctx = EmployeeDSLParser.AggregateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aggregateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(EmployeeDSLParser.AGGREGATE)
            self.state = 67
            self.aggregateFunction()
            self.state = 68
            self.match(EmployeeDSLParser.COLUMN)
            self.state = 69
            self.match(EmployeeDSLParser.STRING_LITERAL)
            self.state = 70
            self.match(EmployeeDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(EmployeeDSLParser.COUNT, 0)

        def SUM(self):
            return self.getToken(EmployeeDSLParser.SUM, 0)

        def AVERAGE(self):
            return self.getToken(EmployeeDSLParser.AVERAGE, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_aggregateFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFunction" ):
                listener.enterAggregateFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFunction" ):
                listener.exitAggregateFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFunction" ):
                return visitor.visitAggregateFunction(self)
            else:
                return visitor.visitChildren(self)




    def aggregateFunction(self):

        localctx = EmployeeDSLParser.AggregateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aggregateFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SORT(self):
            return self.getToken(EmployeeDSLParser.SORT, 0)

        def COLUMN(self):
            return self.getToken(EmployeeDSLParser.COLUMN, 0)

        def STRING_LITERAL(self):
            return self.getToken(EmployeeDSLParser.STRING_LITERAL, 0)

        def SEMICOLON(self):
            return self.getToken(EmployeeDSLParser.SEMICOLON, 0)

        def ASC(self):
            return self.getToken(EmployeeDSLParser.ASC, 0)

        def DESC(self):
            return self.getToken(EmployeeDSLParser.DESC, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_sortStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortStatement" ):
                listener.enterSortStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortStatement" ):
                listener.exitSortStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortStatement" ):
                return visitor.visitSortStatement(self)
            else:
                return visitor.visitChildren(self)




    def sortStatement(self):

        localctx = EmployeeDSLParser.SortStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sortStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EmployeeDSLParser.SORT)
            self.state = 75
            self.match(EmployeeDSLParser.COLUMN)
            self.state = 76
            self.match(EmployeeDSLParser.STRING_LITERAL)
            self.state = 77
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 78
            self.match(EmployeeDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(EmployeeDSLParser.PRINT, 0)

        def SEMICOLON(self):
            return self.getToken(EmployeeDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return EmployeeDSLParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = EmployeeDSLParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(EmployeeDSLParser.PRINT)
            self.state = 81
            self.match(EmployeeDSLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.filterStatement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def filterStatement_sempred(self, localctx:FilterStatementContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




