#include "neut.h"
#include <map>
#include <iostream.h>
#include <cmath>
#include <limits>

using namespace std;
void neut(double* alpha, double* group, int size)
{
        map<double, double> mean;
        map<double, int> meannum;
        for (int i=0; i<size; ++i)
        {
                if (!isnan(alpha[i]) && group[i] > -0.5 && !isnan(group[i])) {
                    mean[group[i]] += alpha[i];
                    ++ meannum[group[i]];
                } else if (group[i] > -0.5 || !isnan(group[i])) { 
                    alpha[i] = numeric_limits<double>::quiet_NaN();
                }
        }
        for (map<double, double>::iterator iter=mean.begin(); iter!=mean.end(); ++iter)
        {
                if (meannum[iter->first]) {
                    if (meannum[iter->first] > 1.5)
                        mean[iter->first] /= meannum[iter->first];
                    else
                        mean[iter->first] = numeric_limits<double>::quiet_NaN();
                }
        }
        for (int i=0; i<size; ++i)
        {
                if (!isnan(alpha[i]) && group[i] > -0.5 && !isnan(group[i]))
                        alpha[i] -= mean[group[i]];
        }
}
