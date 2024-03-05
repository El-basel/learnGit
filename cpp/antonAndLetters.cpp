//
// Created by pc on 2/5/2024.
//


#include "iostream"
#include "set"
void solve()
{
    std::set<char> s{};
    char tmp{};
    std::cin >> tmp;
    while (tmp != '}')
    {
        std::cin >> tmp;
        if(tmp == ' ' or tmp == ',' or tmp == '}')
        {
            continue;
        }
        s.insert(tmp);
    }
    std::cout << s.size();
}

int main() {
    int t{1};

    while (t--) {
        solve();
    }

}