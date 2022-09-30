#include<stdio.h>
void main()
{
	char a[10];
	int i=0,count;
	printf("enter a string\n");
	scanf("%s",a);
	while(a[i]!='\0')
	{
		count++;
		i++;
	}
	printf("the length is%d",count);
}
