# import ply.lex as lex
# import ply.yacc as yacc

# # ------------------ LEXER ------------------

# tokens = (
#     'NUMBER',
#     'PLUS', 'MINUS',
#     'TIMES', 'DIVIDE',
#     'LPAREN', 'RPAREN',
# )

# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
# t_ignore  = ' \t'

# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# def t_error(t):
#     raise Exception(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()

# # ------------------ PARSER ------------------

# precedence = (
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
# )

# # Tree generator rules
# def p_expression_binop(p):
#     '''expression : expression PLUS expression
#                   | expression MINUS expression
#                   | expression TIMES expression
#                   | expression DIVIDE expression'''
#     p[0] = {
#         'type': p[2],
#         'left': p[1],
#         'right': p[3]
#     }

# def p_expression_group(p):
#     'expression : LPAREN expression RPAREN'
#     p[0] = p[2]

# def p_expression_number(p):
#     'expression : NUMBER'
#     p[0] = {'type': 'number', 'value': p[1]}

# def p_error(p):
#     raise Exception(f"Syntax error at '{p.value}'" if p else "Syntax error at EOF")

# parser = yacc.yacc()

# def generate_parse_tree(expression):
#     return parser.parse(expression)