from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaVega_9(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                temp1 = np.log(self.vol[di-self.delay-np.arange(60), ii])
                wm = util.wmean(temp1)
                if np.isnan(wm):
                    continue
                temp = temp1 - wm
                self.alpha[ii] = np.nansum(temp[temp > 0]) / (-np.nansum(temp[temp < 0]) + 1.)

    def dependencies(self):
        self.register_dependency('volume')
