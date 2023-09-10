#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define TAPE_SIZE 0x1000

struct ins
{
    unsigned char op;
    unsigned char dest_reg;
    unsigned char src_reg;
    unsigned char immediate;
} __attribute__((packed)) typedef ins;

struct vm
{
    unsigned int reg1;
    unsigned int reg2;
    unsigned int reg3;
    unsigned int reg4;
    unsigned int cmp;
    unsigned char* tape;
} typedef vm;

int decode_instruction(int fd, ins* curr_ins)
{
    int i=0;
    unsigned char* ins_ptr = (unsigned char *)curr_ins;
    for (int i=0; i < 4; i++)
    {
        read(fd, ins_ptr+i, 1);
    }
    // printf("%lx %lx %lx %lx\n", curr_ins->op, curr_ins->dest_reg, curr_ins->src_reg, curr_ins->immediate);
    return 0;
}

int execute_instruction(int fd, ins* curr_ins,vm* curr_vm)
{
    /*
    Hacky decode, technically an OOB r/w
    */
    unsigned int* dest_reg = (unsigned int*)curr_vm + curr_ins->dest_reg;
    unsigned int* src_reg = (unsigned int*)curr_vm + curr_ins->src_reg;

    // printf("%x %x %x %x\n", curr_ins->op, curr_ins->dest_reg, curr_ins->src_reg, curr_ins->immediate);
    // printf("%x\n", (unsigned char)curr_ins->op);

    switch ((unsigned char)curr_ins->op)
    {
        case 0: // mov
            *dest_reg = *src_reg;
            break;
        case 1: // add
            *dest_reg += *src_reg + curr_ins->immediate;
            break;
        case 2: // sub
            *dest_reg += *src_reg + curr_ins->immediate;
            break;
        case 3: // prnt reg
            printf("%u\n",*dest_reg);
            break;
        case 4: // movi
            *dest_reg = curr_ins->immediate;
            // printf("[movi] %u\n",*dest_reg);
            break;
        case 5: // push
            // curr_vm->tape = (unsigned char *) *src_reg;
            // unsigned int* ptr = (unsigned int *) curr_vm->tape;
            // *ptr = *src_reg;
            curr_vm->tape += 8;
            memcpy(curr_vm->tape, src_reg, 8);
            // printf("[push] %u\n", *src_reg);
            break;
        case 6: // pop
            memcpy(dest_reg, curr_vm->tape, 8);
            // *dest_reg = (unsigned int) curr_vm->tape;
            curr_vm->tape -= 8;
            // printf("[pop] %u\n", *dest_reg);
            break;
        case 7: // cmp
            curr_vm->cmp = *dest_reg - *src_reg;
            break;
        case 8: // jz
            if(curr_vm->cmp == 0)
            {
                short offset = (curr_ins->src_reg << 8) + curr_ins->immediate;
                lseek(fd, offset, SEEK_CUR);
            }
            break;
        case 9: // write
            write(1, curr_vm->tape, curr_ins->immediate);
            break;
        case 0xa: // mul
            // printf("[0] %u %u\n", *dest_reg, *src_reg);
            *dest_reg = *dest_reg * *src_reg;
            *dest_reg += curr_ins->immediate;
            // printf("[1] %u\n", *dest_reg);
            break;
        case 0xb: // addi
            *dest_reg += curr_ins->immediate;
            break;
        case 0xc: // exit
            exit(0);
            break;
        case 0xd: // getnum
            scanf("%u", dest_reg);
            break;
        default:
            // printf("[x] %x %x %x %x\n", curr_ins->op, curr_ins->dest_reg, curr_ins->src_reg, curr_ins->immediate);
            printf("Error executing instruction!\n");
            exit(0);
    }
}

void clear_ins(ins* curr_ins)
{
    curr_ins->op = 0;
    curr_ins->dest_reg = 0;
    curr_ins->src_reg = 0;
    curr_ins->immediate = 0;
}

int main(int argc, char ** argv)
{
    int fd = -1;
    int ret = -1;
    ssize_t count = 0;
    ins* curr_ins = NULL;
    vm* curr_vm = NULL;
    char header[4] = {'\x00'};;
    if (argc < 2)
    {
        printf("Usage %s <program>\n", argv[0]);
        exit(0);
    }

    fd = open(argv[1], O_RDONLY);
    if (fd < 0)
    {
        printf("Could not open %s\n",argv[1]);
        exit(0);
    }

    count = read(fd, &header, 4);
    if (count < 4)
    {
        printf("Failed to read header\n");
        exit(0);
    }

    if (strcmp(header, "SMOL") != 0)
    {
        printf("Not a SMOL program\n");
        exit(0);
    }

    /*
    vm initialization
    */
    curr_ins = malloc(sizeof(ins));
    if (curr_ins == NULL)
    {
        printf("malloc fail\n");
        exit(0);
    }
    curr_vm = malloc(sizeof(vm));
    if (curr_vm == NULL)
    {
        printf("malloc fail\n");
        exit(0);
    }
    curr_vm->tape = malloc(TAPE_SIZE);
    if (curr_vm == NULL)
    {
        printf("malloc fail\n");
        exit(0);
    }

    while (1)
    {
        // Parse in ins struct
        decode_instruction(fd, curr_ins);
        execute_instruction(fd, curr_ins, curr_vm);
        clear_ins(curr_ins);
    }
    free(curr_ins);
}