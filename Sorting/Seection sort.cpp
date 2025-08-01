#include<iostream>
using namespace std;
int main()
{

    int arr[] = {7,8,54,4,9,2,1};
    for(int i =0 ;i < 7; i++)
    {
        int min=i;
        for(int j =i ; j<7 ;j++)
        {
            if(arr[j] < arr[min])
            {
                min = j;
            }
        }
        swap(arr[i], arr[min]);
    }
    cout << "Sorted Array is : ";
    for(int i=0;i<7;i++)
    {
        cout << arr[i] << " ";
    }
}