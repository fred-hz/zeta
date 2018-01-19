from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaMarauder_16(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                value1 = np.zeros(50)
                for i in range(49, -1, -1):
                    if i == 49:
                        value1[i] = util.EffiRatio(self.cps[di - self.delay - i - np.arange(5), ii]) * self.cps[di - self.delay - i][ii]
                    else:
                        tmp = util.EffiRatio(self.cps[di - self.delay - i - np.arange(5), ii]) * 0.5
                        value1[i] = tmp * self.cps[di-self.delay-i][ii] + (1-tmp) * value1[i+1]
                self.alpha[ii] = util.corr(value1[np.arange(20)], self.vol[di-self.delay-np.arange(20), ii] - self.vol[di-self.delay-np.arange(20)-1, ii]) - util.corr(value1[np.arange(5)], self.vol[di-self.delay-np.arange(5), ii] - self.vol[di-self.delay-np.arange(5)-1, ii])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('volume')
