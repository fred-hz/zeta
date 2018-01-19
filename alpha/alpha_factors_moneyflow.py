from alpha.alpha_base import AlphaBase
import numpy as np


class AlphaFactors_1(AlphaBase):
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
        self.AdminiExpenseRate = self.context.fetch_data('AdminiExpenseRate')
        self.DebtEquityRatio = self.context.fetch_data('DebtEquityRatio')
        self.EgibsLong = self.context.fetch_data('EgibsLong')
        self.GainLossVarianceRatio20 = self.context.fetch_data('GainLossVarianceRatio20')
        self.GainLossVarianceRatio60 = self.context.fetch_data('GainLossVarianceRatio60')
        self.MoneyFlow20 = self.context.fetch_data('MoneyFlow20')
        self.NetDebt = self.context.fetch_data('NetDebt')
        self.NRProfitLoss = self.context.fetch_data('NRProfitLoss')
        self.OBV = self.context.fetch_data('OBV')
        self.OBV6 = self.context.fetch_data('OBV6')
        self.OBV20 = self.context.fetch_data('OBV20')
        self.TreynorRatio20 = self.context.fetch_data('TreynorRatio20')
        self.TreynorRatio60 = self.context.fetch_data('TreynorRatio60')
        self.TreynorRatio120 = self.context.fetch_data('TreynorRatio120')
        self.cap = self.context.fetch_data('cap')
        self.alpha = self.context.alpha

    def compute_day(self, di):
        for ii in range(len(self.context.ii_list)):
            if self.is_valid[di][ii]:
                self.alpha[ii] = -self.MoneyFlow20[di-self.delay][ii]
#self.alpha[ii] = -self.MoneyFlow20[di-self.delay][ii]/self.cap[di-self.delay][ii]

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('cap')
        self.register_dependency('AdminiExpenseRate')
        self.register_dependency('DebtEquityRatio')
        self.register_dependency('EgibsLong')
        self.register_dependency('GainLossVarianceRatio20')
        self.register_dependency('GainLossVarianceRatio60')
        self.register_dependency('MoneyFlow20')
        self.register_dependency('NetDebt')
        self.register_dependency('NRProfitLoss')
        self.register_dependency('OBV')
        self.register_dependency('OBV6')
        self.register_dependency('OBV20')
        self.register_dependency('TreynorRatio20')
        self.register_dependency('TreynorRatio60')
        self.register_dependency('TreynorRatio120')
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
