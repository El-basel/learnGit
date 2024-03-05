//
// Created by pc on 1/5/2024.
//


#include "iostream"

void solve()
{
    std::string name{};
    std::cin >> name;
    int characters{0};
    bool distinct{true};
    for (int i = 0; i < name.length(); ++i)
    {
        for (int j = i+1; j < name.length(); ++j)
        {
            if(name[i] == name[j])
            {
                distinct = false;
            }

        }
        if(distinct)
        {
            ++characters;
        }
        distinct = true;
    }
    if(characters % 2 == 0)
    {
        std::cout << "CHAT WITH HER!\n";
    }
    else
    {
        std::cout << "IGNORE HIM!\n";
    }
}

int main() {
    int t{1};
//    std::cin >> t;
    while (t--) {
        solve();
    }

}