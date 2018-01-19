from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_47(AlphaBase):
    def initialize(self):
        self.cps = self.context.fetch_data('adj_close')
        self.low = self.context.fetch_data('adj_low')
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.delay = int(self.params['delay'])

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                n = 100
                Vg = np.zeros(n)
                Vl = np.zeros(n)
                mg = np.zeros(n)
                ml = np.zeros(n)
                RSI = np.zeros(n)
                count = 0
                count1 = 0
                for i in range(n-1, -1, -1):
                    if np.isnan(self.cps[di-self.delay-i][ii]) or np.isnan(self.cps[di-self.delay-i-1][ii]):
                        continue
                    if self.cps[di-self.delay-i][ii] > self.cps[di-self.delay-i-1][ii]:
                        Vg[count] = self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-1][ii]
                    else:
                        Vl[count] = self.cps[di - self.delay - i-1][ii] - self.cps[di - self.delay - i][ii]
                    if count == 10:
                        mg[count1] = np.nanmean(Vg[np.arange(10)])
                        ml[count1] = np.nanmean(Vl[np.arange(10)])
                        if mg[count1] + ml[count1] > 1e-5:
                            RSI[count1] = 100 * mg[count1]/(mg[count1] + ml[count1])
                        else:
                            RSI[count1] = np.nan
                        count1 += 1
                    elif count > 10:
                        mg[count1] = Vg[count] * 0.1 + mg[count1-1] * 0.9
                        ml[count1] = Vl[count] * 0.1 + ml[count1 - 1] * 0.9
                        if mg[count1] + ml[count1] > 1e-5:
                            RSI[count1] = 100 * mg[count1]/(mg[count1] + ml[count1])
                        else:
                            RSI[count1] = np.nan
                        count1 += 1
                    count += 1

                if count1 >= 20:
                    temp = np.zeros(20)
                    for i in range(20):
                        if not np.sum(-np.isnan(self.low[di-self.delay-i-np.arange(20), ii])) == 0:
                            temp[i] = np.nanargmin(self.low[di-self.delay-i-np.arange(20), ii])
                    self.alpha[ii] = util.corr(temp, RSI[count1-1-np.arange(20)]) - util.corr(temp[np.arange(5)], RSI[count1-1-np.arange(5)])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_low')
