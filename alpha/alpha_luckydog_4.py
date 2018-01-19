from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaLuckydog_4(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.ret = self.context.fetch_data('return')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(20)
                temp2 = np.zeros(20)
                for i in range(20):
                    temp = 0
                    for j in range(3):
                        if not np.isnan(self.ret[di-self.delay-i-j][ii]):
                            temp += 1000 * self.ret[di-self.delay-i-j][ii] * pow(0.5, j+1)
                    temp1[i] = temp
                    if not np.sum(-np.isnan(self.ret[di-self.delay-i-np.arange(5), ii])) == 0:
                        temp2[i] = np.nanargmin(self.ret[di-self.delay-i-np.arange(5), ii])
                self.alpha[ii] = util.corr(temp1, temp2)

    def dependencies(self):
        self.register_dependency('return')
