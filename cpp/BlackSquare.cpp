//
// Created by pc on 1/6/2024.
//


#include "iostream"

void solve()
{
    int calories[4];
    for (int i = 0; i < 4; ++i)
    {
        std::cin >> calories[i];
    }
    std::string s{};
    int total{0};
    std::cin >> s;
    for (int i = 0; i < s.length(); ++i)
    {
        total += calories[(s[i] - '0') - 1];
    }
    std::cout << total << '\n';
}

int main() {
    int t{1};
//    std::cin >> t;
    while (t--) {
        solve();
    }

}