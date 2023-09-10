#include <stdio.h>
#include <string.h>

// gcc -o bookshelf bookshelf.c -no-pie -fno-stack-protector

unsigned int cash;

void banner(){
	puts("Welcome to the Book Shelf...         _______ ");
        puts("                                    /      /,");
        puts("BookShelf Management System        /      // ");
        puts("Version 2.0                       /______//  ");
        puts("                                 (______(/   ");
        puts("Grab yourself a coffee and enjoy some books!");
}

void menu(int d){
	puts("\n1) Write a book");
	puts("2) Buy a book");
	printf("3) Write a special book (ADMINS ONLY) (%d)\n",d);
	puts("4) Check out");
	printf(" >> ");
}

void writeBook(char * book){
	memset(book,0,40);
	char audio;
	char buff[40];
	puts("Always great to see aspiring authors!");
	printf("Is this book an audiobook? (y/N) >> ");
	audio = getchar();
	if(audio != '\n')
		getchar();
	if(audio == 'y' || audio == 'Y')
		strcpy(book,"(AB): ");
	printf("Please write your book (40 chars max) >> ");
	fgets(buff,sizeof(buff),stdin);
	if(audio == 'y' || audio == 'Y')
		strcat(book,buff);
	else
		strcpy(book,buff);
	puts("Book saved!");
}

void adminBook(int debug){
	char buff[40];
	if(debug == 0){
		puts("\nUnauthorized access: admins only!\n");
		return;
	}
	puts("\nYou're an admin so I trust that you will be responsible with writing this very special book...");
	printf(" >> ");
	fgets(buff,0x100,stdin);
	puts("Book saved!");
	return;
}

int main(){
	char option;
	int debug = 0;
	char book[40];

	cash = 500;
	banner();
	while(1){
		menu(debug);
		option = getchar();
		getchar();
		switch(option){
			case '1':
				writeBook(book);
				break;
			case '2':
				puts("\nShop is closed, sorry!");
				break;
			case '3':
				adminBook(debug);
				break;
			case '4':
				puts("Bye");
				__asm__(
					"pop %rdi;"
					"ret;"
				);
				return 0;
			default:
				puts("Invalid option!");
				break;
		}
	}
}
