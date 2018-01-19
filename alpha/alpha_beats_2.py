from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBeats_2(AlphaBase):
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
                stdcc = np.nanstd(self.cps[di-self.delay-np.arange(20), ii])
                if stdcc > 1e-5:
                    PercB = (self.cps[di-self.delay][ii] - np.nanmean(self.cps[di-self.delay-np.arange(20), ii]))/4.0/stdcc + 0.5
                else:
                    PercB = 0
                indicator[ii] = PercB * self.cps[di-self.delay][ii] * self.vol[di-self.delay][ii]
        util.rank(indicator)
        tmp = np.where((self.is_valid[di] > 0.5) & (self.cps[di-self.delay-4] > 1e-5))[0]
        self.alpha[tmp] = (self.cps[di-self.delay-4][tmp]-self.cps[di-self.delay][tmp])/self.cps[di-self.delay-4][tmp] * (indicator[tmp] - 0.5)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('volume')