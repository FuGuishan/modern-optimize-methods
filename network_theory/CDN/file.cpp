#include "file.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#define MAXLEN 100
int read_file(char **buff,const char * filename){
    FILE *fp=fopen(filename,"r");
    int index=0;
    if(!fp)
    {
        printf("file error!");
        return 0;
    }
    char line[MAXLEN];
    while(!feof(fp))
    {
        if(fgets(line,MAXLEN,fp)==NULL)
            continue;
        buff[index]=(char*)malloc(MAXLEN*sizeof(char));
        strncpy(buff[index],line,MAXLEN-1);
        buff[index++][MAXLEN-1]=0;
    }
    return index;
}
