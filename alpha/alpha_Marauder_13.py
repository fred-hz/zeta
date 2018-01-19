from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaMarauder_13(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.low = self.context.fetch_data('adj_low')
        self.ret = self.context.fetch_data('return')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(20)
                for i in range(20):
                    if not np.sum(-np.isnan(self.low[di-self.delay-i-np.arange(22), ii])) == 0:
                        temp[i] = np.nanargmax(self.low[di-self.delay-i-np.arange(22), ii])
                self.alpha[ii] = util.corr(temp, self.ret[di-self.delay-np.arange(20), ii]) - util.corr(temp[np.arange(5)], self.ret[di-self.delay-np.arange(5), ii])

    def dependencies(self):
        self.register_dependency('adj_low')
        self.register_dependency('return')
