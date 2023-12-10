 #include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
     int n;
      int n1;

    do
    {
        n = get_int("Start size: ");
    }
    while (n < 9);
    // TODO: Prompt for end size

    do
    {
        n1 = get_int("End Size: ");
    }
    while (n1 < n);

    // TODO: Calculate number of years until we reach threshold

 int count=0;
    while (n != n1)
    {
    int      a = n / 3;
        int b = n / 4;
        n = n + a - b;
        count++;
        if (n1 < n)
        {
            break;
        }
    }

    // TODO: Print number of years

    printf("Years: %i\n", count);
    return 0;
}
