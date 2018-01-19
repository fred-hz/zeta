from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaBeats_22(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(5)
                for i in range(5):
                    tmp = np.nanstd(self.vol[di-self.delay-i-np.arange(20), ii])
                    if tmp > 1e-5:
                        temp[i] = np.nanmean(self.vol[di-self.delay-i-np.arange(20), ii]) / tmp
                temp1 = np.nanmean(temp)
                if abs(temp1) > 1e-3:
                    self.alpha[ii] = (temp[0] - temp1)/temp1

    def dependencies(self):
        self.register_dependency('volume')