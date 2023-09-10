#include <stdio.h>
#include <string.h>

// gcc -o bookshelf bookshelf.c -no-pie -fno-stack-protector

unsigned int cash;

void banner(){
	puts("Welcome to the Book Shelf...         _______ ");
        puts("                                    /      /,");
        puts("BookShelf Management System        /      // ");
        puts("Version 1.0                       /______//  ");
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

void buyBook(){
	char option;
	puts("Want to buy an adventure on paperback?");
	puts("Here's what we have in stock");
	puts("======================================");
	printf("|Cash balance: $%u|\n",cash);
	puts("1) The Catcher in the ROP - $300");
	puts("2) The Great Hacksby - $425");
	puts("3) The Address of puts() - $99999999");
	puts("======================================");
	printf("What do you want to read? >> ");
	option = getchar();
	if(option != '\n')
		getchar();
	switch(option){
		case '1':
			if(cash >= 300){
				cash -= 300;
				printf("A restless hacker named Holden Codefield discovered ROP and became obsessed with its power. He saw himself as a catcher in the ROP, navigating through memory addresses to seize control. His place in the world soon to reveal. The End.\n");
			}else
				puts("You don't have enough cash!");
			break;
		case '2':
			if(cash >= 425){
				cash -= 425;
				printf("In the midst of the Roaring Twenties, extravagant parties corrupted Jay Gatsby's memory. Even with corrupted memory, Gatsby sought to change his past, but realized he'd never be able to find an exploit that rewrites the shattered dreams of lost love. The End.\n");
			}else
				puts("You don't have enough cash!");
			break;
		case '3':
			if(cash >= 99999999){
				printf("In the realm of bits and bytes, the audacious CTF player searched and searched, seeking something useful for their intellectual shenanigans. At long last, they had finally found it. For in the distance, in all it's glory %p rested in slumber, it's image telling a story. The End.\n",puts);
			}else
				puts("You don't have enough cash!");
			break;
		default:
			puts("\nInvalid option!\n");
			buyBook();
			return;
	}
	printf("\nThanks for you're buisness, would you like to leave a tip? (y/N) >> ");
	option = getchar();
	if(option != '\n')
		getchar();
	if(option == 'Y' || option == 'y'){
		puts("\nYay! Thank you!");
		cash -= 10U;
		return;
	}
	puts("\nOh... ok");
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
				buyBook();
				break;
			case '3':
				adminBook(debug);
				break;
			case '4':
				puts("Bye");
				return 0;
			default:
				puts("Invalid option!");
				break;
		}
	}
}
