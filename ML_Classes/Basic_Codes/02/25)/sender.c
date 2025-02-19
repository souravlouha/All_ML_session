#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/msg.h>
#include<errno.h>

#define MAX_TEXT 7

struct message_body {
    long int message_type;
    char text[MAX_TEXT];
};

char *binary(char *arr,int size)
{
  //step-1: create a different character array which will store the binary bit
  char ans[]="0000000";
  //step-2: convert the string to integer
  int sum=0;
  int x=10;
  for(int i=0;i<size;i++)
  {
    int digit=(int)arr[i]-(int)'0';
    sum=sum*x+digit;
  }
  //step-3 convert it into binary
  int n=6;
  printf("The sum is %d\n",sum);
  while(sum>0)
  {
    int digit=(sum%2)+(int)('0');
    ans[n--]=(char)digit;
    sum/=2;
  }
  
  char *ptr=ans;
  return ptr;
}
int main() {
    int msgid = msgget((key_t)1234, 0666 | IPC_CREAT);
    if (msgid == -1) {
        printf("Queue is not created successfully\n");
        exit(1);
    }

    printf("Queue created successfully\n");

    struct message_body message;
    message.message_type = 1;

    while (1) {
        int isMessageReceived = msgrcv(msgid, (void *)&message, MAX_TEXT, 1, 0);
        if (isMessageReceived == -1) {
            printf("Message not received\n");
            exit(1);
        }

        if (strcmp(message.text, "end\n") == 0) {
            printf("Ending the program\n");
            exit(1);
        }
        printf("Received: %s\n", message.text);
    }

    return 0;
}