from alpha.alpha_base import AlphaBase
import numpy as np
from sklearn import linear_model


class AlphaTango_12(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.ret = self.context.fetch_data('return')

    def compute_day(self, di):
        M = 20
        N = 10
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                y = np.zeros(M)
                x = np.ones((M, N+1))
                for i in range(M):
                    if not np.isnan(self.ret[di-self.delay-i][ii]):
                        y[i] = self.ret[di-self.delay-i][ii]
                    for j in range(1, N+1):
                        if not np.isnan(self.cps[di-self.delay-i-j][ii]):
                            x[i][j] = self.cps[di-self.delay-i-j][ii]
                        else:
                            x[i][j] = 10.
                reg = linear_model.LinearRegression()
                reg.fit(x, y)
                mark = np.array([False] * N, dtype=bool)
                cnt = 0
                for i in range(1, len(reg.coef_)):
                    if reg.coef_[i] > 1e-3:
                        cnt += 1
                        mark[i-1] = True
                if cnt < 1:
                    continue
                y1 = np.zeros(M)
                x1 = np.ones((M, cnt+1))
                for i in range(M):
                    if not np.isnan(self.ret[di-self.delay-i][ii]):
                        y1[i] = self.ret[di-self.delay-i][ii]
                    k = 1
                    for j in range(1, N+1):
                        if mark[j-1]:
                            if not np.isnan(self.cps[di-self.delay-i-j][ii]):
                                x1[i][k] = self.cps[di-self.delay-i-j][ii]
                            else:
                                x1[i][k] = 10.
                            k += 1
                reg = linear_model.LinearRegression()
                reg.fit(x1, y1)
                temp = reg.coef_[0]
                for i in range(cnt):
                    temp += self.ret[di-self.delay-i][ii] * reg.coef_[i+1]
                self.alpha[ii] = temp

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('return')
