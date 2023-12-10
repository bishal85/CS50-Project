#include <cs50.h>
#include <stdio.h>

int main(void)
{ // declare variables
    int i, k, j, n;
    do
    {
        n = get_int("Height: "); // promt user to input

      }
    while (n < 0 || n > 8 || n == 0);
    for (i = 1; i <= n; i++) // inner loop
    {
        for (j = i; j < n; j++) // outer loop
        {
            printf(" "); // print space
        }
        for (k = 1; k <= i; k++)
        {
            printf("#"); // print the Star
        }
        printf("\n");
    }
    return 0;

}
