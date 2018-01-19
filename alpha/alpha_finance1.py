from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFinance(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.TAssets = self.context.fetch_data("TAssets")
        self.TCA = self.context.fetch_data("TCA")
        self.alpha = self.context.alpha
        self.datas = [[] for i in range(len(self.context.ii_list))]
        self.mark = [True] * len(self.context.ii_list)

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                if self.mark[ii]:
                    for i in range(500):
                        if abs(self.TAssets[di-self.delay-i][ii]) > 1e-3 and not np.isnan(self.TCA[di-self.delay-i][ii]) and not np.isnan(self.TAssets[di-self.delay-i][ii]):
                            temp = self.TCA[di-self.delay-i][ii]/self.TAssets[di-self.delay-i][ii]
                            if len(self.datas[ii]) == 0 or abs(temp - self.datas[ii][-1]) > 1e-3:
                                self.datas[ii].append(temp)
                        if len(self.datas[ii]) >= 8:
                            break
                    self.mark[ii] = False

                if abs(self.TAssets[di-self.delay][ii]) > 1e-3 and not np.isnan(self.TCA[di-self.delay][ii]) and not np.isnan(self.TAssets[di-self.delay][ii]):
                    temp = self.TCA[di-self.delay][ii]/self.TAssets[di-self.delay][ii]
                    if len(self.datas[ii]) == 0 or abs(temp - self.datas[ii][-1]) > 1e-3:
                        self.datas[ii].append(temp)
                
                    if len(self.datas[ii]) >= 8:
                        temp = np.zeros(4)
                        for i in range(4):
                            temp[i] = self.datas[ii][-1-i]/self.datas[ii][-1-i-4]
                        util.rank(temp)
                        self.alpha[ii] = temp[0]

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('TAssets')
        self.register_dependency('TCA')
