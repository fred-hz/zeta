from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBeats_24(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        indicator = np.zeros(len(self.context.ii_list))
        indicator.flat = np.nan
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                n = 100
                ATR = np.zeros(n)
                PDM = np.zeros(n)
                NDM = np.zeros(n)
                PDI = np.zeros(n)
                NDI = np.zeros(n)
                DX = np.zeros(n)
                ADI = np.zeros(n)
                count = 0
                for i in range(n - 1, -1, -1):
                    if np.isnan(self.high[di - self.delay - i][ii]) or np.isnan(
                            self.high[di - self.delay - i - 1][ii]) or np.isnan(
                            self.low[di - self.delay - i][ii]) or np.isnan(self.low[di - self.delay - i][ii]):
                        continue
                    if count == 0:
                        ATR[count] = self.high[di - self.delay - i][ii] - self.low[di - self.delay - i][ii]
                        if self.high[di - self.delay - i][ii] - self.high[di - self.delay - i - 1][ii] > \
                                        self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii] and \
                                        self.high[di - self.delay - i][ii] > self.high[di - self.delay - i - 1][ii]:
                            PDM[count] = self.high[di - self.delay - i][ii] - self.high[di - self.delay - i - 1][ii]
                        if self.high[di - self.delay - i][ii] - self.high[di - self.delay - i - 1][ii] < \
                                        self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii] and \
                                        self.low[di - self.delay - i - 1][ii] > self.low[di - self.delay - i][ii]:
                            NDM[count] = self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii]
                        if abs(ATR[count]) > 1e-5:
                            PDI[count] = PDM[count] / ATR[count]
                            NDI[count] = NDM[count] / ATR[count]
                    else:
                        ATR[count] = (self.high[di - self.delay - i][ii] - self.low[di - self.delay - i][ii]) * 0.1 + \
                                     ATR[count - 1] * 0.9
                        if self.high[di - self.delay - i][ii] - self.high[di - self.delay - i - 1][ii] > \
                                        self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii] and \
                                        self.high[di - self.delay - i][ii] > self.high[di - self.delay - i - 1][ii]:
                            PDM[count] = self.high[di - self.delay - i][ii] - self.high[di - self.delay - i - 1][ii]
                        if self.high[di - self.delay - i][ii] - self.high[di - self.delay - i - 1][ii] < \
                                        self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii] and \
                                        self.low[di - self.delay - i - 1][ii] > self.low[di - self.delay - i][ii]:
                            NDM[count] = self.low[di - self.delay - i - 1][ii] - self.low[di - self.delay - i][ii]
                        if abs(ATR[count]) > 1e-5:
                            PDI[count] = PDM[count] / ATR[count] * 0.1 + PDI[count - 1] * 0.9
                            NDI[count] = NDM[count] / ATR[count] * 0.1 + NDI[count - 1] * 0.9

                    if abs(PDI[count] + NDI[count]) > 1e-5:
                        DX[count] = abs(PDI[count] - NDI[count]) / (PDI[count] + NDI[count]) * 100
                    if count == 0:
                        ADI[count] = DX[count]
                    else:
                        ADI[count] = ADI[count-1] * 0.9 + DX[count] * 0.1
                    count += 1
                indicator[ii] = ADI[count-1]
        util.rank(indicator)
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.nanmean(self.cps[di-self.delay-np.arange(5), ii])
                if abs(temp1) > 1e-5:
                    self.alpha[ii] = (temp1 - self.cps[di-self.delay][ii]) / temp1 * (indicator[ii] - 0.5)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('volume')