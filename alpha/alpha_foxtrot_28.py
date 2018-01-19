from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_28(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                Tao = np.zeros(100)
                for i in range(99, -1, -1):
                    if i == 99:
                        temp = 0.
                        cnt = 0.
                        for j in range(9):
                            for k in range(j+1, 10):
                                if np.isnan(self.cps[di-self.delay-i-j][ii]) or np.isnan(self.cps[di-self.delay-i-k][ii]):
                                    continue
                                temp += np.sign(self.cps[di-self.delay-i-j][ii] - self.cps[di-self.delay-i-k][ii])
                                cnt += 1.
                        if cnt > 1e-5:
                            Tao[i] = temp / cnt
                    else:
                        tmp1 = np.nansum(np.sign(self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-np.arange(1, 10), ii]))
                        tmp2 = np.nansum(np.sign(self.cps[di - self.delay - i - np.arange(1, 10), ii] - self.cps[di - self.delay - i - 10][ii]))
                        Tao[i] = Tao[i+1] + (tmp1 - tmp2) / 45.

                Vg = np.zeros(10)
                for i in range(10):
                    if self.cps[di-self.delay-i][ii] > self.cps[di-self.delay-i-1][ii]:
                        Vg[i] = self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-1][ii]
                self.alpha[ii] = -util.corr(Vg, Tao[np.arange(10)])

    def dependencies(self):
        self.register_dependency('adj_close')
