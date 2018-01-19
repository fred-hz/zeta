from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaLuckydog_2(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.open = self.context.fetch_data('adj_open')
        self.ret = self.context.fetch_data('return')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(20)
                for i in range(20):
                    if not np.sum(-np.isnan(self.ret[di-self.delay-i-np.arange(5), ii])) == 0:
                        temp1[i] = np.nanargmax(self.ret[di-self.delay-i-np.arange(5), ii])
                self.alpha[ii] = util.corr(temp1, self.open[di-self.delay-np.arange(20), ii])

    def dependencies(self):
        self.register_dependency('adj_open')
        self.register_dependency('return')
