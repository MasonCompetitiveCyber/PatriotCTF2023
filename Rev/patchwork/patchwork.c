#include <stdio.h>

#define HIDE_LETTER(a)   (a) + 0x50
#define UNHIDE_STRING(str)  do { char * ptr = str ; while (*ptr) *ptr++ -= 0x50; } while(0)
#define HIDE_STRING(str)  do {char * ptr = str ; while (*ptr) *ptr++ += 0x50;} while(0)

int main()
{

    

    int jump = 0;
    printf("Trampolines are quite fun!; I love to jump! \n");
    printf("You should try jumping too! It\'ll sure be more fun than reversing the flag manually.\n");

    if (jump) {
        give_flag();
    }

    return 0;
}

int give_flag()
{
	// store the "secret password" as mangled byte array in binary
    char flag[] = { HIDE_LETTER('P') , HIDE_LETTER('C') , HIDE_LETTER('T') , HIDE_LETTER('F') , HIDE_LETTER('{')
, HIDE_LETTER('J') , HIDE_LETTER('u') , HIDE_LETTER('M') , HIDE_LETTER('p') , HIDE_LETTER('_'),
        HIDE_LETTER('u') ,HIDE_LETTER('P') ,HIDE_LETTER('_') ,HIDE_LETTER('4') ,HIDE_LETTER('n'), HIDE_LETTER('d'),
        HIDE_LETTER('_'), HIDE_LETTER('g'), HIDE_LETTER('3'), HIDE_LETTER('t'), HIDE_LETTER('_'), HIDE_LETTER('d'),
        HIDE_LETTER('0'),HIDE_LETTER('W'),HIDE_LETTER('n'), HIDE_LETTER('}'),'\0' };
    UNHIDE_STRING(flag);  // unmangle the string in-place
    printf("%s\n", flag);
    HIDE_STRING(flag);  //mangle back
}