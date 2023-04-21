%{
#include <ctype.h>
%}
%token DIGITO

%%
linea   : expr '\n' { printf("%d\n", $1);}
        ;
expr    : expr '+' term { $$ = $1 + $3;}
        | term
        ;
term    : term '*' factor { $$ = $1 * $3;}
        | factor
        ;
factor  : '(' expr ')' { $$ = $2; }
        | DIGITO
        ;
%%

yylex() {
    int c;
    c = getchar();
    if (isdigit(c)) {
        yylval = c-'0';
        return DIGITO;
    }
    return c;
}