#include <stdio.h>
#include <string.h>

void outputFlag() {
    char flag[35];
    FILE* pctfFlag = fopen("flag.txt", "r");

    if (pctfFlag == NULL) {
        printf("Unable to find flag.txt :(");
    } else {
        fgets(flag, 35, pctfFlag);
        printf("%s", flag);
    }
    fclose(pctfFlag);
}

int check(){
    char input[300];
    char favAnimal[8] = "Giraffe";
    int priv = 0;
    
    printf("Input guess: ");
    gets(input);

    if(strcmp(input, favAnimal)) {
        printf("ERRR! Wrong!\n");
    }
    else {
        printf("That's not my favorite animal... I promise!\n");
    }
    if(priv) {
        printf("I wasn't able to trick you...\n");
        outputFlag();
    }
}

int main(){
    printf("Hello there, friend! Can you guess my favorite animal?\n");
    check();
    return 0;
}
