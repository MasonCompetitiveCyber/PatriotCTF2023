#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


struct note
{
    unsigned short note_id;
    unsigned short note_length;
    unsigned char note[100];
} __attribute__((packed)) typedef note;

__attribute__((used)) void exit_program()
{
    exit(0);
}

struct f_ptr
{
    typeof(&exit_program) exit_function;
    unsigned int garbage[0x80];
};

struct stupid_struct
{
    struct note global_note;
    struct f_ptr global_exit;
};

// GCC was not being nice and ordering these right
// So we need to manually specify our order in a struct
struct stupid_struct global_obj;
// note* global_note = &global_obj.obj_one;
// struct f_ptr* global_exit = &global_obj.obj_two;

void voice_test()
{
    asm(
"ldr x0, [sp, #0]\n\t"
"ldp x29, x30, [sp], #0\n\t"
"add sp, sp, #0x10"
);
}
void male_voice_test()
{
    asm(
"ldr x1, [sp, #0]\n\t"
"ldp x29, x30, [sp], #0\n\t"
"add sp, sp, #0x10"
);
}
void female_voice_test()
{
    asm(
"ldr x2, [sp, #0]\n\t"
"ldp x29, x30, [sp], #0x0\n\t"
"add sp, sp, #0x10"
);
}
void voice_note()
{
    struct note my_note;
    memcpy(&my_note, &global_obj.global_note, sizeof(struct note));
    printf("Ahhhem. Text to speach is down, so you'll have to manage with a transcript:\n");
    /*
    Another info leak, this time a stack cookie.
    */
    write(1,&my_note.note, global_obj.global_note.note_length);
}
struct dumb
{
    struct note my_note;
    unsigned int note_length;
};
void robot_voice_note()
{

    struct dumb my_stack;
    /*
    Third vulnerability, straight stack overflow
    */
    memcpy(&my_stack.my_note.note, &global_obj.global_note.note, global_obj.global_note.note_length);
    printf("Beep Boop. TeXt T0 $P3ach 1s d0wn, s0 y0u'1l h4v3 t0 m@nage w1th a tr@nscript:\n");
    write(1,&my_stack.my_note.note, global_obj.global_note.note_length);
}

void read_note()
{
    printf("Note:\n");
    if (global_obj.global_note.note_id == 0)
    {
        printf("Note is undefined! Create a note first!\n");
        return;
    }

    write(1, &global_obj.global_note.note, global_obj.global_note.note_length);
}

void create_note()
{
    unsigned short int note_length = 0;
    unsigned short int note_id = global_obj.global_note.note_id;
    printf("Note ID:\n");
    // Here is the vulnerability.
    // Reading 4 bytes into a 2 byte object.
    // Gets around 99 byte max size for length
    scanf("%u", &global_obj.global_note.note_id); 
    if (note_id == global_obj.global_note.note_id)
    {
        printf("Old note ID, using old length\n");
    }
    else
    {
        printf("Note length: [MAX 99 CHARACTERS]\n");
        scanf("%hu", &note_length);
        if (note_length > 99)
        {
            printf("Note length too long try again\n");
            return;
        }
        global_obj.global_note.note_length = note_length;
    }

    
    printf("Message:\n");
    read(0, &global_obj.global_note.note, global_obj.global_note.note_length);
}

void delete_note()
{
    printf("Writing note's contents into garbage\n");
    int fd = -1;
    fd = open("/dev/null", O_RDWR);
    if (fd < 0)
    {
        exit(-1);
    }
    write(fd, &global_obj.global_note.note, global_obj.global_note.note_length);
    // close(fd); // Without the close here we can do a bl into open without it closing us.

    printf("Deleting note\n");
    global_obj.global_note.note_id = 0;
    global_obj.global_note.note_length = 0;
    memset(&global_obj.global_note.note, '\x00', 100);
}


void menu()
{
    char input;
    while (1)
    {
        printf("Note taker menu:\n");
        printf("[1] Create note\n");
        printf("[2] View note\n");
        printf("[3] Delete note\n");
        printf("[4] Quit\n");
        input = getc(stdin);
        switch (input)
        {
            case '1':
                create_note();
                break;
            case '2':
                read_note();
                break;
            case '3':
                delete_note();
                break;
            case '4':
                global_obj.global_exit.exit_function();
                break;
            case '5':
                return;
            default:
                printf("Invalid choice\n");
        }

    }
}

int main(int argc, char ** argv)
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    global_obj.global_exit.exit_function = exit_program;
    menu();
}