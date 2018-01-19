from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaBarra(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.BETA = self.context.fetch_data('BETA')
        self.BTOP = self.context.fetch_data('BTOP')
        self.DIVYILD = self.context.fetch_data('DIVYILD')
        self.EARNYILD = self.context.fetch_data('EARNYILD')
        self.GROWTH = self.context.fetch_data('GROWTH')
        self.LEVERAGE = self.context.fetch_data('LEVERAGE')
        self.LIQUIDTY = self.context.fetch_data('LIQUIDTY')
        self.MOMENTUM = self.context.fetch_data('MOMENTUM')
        self.RESVOL = self.context.fetch_data('RESVOL')
        self.SIZE = self.context.fetch_data('SIZE')
        self.SIZENL = self.context.fetch_data('SIZENL')
        self.alpha = self.context.alpha

    def compute_day(self, di):
        if di == 354:
            self.alpha.flat = 0.
        else:
            for ii in range(len(self.context.ii_list)):
                if self.is_valid[di][ii]:
                    self.alpha[ii] = -self.SIZENL[di][ii]

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('BETA')
        self.register_dependency('BTOP')
        self.register_dependency('DIVYILD')
        self.register_dependency('EARNYILD')
        self.register_dependency('GROWTH')
        self.register_dependency('LEVERAGE')
        self.register_dependency('LIQUIDTY')
        self.register_dependency('MOMENTUM')
        self.register_dependency('RESVOL')
        self.register_dependency('SIZE')
        self.register_dependency('SIZENL')
