from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaMarauder_11(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.open = self.context.fetch_data('adj_open')
        self.ret = self.context.fetch_data('return')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                value1 = np.zeros(20)
                value2 = np.zeros(20)
                for i in range(19, -1, -1):
                    if i == 19:
                        value1[i] = self.open[di-self.delay-i][ii]
                    else:
                        value1[i] = (self.open[di - self.delay - i][ii] + value1[i+1]) * 0.5
                for i in range(20):
                    value2[i] = util.EffiRatio(self.ret[di-self.delay-i-np.arange(5), ii])
                self.alpha[ii] = util.corr(value1, value2) - util.corr(value1[np.arange(5)], value2[np.arange(5)])

    def dependencies(self):
        self.register_dependency('adj_open')
        self.register_dependency('return')