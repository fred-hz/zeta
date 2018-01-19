from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaChacha_9(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.high = self.context.fetch_data('adj_high')
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.zeros(10)
                temp2 = np.zeros(10)
                for i in range(10):
                    temp1[i] = np.nanmax(self.high[di-self.delay-i-np.arange(20), ii])
                    temp2[i] = util.EffiRatio(self.vol[di - self.delay - i - np.arange(20), ii])
                temp = np.nanstd(temp1)
                if temp > 1e-5:
                    self.alpha[ii] = np.nanstd(temp2) / temp

    def dependencies(self):
        self.register_dependency('adj_high')
        self.register_dependency('volume')