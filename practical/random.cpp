#include <iostream>
#include <random>
#include<time.h>
using namespace std;

int main()
{
    static mt19937 gen(time(nullptr));
    static uniform_int_distribution<int> distr(20, 100);

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            /* code */
            cout << distr(gen) << " ";
        }
        cout << endl;
    }

    return 0;
}