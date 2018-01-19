from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFdmtIndi_npMARgin(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.npMARgin = self.context.fetch_data("npMARgin")
        self.alpha = self.context.alpha
        self.datas = [[] for i in range(len(self.context.ii_list))]
        self.mark = [True] * len(self.context.ii_list)

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                if self.mark[ii]:
                    for i in range(500):
                        if not np.isnan(self.npMARgin[di-self.delay-i][ii]):
                            if len(self.datas[ii]) == 0 or abs(self.datas[ii][-1]-self.npMARgin[di-self.delay-i][ii]) > 1e-5:
                                self.datas[ii].append(self.npMARgin[di-self.delay-i][ii])
                        if len(self.datas[ii]) >= 8:
                            break
                    self.mark[ii] = False

                if not np.isnan(self.npMARgin[di-self.delay][ii]):
                    if len(self.datas[ii]) == 0 or abs(self.datas[ii][-1]-self.npMARgin[di-self.delay][ii]) > 1e-5:
                        self.datas[ii].append(self.npMARgin[di-self.delay][ii])
                
                    if len(self.datas[ii]) >= 8:
                        temp = np.zeros(4)
                        for i in range(4):
                            temp[i] = self.datas[ii][-1-i]-self.datas[ii][-1-i-4]
                        util.rank(temp)
                        self.alpha[ii] = temp[0]

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('npMARgin')
