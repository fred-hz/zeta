from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaBlackrock_5(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.high = self.context.fetch_data('adj_high')
        self.low = self.context.fetch_data('adj_low')
        self.open = self.context.fetch_data('adj_open')
        self.vol = self.context.fetch_data('volume')
        self.alpha = self.context.alpha

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                self.alpha[ii] = -self.vol[di-self.delay][ii]*(self.cps[di-self.delay][ii] - (self.high[di-self.delay][ii]+self.low[di-self.delay][ii])/2.)/(self.high[di-self.delay][ii]-self.low[di-self.delay][ii])

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_high')
        self.register_dependency('adj_low')
        self.register_dependency('adj_open')
        self.register_dependency('volume')
