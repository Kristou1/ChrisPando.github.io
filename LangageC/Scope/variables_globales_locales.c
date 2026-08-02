/* Les variables peuvent avoir une portée globale.
Cela signifie qu'elles persistent entre toutes les fonctions.
Elles sont définies en début de code, hors de toute fonction.*/

#include <stdio.h>

int j = 42; // j est une variable globale.

void func3(){
    int i = 11, j = 13; // j est une variable locale à func3.
    printf(
        "\t\t\t[in func3] i = %d (%p), j = %d (%p)\n",
        i,
        (void *)&i,
        j,
        (void *)&j
    );
}

void func2(){
    int i = 7;
    printf(
        "\t\t[in func2] i = %d (%p), j = %d (%p)\n",
        i,
        (void *)&i,
        j,
        (void *)&j
    );

    func3();

    printf(
        "\t\t[back in func2] i = %d (%p), j = %d (%p)\n",
        i,
        (void *)&i,
        j,
        (void *)&j
    );
}

void func1(){
    int i = 5;
    printf(
        "\t[in func1] i = %d (%p), j = %d (%p)\n",
        i,
        (void *)&i,
        j,
        (void *)&j
    );

    func2();

    printf(
        "\t[back in func1] i = %d (%p), j = %d (%p)\n",
        i,
        (void *)&i,
        j,
        (void *)&j
    );
}

int main(void){
    int i = 3;
    printf(
        "[in main] i = %d (%p), j = %d (%p)\n",
        i,
        (void *)&i,
        j,
        (void *)&j
    );

    func1();

    printf(
        "[back in main] i = %d (%p), j = %d (%p)\n",
        i,
        (void *)&i,
        j,
        (void *)&j
    );
}
