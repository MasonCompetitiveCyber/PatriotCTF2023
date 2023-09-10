#include <stdio.h>
#include <stdlib.h>

// gcc -o printshift printshift.c -no-pie

void win(){
	FILE * flag = fopen("flag.txt","r");
	if(flag == NULL){
		printf("\nFailed to open flag file! Please contact an organizer.\n");
		exit(1);
	}
	char c = fgetc(flag);
	while(c != EOF){
		printf("%c",c);
		c = fgetc(flag);
	}
	fclose(flag);
}

int main(){
	char buff[100];
        printf("\nWelcome to the Print Shop!\n");
        printf("\nWhat would you like to print? >> ");
        fgets(buff,sizeof(buff),stdin);
        printf("\nThank you for your buisness!\n\n");
        printf(buff);
        exit(0);
}
