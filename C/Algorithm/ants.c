#include <stdio.h>
#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b

long len, n;

void input()
{
	long Max = -1, Min = -1;
	long i, q, p = 0;

	scanf("%ld%ld",&len,&n);
	for(i = 0; i < n; i++)
	{
		scanf("%ld",&p);
		q = p;
		p = min(p,len-p);
		if(p>Max)
			Max = p;
		q = max(q,len-q);
		if(q>Min)
			Min = q;
	}
	printf("%ld %ld\n",Max,Min);
}

int main()
{
	int t;

	scanf("%d",&t);
	while(t--)
		input();
	return 1;
}
