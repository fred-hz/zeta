from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_6(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                Vg = np.zeros(10)
                for i in range(10):
                    if self.cps[di-self.delay-i][ii] > self.cps[di-self.delay-i-1][ii]:
                        Vg[i] = self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-1][ii]

                n = 50
                ATR = np.zeros(n)
                NDM = np.zeros(n)
                NDI = np.zeros(n)
                for i in range(n-1, -1, -1):
                    if i == n-1:
                        ATR[i] = self.high[di-self.delay-i][ii] - self.low[di-self.delay-i][ii]
                        if self.low[di-self.delay-i-1][ii] - self.low[di-self.delay-i][ii] > self.high[di-self.delay-i][ii] - self.high[di-self.delay-i-1][ii] and self.low[di-self.delay-i-1][ii] > self.low[di-self.delay-i][ii]:
                            NDM[i] = self.low[di-self.delay-i-1][ii] - self.low[di-self.delay-i][ii]
                        if abs(ATR[i]) > 1e-5:
                            NDI[i] = NDM[i]/ATR[i] * 1000
                    else:
                        ATR[i] = (self.high[di - self.delay - i][ii] - self.low[di - self.delay - i][ii]) * 0.1 + ATR[i+1] * 0.9
                        if self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii] > \
                                        self.high[di - self.delay - i][ii] - self.high[di - self.delay - i - 1][ii] and \
                                        self.low[di - self.delay - i - 1][ii] > self.low[di - self.delay - i][ii]:
                            NDM[i] = self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii]
                        if abs(ATR[i]) > 1e-5:
                            NDI[i] = NDM[i] / ATR[i] * 100 + NDI[i+1] * 0.9 # 100 = 0.1 * 1000
                self.alpha[ii] = util.corr(NDI[np.arange(10)], Vg)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')