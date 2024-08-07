%{
#include <stdio.h>
#include <stdlib.h>
%}

%token A B C D

%%

first_production: second_production third_production fourth_production
          | second_production fourth_production
		  | third_production fourth_production
		  | fourth_production
          ;
second_production: A second_production B
          | A B
          ;
third_production:  B third_production C
          | B C
          ;
fourth_production: D fourth_production
          | D
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
    if (c == '0') {
        return A;
    } else if (c == '1') {
        return B;
      }
      else if (c == '2') {
        return C;
      }
	  else if (c == '3') {
		return D;
	  }
      else {
        return -1;
      }
}
