from alpha.alpha_base import AlphaBase
import numpy as np
import util, scipy.stats


class AlphaLuckydog_1(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.high = self.context.fetch_data('adj_high')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(20)
                for i in range(20):
                    temp1[i] = scipy.stats.kurtosis(self.high[di-self.delay-i-np.arange(22), ii], nan_policy='omit')
                self.alpha[ii] = -util.corr(temp1, self.high[di-self.delay-np.arange(20), ii])

    def dependencies(self):
        self.register_dependency('adj_high')