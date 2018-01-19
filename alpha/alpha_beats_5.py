from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBeats_5(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        indicator = np.zeros(len(self.context.ii_list))
        indicator.flat = np.nan
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = util.mabsdv(self.vol[di-self.delay-np.arange(5), ii])
                if self.vol[di-self.delay][ii] > 1e-5:
                    indicator[ii] = temp/self.vol[di-self.delay][ii]
        util.rank(indicator)
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.nanmean(self.cps[di-self.delay-np.arange(5), ii])
                if abs(temp1) > 1e-5:
                    self.alpha[ii] = (self.cps[di-self.delay][ii] - temp1) / temp1 * (indicator[ii] - 0.5)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('volume')