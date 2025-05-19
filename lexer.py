import re

def lex(code):
    token_specification = [
        ('NUMBER',   r'\d+'),
        ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
        ('EQUALS',   r'='),
        ('PLUS',     r'\+'),
        ('MINUS',    r'-'),
        ('MULT',     r'\*'),
        ('DIV',      r'/'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('SEMI',     r';'),
        ('SKIP',     r'[ \t\n]+'),  # Skip spaces and tabs
        ('MISMATCH', r'.'),         # Any other character
    ]

    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    tokens = []

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        else:
            tokens.append((kind, value))

    return tokens