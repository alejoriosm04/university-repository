%{
#include <stdio.h>
#include <stdlib.h>
%}

%token L R

%%

first_production: first_production L R
				| L R first_production
				| L first_production R
				| L R
				;
%%

int main() {
    printf("Ingrese una cadena: ");
    if (yyparse() == 0) {
        printf("cadena valida\n");
    } else {
        printf("cadena invalida\n");
    }
    return 0;
}

int yylex() {
    int c = getchar();
    if (c == '(') {
        return L;
    } else if (c == ')') {
        return R;
      }
      else {
        return -1;
      }
}
