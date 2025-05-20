import json
import pandas as pd
from antlr4 import *
from EmployeeDSLLexer import EmployeeDSLLexer
from EmployeeDSLParser import EmployeeDSLParser
from EmployeeDSLVisitor import EmployeeDSLVisitor

class EmployeeDSLInterpreter(EmployeeDSLVisitor):
    def __init__(self):
        self.data = None
        self.filters = []
        self.aggregations = []
        self.sorting = None
        self.last_result = None

    def visitProgram(self, ctx):
        # Visit all statements
        result = None
        for statement in ctx.statement():
            res = self.visit(statement)
            # Capture the result of print statement
            if isinstance(res, dict):
                result = res
        # If no print statement, prepare a default result
        if result is None:
            result = self._execute_query()
        return result

    def visitLoadStatement(self, ctx):
        filename = ctx.STRING_LITERAL().getText()[1:-1]
        self.data = pd.read_csv(filename)
        return None

    def visitFilterStatement(self, ctx):
        # Handle AND / OR compositions of filters
        if ctx.AND():
            left_filters = self.visit(ctx.filterStatement(0))
            right_filters = self.visit(ctx.filterStatement(1))
            combined_filters = []
            if left_filters:
                combined_filters.extend(left_filters)
            if right_filters:
                combined_filters.extend(right_filters)
            self.filters.extend(combined_filters)
            return combined_filters

        if ctx.OR():
            left_filters = self.visit(ctx.filterStatement(0))
            right_filters = self.visit(ctx.filterStatement(1))
            combined_filters = []
            if left_filters:
                combined_filters.extend(left_filters)
            if right_filters:
                combined_filters.extend(right_filters)
            self.filters.extend(combined_filters)
            return combined_filters

        # Basic filter
        if ctx.COLUMN() and ctx.STRING_LITERAL():
            column = ctx.STRING_LITERAL().getText()[1:-1]
            operator = self.visit(ctx.operator())
            value = self.visit(ctx.value())
            filter_obj = {
                'column': column,
                'operator': operator,
                'value': value
            }
            self.filters.append(filter_obj)
            return [filter_obj]
        return []

    def visitOperator(self, ctx):
        if ctx.GT(): return '>'
        if ctx.LT(): return '<'
        if ctx.GTE(): return '>='
        if ctx.LTE(): return '<='
        if ctx.EQ(): return '=='
        if ctx.NEQ(): return '!='
        if ctx.BETWEEN(): return 'between'
        return None

    def visitValue(self, ctx):
        if ctx.NUMBER() and not ctx.AND():
            number_token = ctx.NUMBER()
            if isinstance(number_token, list):
                return float(number_token[0].getText())
            else:
                return float(number_token.getText())
        elif ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()[1:-1]
        elif ctx.NUMBER() and ctx.AND():
            min_val = float(ctx.NUMBER(0).getText())
            max_val = float(ctx.NUMBER(1).getText())
            return [min_val, max_val]
        return None

    def visitAggregateStatement(self, ctx):
        aggregation_func = self.visit(ctx.aggregateFunction())
        column = None
        for child in ctx.getChildren():
            text = child.getText()
            if text == 'column':
                siblings = list(ctx.getChildren())
                idx = siblings.index(child)
                if idx + 1 < len(siblings):
                    next_child = siblings[idx + 1]
                    if next_child.getSymbol() and next_child.getSymbol().type == EmployeeDSLLexer.STRING_LITERAL:
                        column = next_child.getText()[1:-1]
                        break
        if column is None:
            if ctx.STRING_LITERAL():
                column = ctx.STRING_LITERAL().getText()[1:-1]
        self.aggregations.append({
            'function': aggregation_func,
            'column': column
        })
        return None

    def visitAggregateFunction(self, ctx):
        if ctx.COUNT(): return 'count'
        if ctx.SUM(): return 'sum'
        if ctx.AVERAGE(): return 'average'
        return None

    def visitSortStatement(self, ctx):
        column = ctx.STRING_LITERAL().getText()[1:-1]
        ascending = ctx.ASC() is not None
        self.sorting = {
            'column': column,
            'ascending': ascending
        }
        return None

    def visitPrintStatement(self, ctx):
        result = self._execute_query()
        self.last_result = result
        return result

    def _execute_query(self):
        if self.data is None:
            return {
                'filtered_data': [],
                'aggregations': {},
                'record_count': 0
            }
        filtered_data = self.data.copy()
        for filter_op in self.filters:
            column = filter_op['column']
            operator = filter_op['operator']
            value = filter_op['value']
            if operator == '>':
                filtered_data = filtered_data[filtered_data[column] > value]
            elif operator == '<':
                filtered_data = filtered_data[filtered_data[column] < value]
            elif operator == '>=':
                filtered_data = filtered_data[filtered_data[column] >= value]
            elif operator == '<=':
                filtered_data = filtered_data[filtered_data[column] <= value]
            elif operator == '==':
                filtered_data = filtered_data[filtered_data[column] == value]
            elif operator == '!=':
                filtered_data = filtered_data[filtered_data[column] != value]
            elif operator == 'between':
                min_val, max_val = value
                filtered_data = filtered_data[(filtered_data[column] >= min_val) & (filtered_data[column] <= max_val)]
        if self.sorting:
            filtered_data = filtered_data.sort_values(
                by=self.sorting['column'],
                ascending=self.sorting['ascending']
            )
        aggregation_results = {}
        for agg in self.aggregations:
            func = agg.get('function')
            column = agg.get('column')
            if func == 'count':
                aggregation_results[f'count_{column}'] = len(filtered_data)
            elif func == 'sum':
                aggregation_results[f'sum_{column}'] = filtered_data[column].sum()
            elif func == 'average':
                aggregation_results[f'average_{column}'] = filtered_data[column].mean()
        result = {
            'filtered_data': json.loads(filtered_data.to_json(orient='records')),
            'aggregations': aggregation_results,
            'record_count': len(filtered_data)
        }
        return result

def parse_and_interpret(input_string):
    input_stream = InputStream(input_string)
    lexer = EmployeeDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EmployeeDSLParser(token_stream)
    tree = parser.program()
    interpreter = EmployeeDSLInterpreter()
    result = interpreter.visit(tree)
    return result
