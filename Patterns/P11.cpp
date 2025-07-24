#include<iostream>
using namespace std;
int main()
{
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<i;j++)
        {
            cout<<j+1;
        }
        int s = 2 * (5 - i);
        for(int j=0; j<s-1 ; j++)
        {
            cout<<" ";
        }  
        for(int j=i;j>=1;j--)
        {
            cout<<j;
        }
        cout<<endl; 

    }
}