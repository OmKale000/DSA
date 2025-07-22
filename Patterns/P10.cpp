#include<iostream>
using namespace std;
int main()
{
    for(int i=0;i<5;i++)
    {
        int st ;
        if(i%2 == 0)
        {
            st = 0;
        }
        else
        {
            st = 1;
        }
        for(int j =0 ;j<i;j++)
        {
            cout<<st;
            st =1-st;
        }
        cout<<endl;
    }
}