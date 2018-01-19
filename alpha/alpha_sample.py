from alpha.alpha_base import AlphaBase
import numpy as np
import pickle
import csv


class AlphaSample(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.ret = self.context.fetch_data('return')
        self.vol = self.context.fetch_data('volume')
        self.cps = self.context.fetch_data('adj_close')
        self.cap = self.context.fetch_data('cap')
        self.stdret = np.zeros((len(self.context.di_list), len(self.context.ii_list)))
        self.det_liquid = np.zeros(len(self.context.ii_list))
        self.alpha = self.context.alpha

    def compute_day(self, di):
        if di == 2672:
            for ii in range(len(self.context.ii_list)):
                if np.nanmean(self.vol[di-self.delay-np.arange(244),ii]) * np.nanmean(self.cps[di-self.delay-np.arange(244),ii]) > 6650000 and np.nanmean(self.cap[di-self.delay-np.arange(244),ii]) > 665000000:
                    self.det_liquid[ii] = 1. 
#self.stdret[di][ii] = np.nanstd(self.ret[di-np.arange(63), ii])
#if di == 2843:
            np.savetxt("liquid_name.csv", self.det_liquid, delimiter=",")
            with open('liquid_name', 'wb') as output:
                pickle.dump(self.det_liquid, output)
#if self.is_valid[di][ii]:
#self.alpha[ii] = (self.cps[di-self.delay-5][ii] - self.cps[di-self.delay][ii])/self.cps[di-self.delay-5][ii]

    def dependencies(self):
        self.register_dependency('return')
        self.register_dependency('volume')
        self.register_dependency('adj_close')
        self.register_dependency('cap')
