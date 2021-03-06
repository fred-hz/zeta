from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaRumba_4(AlphaBase):
    def initialize(self):
        self.cps = self.context.fetch_data('adj_close')
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

                if count >= 5 and count1 >= 5:
                    self.alpha[ii] = -util.corr(Vl[count - 1 - np.arange(5)], RSI[count1 - 2 - np.arange(5)])

    def dependencies(self):
        self.register_dependency('adj_close')