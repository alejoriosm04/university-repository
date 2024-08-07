import ply.lex as lex
import ply.yacc as yacc

# tokens
tokens = ['PALABRA']

# reglas
def t_PALABRA(token):
    r'[a-zA-Z ]+'
    token.value = token.value.lower()
    return token

# definición de errores lexicográficos
def t_error(token):
    print(f"Carácter no válido '{token.value[0]}'")
    token.lexer.skip(1)

# reglas de precedencia
precedence = () 

# reglas de gramática
def p_palindromo(p):
    """
    palindromo : PALABRA
               | PALABRA palindromo
    """
    cadena = p[1].replace(' ', '')
    if cadena == cadena[::-1]:
        print(f"La cadena '{p[1]}' es un palíndromo")
    else:
        print(f"La cadena '{p[1]}' no es un palíndromo")

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en entrada")

# construcción del lexer y parser
lexer = lex.lex()
parser = yacc.yacc()

# función para evaluar una cadena
def evaluar(cadena):
    resultado = parser.parse(cadena, lexer=lexer)
    return resultado

# prueba del parser con una cadena
evaluar('ana')
evaluar('anita lava la tina')
evaluar('hola mundo')
