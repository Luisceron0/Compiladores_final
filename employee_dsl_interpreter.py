import json
import csv
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
        
    def visitProgram(self, ctx):
        # Process all statements
        for statement in ctx.statement():
            self.visit(statement)
        return self.data
    
    def visitLoadStatement(self, ctx):
        # Extract the CSV file path
        filename = ctx.STRING_LITERAL().getText()[1:-1]  # Remove quotes
        
        # Load CSV to pandas DataFrame
        self.data = pd.read_csv(filename)
        
        # Convert to JSON internally
        self.data_json = json.loads(self.data.to_json(orient='records'))
        return self.data
    
    def visitFilterStatement(self, ctx):
        # Handle AND / OR compositions of filters
        if ctx.AND():
            left_filters = self.visit(ctx.filterStatement(0))
            right_filters = self.visit(ctx.filterStatement(1))
            # Both filters are already processed and added
            return
            
        if ctx.OR():
            left_filters = self.visit(ctx.filterStatement(0))
            right_filters = self.visit(ctx.filterStatement(1))
            # Both filters are already processed and added
            return
        
        # Handle basic filter
        if ctx.COLUMN():
            column = ctx.STRING_LITERAL().getText()[1:-1]  # Remove quotes
            operator = self.visit(ctx.operator())
            value = self.visit(ctx.value())
            
            # Add filter to the list
            self.filters.append({
                'column': column,
                'operator': operator,
                'value': value
            })
        
        return self.filters
    
    def visitOperator(self, ctx):
        if ctx.GT(): return '>'
        if ctx.LT(): return '<'
        if ctx.GTE(): return '>='
        if ctx.LTE(): return '<='
        if ctx.EQ(): return '=='
        if ctx.NEQ(): return '!='
        if ctx.BETWEEN(): return 'between'
        
    def visitValue(self, ctx):
        if ctx.NUMBER() and not ctx.AND():
            # Single number
            return float(ctx.NUMBER().getText())
        elif ctx.STRING_LITERAL():
            # String value
            return ctx.STRING_LITERAL().getText()[1:-1]  # Remove quotes
        elif ctx.NUMBER() and ctx.AND():
            # Range for BETWEEN
            min_val = float(ctx.NUMBER(0).getText())
            max_val = float(ctx.NUMBER(1).getText())
            return [min_val, max_val]
    
    def visitAggregateStatement(self, ctx):
        aggregation_func = self.visit(ctx.aggregateFunction())
        column = ctx.STRING_LITERAL().getText()[1:-1]  # Remove quotes
        
        self.aggregations.append({
            'function': aggregation_func,
            'column': column
        })
        
        return self.aggregations
    
    def visitAggregateFunction(self, ctx):
        if ctx.COUNT(): return 'count'
        if ctx.SUM(): return 'sum'
        if ctx.AVERAGE(): return 'average'
    
    def visitSortStatement(self, ctx):
        column = ctx.STRING_LITERAL().getText()[1:-1]  # Remove quotes
        ascending = ctx.ASC() is not None
        
        self.sorting = {
            'column': column,
            'ascending': ascending
        }
        
        return self.sorting
        
    def visitPrintStatement(self, ctx):
        # Execute all accumulated operations
        result = self._execute_query()
        return result
    
    def _execute_query(self):
        """Execute all accumulated operations on the data"""
        if self.data is None:
            return "No data loaded. Use 'load' command first."
        
        # Start with original data
        filtered_data = self.data.copy()
        
        # Apply filters
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
        
        # Apply sorting if specified
        if self.sorting:
            filtered_data = filtered_data.sort_values(
                by=self.sorting['column'], 
                ascending=self.sorting['ascending']
            )
        
        # Apply aggregations
        aggregation_results = {}
        for agg in self.aggregations:
            func = agg['function']
            column = agg['column']
            
            if func == 'count':
                aggregation_results[f'count_{column}'] = len(filtered_data)
            elif func == 'sum':
                aggregation_results[f'sum_{column}'] = filtered_data[column].sum()
            elif func == 'average':
                aggregation_results[f'average_{column}'] = filtered_data[column].mean()
        
        # Prepare the results
        result = {
            'filtered_data': json.loads(filtered_data.to_json(orient='records')),
            'aggregations': aggregation_results,
            'record_count': len(filtered_data)
        }
        
        return result

def parse_and_interpret(input_string):
    # Create the lexer and parser
    input_stream = InputStream(input_string)
    lexer = EmployeeDSLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = EmployeeDSLParser(token_stream)
    
    # Parse the input
    tree = parser.program()
    
    # Create and run the interpreter
    interpreter = EmployeeDSLInterpreter()
    result = interpreter.visit(tree)
    
    return result

def main():
    # Example script
    script = '''
    load "empleados.csv";
    filter column "edad" > 25;
    aggregate count column "id_empleado";
    aggregate average column "salario";
    aggregate sum column "dias_laborados";
    print;
    '''
    
    # Parse and interpret the script
    result = parse_and_interpret(script)
    
    # Display the results
    print("Execution Result:")
    print(f"Number of records: {result['record_count']}")
    
    for agg_name, agg_value in result['aggregations'].items():
        print(f"{agg_name}: {agg_value}")
    
    # Optionally print first few records of filtered data
    if result['record_count'] > 0:
        print("\nFirst 5 records of filtered data:")
        for record in result['filtered_data'][:5]:
            print(record)

if __name__ == "__main__":
    main()
