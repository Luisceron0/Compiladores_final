grammar EmployeeDSL;

// Parser rules
program : statement+ EOF ;

statement
    : loadStatement
    | filterStatement
    | aggregateStatement
    | printStatement
    | sortStatement
    ;

loadStatement : LOAD STRING_LITERAL SEMICOLON ;

filterStatement
    : FILTER COLUMN STRING_LITERAL operator value SEMICOLON
    | filterStatement AND filterStatement
    | filterStatement OR filterStatement
    ;

operator : GT | LT | GTE | LTE | EQ | NEQ | BETWEEN ;

value
    : NUMBER                                     // Para filtros con números
    | STRING_LITERAL                             // Para filtros con texto
    | NUMBER AND NUMBER                          // Para BETWEEN
    ;

aggregateStatement
    : AGGREGATE aggregateFunction COLUMN STRING_LITERAL SEMICOLON
    ;

aggregateFunction
    : COUNT
    | SUM
    | AVERAGE
    ;

sortStatement : SORT COLUMN STRING_LITERAL (ASC | DESC) SEMICOLON ;

printStatement : PRINT SEMICOLON ;

// Lexer rules
LOAD : 'load' ;
FILTER : 'filter' ;
COLUMN : 'column' ;
AGGREGATE : 'aggregate' ;
PRINT : 'print' ;
SORT : 'sort' ;
ASC : 'asc' ;
DESC : 'desc' ;

// Aggregate functions
COUNT : 'count' ;
SUM : 'sum' ;
AVERAGE : 'average' ;

// Operators
GT : '>' ;
LT : '<' ;
GTE : '>=' ;
LTE : '<=' ;
EQ : '==' ;
NEQ : '!=' ;
BETWEEN : 'between' ;

// Logical operators
AND : 'and' ;
OR : 'or' ;

// Basic types
NUMBER : [0-9]+ ('.' [0-9]+)? ;
STRING_LITERAL : '"' (~["\r\n])* '"' ;
SEMICOLON : ';' ;

// Skip whitespace and comments
WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
