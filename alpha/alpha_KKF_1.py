from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaKKF_1(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.ret = self.context.fetch_data('return')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(5)
                temp2 = np.zeros(22)
                for i in range(5):
                    if not np.sum(-np.isnan(self.ret[di-self.delay-i-np.arange(5), ii])) == 0:
                        temp1[i] = np.nanargmin(self.ret[di-self.delay-i-np.arange(5), ii])
                for i in range(22):
                    if not np.sum(-np.isnan(self.ret[di-self.delay-i-np.arange(5), ii])) == 0:
                        temp2[i] = np.nanargmin(self.ret[di-self.delay-i-np.arange(5), ii])
                self.alpha[ii] = np.nanargmin(temp1) - np.nanargmin(temp2)

    def dependencies(self):
        self.register_dependency('return')
