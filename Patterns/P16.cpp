#include<iostream>
using namespace std;
int main()
{
    for(int i=0;i<7;i++)
    {
        for(int j=0;j<7-i-1 ; j++)
        {
            cout<<" ";
        }
        char ch ='A';
        int x = (2*i+1)/2;
        for(int j=0; j < 2*i+1 ;j++)
        {
            cout<<ch;
            if(j < x) ch++;
            else ch--;
        }
        cout<<endl;
    }
}