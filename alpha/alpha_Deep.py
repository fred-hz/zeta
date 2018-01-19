from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaDeep(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.alpha = self.context.alpha

    def compute_day(self, di):
        tmp = np.where(self.is_valid[di])[0]
        self.alpha[tmp] = self.high[di-self.delay][tmp] - self.cps[di - self.delay][tmp]

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
