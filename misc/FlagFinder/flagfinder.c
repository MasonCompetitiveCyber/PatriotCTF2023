#include <stdio.h>
#include <unistd.h>
#include <string.h>

__attribute__((constructor)) void ignore_me(){
        setbuf(stdin, NULL);
        setbuf(stdout, NULL);
        setbuf(stderr, NULL);
}

int main()
{   
    char user[101];
    printf("What is the password: ");
    scanf("%s", user);
    
    
    //Flag
    //pctf{Tim3ingI8N3at}
    //length: 13
    char flag[] = "pctf{Tim3ingI8N3at}";
    
    if(strlen(user) < strlen(flag)){
        printf("%s is not long enough", user);
    
    }else if(strlen(user) > strlen(flag)){
        printf("%s is too long", user);
        
    }else{
        for(int i = 0; i < strlen(flag); i++){
            
            if(user[i] == flag[i]){
                //testing
                printf("User input: %d\nFlag input: %d\n", user[i], flag[i]);
                sleep(0.5);
            }else{
                printf("There's been an error");
                break;
            }
            
        }
    }
    
    //printf("%s", flag);
    printf("\n%s", user);
    
    return 0;
}
