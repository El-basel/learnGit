//
// Created by pc on 1/3/2024.
//


#include "iostream"

void solve()
{
    int a, b;
    std::cin >> a >> b;
    int years {};
    while(a <= b)
    {
        a *= 3;
        b *= 2;
        ++years;
    }
    std::cout << years << std::endl;
}

int main() {
//    int t{};
//    std::cin >> t;
//    while (t--) {
        solve();
//    }

}