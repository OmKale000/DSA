#include<iostream>
using namespace std;
int main()
{
    int n =5;
    for(int i=0;i<2*n-1;i++)
    {
        int st=i;
        if(i>n) 
        {
            st=2*n-i;
        }
        for(int j=1;j<st;j++)
        {
            cout<<"* ";
        }
        cout<<endl;
    
    }
}