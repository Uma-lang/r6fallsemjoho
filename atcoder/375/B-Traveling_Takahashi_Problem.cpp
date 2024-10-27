#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

double cost(double a, double b, double c, double d);

int main()
{
    int n;
    cin >> n;

    // double x[n], y[n];
    vector<double> x(n + 1), y(n + 1);
    x[0] = 0.0;
    y[0] = 0.0;
    for (int i = 1; i <= n; i++)
    {
        cin >> x[i] >> y[i];
    }

    double sum = 0.0;
    for (int i = 0; i < n; i++)
    {
        sum += cost(x[i], y[i], x[i + 1], y[i + 1]);
        // cout << x[i] << y[i] << x[i+1] << y[i+1] << sum << '\n';
    }
    // sum += cost();
    sum += cost(x[n], y[n], 0, 0);
    // cout << x[n] << y[n] << x[0] << y[0] << sum << '\n';
    cout << fixed << setprecision(8) << sum;

    return 0;
}

double cost(double a, double b, double c, double d)
{
    return sqrt((a - c) * (a - c) + (b - d) * (b - d));
}