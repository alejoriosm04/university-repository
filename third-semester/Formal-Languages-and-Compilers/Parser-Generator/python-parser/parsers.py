import ply.lex as lex 
import ply.yacc as yacc

# Definir tokens
tokens = (
    'NUMERO', # Un número entero
    'SUMA', # El signo de suma '+'
    'RESTA', # El signo de resta '-'
    'MULTIPLICACION', # El signo de multiplicación '*'
    'DIVISION', # El signo de división '/'
    'PARENTESIS_IZQUIERDO', # El paréntesis izquierdo '('
    'PARENTESIS_DERECHO', # El paréntesis derecho ')'
)

# Expresiones regulares para los tokens
t_NUMERO = r'\d+'                # Un número entero
t_SUMA = r'\+'                   # El signo de suma '+'
t_RESTA = r'\-'                   # El signo de resta '-'
t_MULTIPLICACION = r'\*'         # El signo de multiplicación '*'
t_DIVISION = r'/'                # El signo de división '/'
t_PARENTESIS_IZQUIERDO = r'\('   # El paréntesis izquierdo '('
t_PARENTESIS_DERECHO = r'\)'     # El paréntesis derecho ')'

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t' 

# Manejo de errores
def t_error(t): 
    print("Caracter inesperado '%s'" % t.value[0]) 
    t.lexer.skip(1)

# Reglas de producción para el parser
def p_expresion_suma(p):
    'expresion : termino SUMA expresion'
    p[0] = p[1] + p[3]

def p_expresion_resta(p): 
    'expresion : termino RESTA expresion' 
    p[0] = p[1] - p[3]

def p_expresion_termino(p):
    'expresion : termino'
    p[0] = p[1]

def p_termino_multiplicacion(p):
    'termino : factor MULTIPLICACION termino'
    p[0] = p[1] * p[3]

def p_termino_division(p):
    'termino : factor DIVISION termino'
    p[0] = p[1] / p[3]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]

def p_factor_parentesis(p):
    'factor : PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO'
    p[0] = p[2]

def p_factor_numero(p):
    'factor : NUMERO'
    p[0] = int(p[1])

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

# Crear el lexer y el parser
lexer = lex.lex()
parser = yacc.yacc()

# Función para evaluar una cadena de entrada
def evaluar(expresion):
    resultado = parser.parse(expresion)
    if resultado is not None:
        print(f"La expresión '{expresion}' es válida y su resultado es {resultado}")
    else:
        print(f"La expresión '{expresion}' es inválida")

# Evaluar una cadena de entrada
evaluar('3 + 4 * (2 - 1)') 
evaluar('3 + 4 * (2 - 1)')
evaluar('5 - 3 * 2')
