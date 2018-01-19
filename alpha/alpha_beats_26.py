from alpha.alpha_base import AlphaBase
import numpy as np
import math


class AlphaBeats_26(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cap = self.context.fetch_data('cap')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(5)
                for i in range(5):
                    tmp = np.nanstd(self.vol[di-self.delay-i-np.arange(20), ii])
                    if tmp > 1e-5:
                        temp[i] = math.log(self.cap[di-self.delay-i][ii])/tmp*1000
                temp_ = np.nanmean(temp)
                if abs(temp_) > 1e-5:
                    self.alpha[ii] = (temp[0] - temp_)/temp_

    def dependencies(self):
        self.register_dependency('cap')
        self.register_dependency('volume')