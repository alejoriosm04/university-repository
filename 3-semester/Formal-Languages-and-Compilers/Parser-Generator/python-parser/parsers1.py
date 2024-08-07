import ply.lex as lex
import ply.yacc as yacc

# Definir tokens
tokens = (
    'TRUE',
    'FALSE',
    'NOT',
    'AND',
    'OR',
    'PARENTESIS_IZQUIERDO',
    'PARENTESIS_DERECHO',
)

# Expresiones regulares para los tokens
t_TRUE = r'TRUE'                    # La constante booleana true
t_FALSE = r'FALSE'                  # La constante booleana false
t_NOT = r'NOT'                      # El operador booleano not
t_AND = r'AND'                      # El operador booleano and
t_OR = r'OR'                        # El operador booleano or
t_PARENTESIS_IZQUIERDO = r'\('      # El paréntesis izquierdo '('
t_PARENTESIS_DERECHO = r'\)'        # El paréntesis derecho ')'

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Caracter inesperado '%s'" % t.value[0])
    t.lexer.skip(1)

# Reglas de producción para el parser
def p_expresion_not(p):
    'expresion : NOT expresion'
    p[0] = not p[2]

def p_expresion_and(p):
    'expresion : expresion AND expresion'
    p[0] = p[1] and p[3]

def p_expresion_or(p):
    'expresion : expresion OR expresion'
    p[0] = p[1] or p[3]

def p_expresion_parentesis(p):
    'expresion : PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO'
    p[0] = p[2]

def p_expresion_true(p):
    'expresion : TRUE'
    p[0] = True

def p_expresion_false(p):
    'expresion : FALSE'
    p[0] = False

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
evaluar("TRUE AND FALSE") #salida
#evaluar("TRUE AND (FALSE OR TRUE)") #salida
#evaluar("TRUE AND (FALSE OR TRUE) AND NOT FALSE") #salida
evaluar("FALSE FALSE") #salida
