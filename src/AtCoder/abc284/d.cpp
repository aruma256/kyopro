#include <cmath>
#include <iostream>

using namespace std;
using ll = long long;

int main()
{
    ll T;
    cin >> T;
    for (int t=0; t<T; t++) {
        ll n;
        cin >> n;
        for (ll i=2;;i++) {
            ll p, q;
            if (n%i == 0) {
                if (n%(i*i) == 0) {
                    p = i;
                    q = n/i/i;
                } else {
                    p = (ll)round(sqrt(n/i));
                    q = i;
                }
                cout << p << " " << q << endl;
                break;
            }
        }
    }
    return 0;
}
