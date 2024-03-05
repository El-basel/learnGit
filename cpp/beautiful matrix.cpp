//
// Created by pc on 1/3/2024.
//


#include "iostream"

void solve() {

    int arr[5][5];
    int x,y;
    int steps{};
    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            std::cin >> arr[i][j];
            if(arr[i][j])
            {
                x = i;
                y = j;
            }
        }
    }
    while(x > 2)
    {
        --x;
        ++steps;
    }
    while(x < 2)
    {
        ++x;
        ++steps;
    }
    while(y > 2)
    {
        --y;
        ++steps;
    }
    while(y < 2)
    {
        ++y;
        ++steps;
    }
    std::cout << steps;
}

int main() {
//    int t{};
//    std::cin >> t;
//    while (t--) {
        solve();
//    }

}