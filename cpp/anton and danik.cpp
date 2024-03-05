//
// Created by pc on 1/3/2024.
//


#include "iostream"

void solve()
{
    int games, anton, danik;
    std::string s{};
    std::cin >> games >> s;
    for (int i = 0; i < games; ++i)
    {
        if(s[i] == 'A')
            ++anton;
        else if (s[i] == 'D')
            ++danik;
    }
    if(anton > danik)
    {
        std::cout << "Anton\n";
    }
    else if(anton < danik)
    {
        std::cout << "Danik\n";
    } else
        std::cout << "Friendship\n";
}

int main() {
    /*int t{};
    std::cin >> t;
    while (t--) {
        solve();
    }*/
    solve();

}