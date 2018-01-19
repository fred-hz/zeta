from alpha.alpha_base import AlphaBase
import numpy as np
import scipy.stats


class AlphaFoxtrot_43(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.alpha = self.context.alpha
        self.vol = self.context.fetch_data('volume')

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                Skewvv = np.zeros(20)
                for i in range(20):
                    Skewvv[i] = scipy.stats.skew(self.vol[di-self.delay-i-np.arange(20), ii], nan_policy='omit')
                temp = np.nanstd(Skewvv)
                if temp > 1e-5:
                    self.alpha[ii] = (np.nanmean(Skewvv) - Skewvv[0]) /temp

    def dependencies(self):
        self.register_dependency('volume')