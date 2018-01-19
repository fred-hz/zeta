from alpha.alpha_base import AlphaBase
import numpy as np
import util


class AlphaFinance(AlphaBase):
    def initialize(self):
        self.delay = int(self.params['delay'])
        self.is_valid = self.context.is_valid
        self.cps = self.context.fetch_data('adj_close')
        self.tRevenue = self.context.fetch_data("tRevenue")
        self.operateProfit = self.context.fetch_data("operateProfit")
        self.alpha = self.context.alpha
        self.datas1 = [[] for i in range(len(self.context.ii_list))]
        self.datas2 = [[] for i in range(len(self.context.ii_list))]
        self.mark = [True] * len(self.context.ii_list)

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                if self.mark[ii]:
                    for i in range(500):
                        if not np.isnan(self.operateProfit[di-self.delay-i][ii]) and not np.isnan(self.tRevenue[di-self.delay-i][ii]):
                            if len(self.datas1[ii]) == 0 or abs(self.datas1[ii][-1]-self.operateProfit[di-self.delay-i][ii]) > 1e-3:
                                self.datas1[ii].append(self.operateProfit[di-self.delay-i][ii])
                                self.datas2[ii].append(self.tRevenue[di-self.delay-i][ii])
                        if len(self.datas1[ii]) >= 8:
                            break
                    self.mark[ii] = False

                if not np.isnan(self.operateProfit[di-self.delay][ii]) and not np.isnan(self.tRevenue[di-self.delay][ii]):
                    if len(self.datas1[ii]) == 0 or abs(self.datas1[ii][-1]-self.operateProfit[di-self.delay][ii]) > 1e-3:
                        self.datas1[ii].append(self.operateProfit[di-self.delay][ii])
                        self.datas2[ii].append(self.tRevenue[di-self.delay][ii])
                
                    if len(self.datas1[ii]) >= 8:
                        temp = np.zeros(4)
                        for i in range(4):
                            temp[i] = (self.datas1[ii][-1-i]-self.datas1[ii][-1-i-4])/(self.datas2[ii][-1-i]-self.datas2[ii][-1-i-4])
                        util.rank(temp)
                        self.alpha[ii] = temp[0]

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('tRevenue')
        self.register_dependency('operateProfit')
