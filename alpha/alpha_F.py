from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaF(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')
        self.open = self.context.fetch_data('adj_open')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                co = np.nanstd(self.cps[di-self.delay-np.arange(10), ii] - self.open[di-self.delay-np.arange(10), ii])
                hl = np.nanstd(self.high[di - self.delay - np.arange(10), ii] - self.low[di - self.delay - np.arange(10), ii])
                if hl > 1e-5:
                    self.alpha[ii] = co/hl

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('adj_open')