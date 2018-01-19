#include "rank.h"
#include <vector>
#include <algorithm>
#include <iostream.h>
#include <cmath>
#include <limits>
#include <utility>

using namespace std;
const bool cmp(const pair<int, double> p1, const pair<int, double> p2) {
    if (isnan(p1.second) && isnan(p2.second)) {
        return false;
    }
    else if (isnan(p1.second) && !isnan(p2.second)) {
        return false;
    }
    else if (!isnan(p1.second) && isnan(p2.second)) {
        return true;
    }
    else {
        if (p1.second < p2.second) {
            return true;
        }
        else {
            return false;
        }
    }
}

int rank(double* x, int size)
{
        int i, j, k, n;
        vector<pair<int, double> > xmap;
        for (i = 0; i < size; i++) {
            if (!isnan(x[i])) {
                xmap.push_back(make_pair(i, x[i]));
            }
        }

        n = xmap.size();
        if (n <= 1) {
            if (n == 1) {
                x[xmap[0].first] = 0.5;
            }
            return n;
        }

        sort(xmap.begin(), xmap.end(), cmp);

        double d = n - 1;
        for (i = 0; i < n;) {
            // check for duplicates
            for (j = i + 1; j < n && ((x[xmap[j].first] == x[xmap[i].first]) || (fabs(x[xmap[j].first] - x[xmap[i].first]) <= ((fabs(x[xmap[j].first]) + fabs(x[xmap[i].first])) * 1e-9))); ++j) {
            }
            --j;
            // duplicates should have same rank
            double val = (i+j)/d/2.;
            for (k = i; k <= j; ++k) {
                x[xmap[k].first] = val;
            }
            i = j + 1;
        }
        return n;
}



