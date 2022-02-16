#include<iostream>
using namespace std;

int arr[11];
int N, T;
int main(void){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;
    cin >> T;
    for (int k = 0; k < T; k++){
        cin >> N;
        if (N < 4){
            cout << arr[N] << "\n";
            continue;
        }
        for (int i = 4; i <= N; i++){
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3];
        }
        cout << arr[N] << "\n";
    }
}
