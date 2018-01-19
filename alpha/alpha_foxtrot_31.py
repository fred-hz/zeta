from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFoxtrot_31(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.low = self.context.fetch_data('adj_low')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(10)
                temp2 = np.zeros(10)
                for i in range(10):
                    if self.cps[di-self.delay-i][ii] > self.cps[di-self.delay-i-1][ii]:
                        temp1[i] = self.cps[di-self.delay-i][ii] - self.cps[di-self.delay-i-1][ii]
                    if not np.sum(-np.isnan(self.low[di-self.delay-i-np.arange(20), ii])) == 0:
                        temp2[i] = np.nanargmin(self.low[di-self.delay-i-np.arange(20), ii])

                self.alpha[ii] = -util.corr(temp1, temp2)

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_low')
