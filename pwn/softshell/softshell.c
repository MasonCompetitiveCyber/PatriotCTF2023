#define _GNU_SOURCE
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// gcc -o softshell softshell.c -w

__attribute__((constructor)) void ignore_me(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

typedef struct command{
	char * tag;
	char * cmd;
	char ** args;
	int argslen;
	int index;
	struct command * next;
} command;

int currIndex __attribute__((section(".data"))) = 0;
char  allowed[] __attribute__((section(".data"))) = "/usr/games/cowsay moooo";

void banner(){
	puts("               __ _       _          _ _ ");
	puts("              / _| |     | |        | | |");
	puts("    ___  ___ | |_| |_ ___| |__   ___| | |");
	puts("   / __|/ _ \\|  _| __/ __| '_ \\ / _ \\ | |");
	puts("   \\__ \\ (_) | | | |_\\__ \\ | | |  __/ | |");
	puts("   |___/\\___/|_|  \\__|___/_| |_|\\___|_|_|");
	puts("\n");
	puts("     The c shell that can't do anything!");
	puts("          (Please don't try to)\n");
}

void menu(){
	puts("\n1) Add command");
	puts("2) View command");
	puts("3) Edit tag");
	puts("4) Run command");
	puts("5) Remove argument");
}

command * add_cmd(command * head){
	char in[250];

	command * node = (command*) malloc(sizeof(command));
	head->next = node;
	node->next = NULL;
	node->index = currIndex++;
	node->argslen = 1;

	printf("\nCommand to add >> ");
	fgets(in,sizeof(in),stdin);
	in[strlen(in)-1] = '\0';
	node->cmd = malloc(strlen(in)+1);
	strcpy(node->cmd, in);

	int i = 0;
	while(in[i] != '\0'){
		if(in[i] == ' ')
			node->argslen++;
		i++;
	}

	i = 0;
	char * ptr;
	ptr = strtok(in," ");
	node->args = malloc(sizeof(char*));
	while(ptr != NULL){
		node->args = realloc(node->args,(i+1)*sizeof(char*));
		node->args[i] = malloc((strlen(ptr) + 1));
		strcpy(node->args[i],ptr);
		i++;
		ptr = strtok(NULL, " ");
	}
	printf("Command added at index %d",node->index);
	printf("\nTag for command >> ");
	memset(in,0,sizeof(in));
	fgets(in,sizeof(in),stdin);
	in[strlen(in)-1] = '\0';
	node->tag = malloc(strlen(in)+1);
	strcpy(node->tag, in);
	return node;
}

void view_cmd(int index, command * dummy){
	int * i = &currIndex;
	command * node = dummy->next;
	if(index > *i-1){
		printf("\nInvalid index!\n");
		return;
	}
	while(node != NULL){
		if(index == node->index){
			printf("\nCmd %d || Tag: %s\n",node->index,node->tag);
			char buff[10];
			int option;
			printf("Index of argument >> ");
			fgets(buff,sizeof(buff),stdin);
			option = atoi(buff);
			if(option > node->argslen-1){
				printf("\nInvalid index!\n");
				return;
			}
			if(strlen(node->args[option]) > 5){
				printf("\nArgument is too large!\n");
				return;
			}
			printf(node->args[option]);
			break;
		}
		node = node->next;
	}
}

void edit_tag(int index, command * dummy){
	if(index > currIndex-1){
		printf("\nInvalid index!\n");
		return;
	}
	command * node = dummy->next;
	char in[250];
	while(node != NULL){
		if(index == node->index)
			break;
		node = node->next;
	}
	printf("\nEdit tag >> ");
	fgets(in,strlen(node->tag),stdin);
	in[strlen(in)-1] = '\0';
	strcpy(node->tag,in);
}

void run_cmd(int index, command * dummy){
	if(index > currIndex-1){
		printf("\nInvalid index!\n");
		return;
	}
	command * node = dummy->next;
	while(node != NULL){
		if(index == node->index)
			break;
		node = node->next;
	}
	if(strcmp(node->cmd,allowed) == 0){
		int pid = fork();
		if(pid == 0){
			execvp(node->args[0],node->args);
			perror("execvp");
		}else if(pid == -1)
			return;
		else
			waitpid(pid,NULL,0);
	}else{
		printf("\nCommand not allowed!\nLeave feedback? (y/n) >> ");
		char option = getchar();
		if(!(option == 'Y' || option == 'y')){
			if(option == '\n')
				return;
			getchar();
			return;
		}
		getchar();
		printf("Feedback >> ");
		char * feedback = malloc(40);
		fgets(feedback,40,stdin);
		FILE *fptr = fopen("/dev/null","a");
		fprintf(fptr,"%s",feedback);
		fclose(fptr);
	}
}

void del_arg(int index, command * head){
	command * node = head->next;
	if(index > currIndex){
		printf("\nInvalid index!\n");
		return;
	}
	while(node != NULL){
		if(node->index == index)
			break;
		node = node->next;
	}
	free(node->args[node->argslen-1]);
	node->argslen--;
}

int main(){
	banner();
	char buff[8];
	int choice;

	command * head = (command*) malloc(sizeof(command));
	head->next = NULL;
	command * dummy = head;

	while(1){
		memset(buff,0,sizeof(buff));
		menu();
		printf("Choose an option >> ");
		fgets(buff, sizeof(buff), stdin);
		choice = atoi(buff);
		switch(choice){
			case 1:
				head = add_cmd(head);
				break;
			case 2:
				memset(buff,0,sizeof(buff));
				printf("\nIndex of command to view >> ");
				fgets(buff,sizeof(buff),stdin);
				view_cmd(atoi(buff),dummy);
				break;
			case 3:
				memset(buff,0,sizeof(buff));
				printf("\nIndex of command to edit >> ");
				fgets(buff,sizeof(buff),stdin);
				edit_tag(atoi(buff),dummy);
				break;
			case 4:
				memset(buff,0,sizeof(buff));
				printf("\nIndex of command to run >> ");
				fgets(buff,sizeof(buff),stdin);
				run_cmd(atoi(buff),dummy);
				break;
			case 5:
				memset(buff,0,sizeof(buff));
				printf("\nIndex of command to remove arg >> ");
				fgets(buff,sizeof(buff),stdin);
				del_arg(atoi(buff),dummy);
				break;
			default:
				printf("\nInvalid option!\n");
		}
	}
}
