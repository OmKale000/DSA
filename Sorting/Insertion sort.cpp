#include<iostream>
using namespace std;
int main()
{
    int arr[] = {7, 2, 8, 3, 9};

    for(int i=0;i<5;i++)
    {
        int key = arr[i];
        int j = i-1;
        while(j>=0 && arr[j] > key)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
        
    }

    cout << "Sorted Array is : ";
    for(int i=0;i<5;i++)
    {
        cout << arr[i] << " ";
    }
}