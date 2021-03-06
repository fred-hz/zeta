from alpha.alpha_base import AlphaBase
import numpy as np
import util, scipy.stats


class AlphaFoxtrot_30(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.high = self.context.fetch_data('adj_high')
        self.cps = self.context.fetch_data('adj_close')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                value1 = np.zeros(10)
                value2 = np.zeros(10)
                for i in range(10):
                    value1[i] = scipy.stats.skew(self.cps[di-self.delay-i-np.arange(20), ii], nan_policy='omit')
                    value2[i] = np.nanmax(self.high[di-self.delay-i-np.arange(5), ii])
                self.alpha[ii] = -util.corr(value1, value2)

    def dependencies(self):
        self.register_dependency('adj_high')
        self.register_dependency('adj_close')