from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaTango_21(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                if not np.isnan(self.cps[di-self.delay][ii]):
                    self.alpha[ii] = 0.5 - self.cps[di-self.delay][ii] + int(self.cps[di-self.delay][ii])

    def dependencies(self):
        self.register_dependency('adj_close')