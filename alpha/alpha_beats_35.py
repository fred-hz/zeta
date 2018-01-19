from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBeats_35(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp = np.zeros(5)
                for i in range(5):
                    temp[i] = util.EffiRatio(self.cps[di-self.delay-i-np.arange(5), ii])
                tmp = np.nanmean(temp)
                if abs(tmp) > 1e-5:
                    self.alpha[ii] = (temp[0] - tmp) / tmp

    def dependencies(self):
        self.register_dependency('adj_close')