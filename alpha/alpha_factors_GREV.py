from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaFactors(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.REC = self.context.fetch_data('REC')
        self.DAREC = self.context.fetch_data('DAREC')
        self.GREC = self.context.fetch_data('GREC')
        self.FY12P = self.context.fetch_data('FY12P')
        self.DAREV = self.context.fetch_data('DAREV')
        self.GREV = self.context.fetch_data('GREV')
        self.SFY12P = self.context.fetch_data('SFY12P')
        self.DASREV = self.context.fetch_data('DASREV')
        self.GSREV = self.context.fetch_data('GSREV')
        self.FEARNG = self.context.fetch_data('FEARNG')
        self.FSALESG = self.context.fetch_data('FSALESG')
        self.alpha = self.context.alpha

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                self.alpha[ii] = self.GREV[di-self.delay][ii]

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('REC')
        self.register_dependency('DAREC')
        self.register_dependency('GREC')
        self.register_dependency('FY12P')
        self.register_dependency('DAREV')
        self.register_dependency('GREV')
        self.register_dependency('SFY12P')
        self.register_dependency('DASREV')
        self.register_dependency('GSREV')
        self.register_dependency('FEARNG')
        self.register_dependency('FSALESG')
