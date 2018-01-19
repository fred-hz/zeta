from data_manager.dm_base import DataManagerBase
import numpy as np
import re, os


class DataManagerFactors(DataManagerBase):
    def __init__(self, params, context):
        super(DataManagerFactors, self).__init__(params=params, context=context)
        # Fetch data from context and identify values to variables
        self.data_path = self.params['dataPath']

    def initialize(self):
        self.ii_list = self.context.ii_list
        self.di_list = self.context.di_list

    def provide_data(self):
        di_size = len(self.context.di_list)
        ii_size = len(self.context.ii_list)

        self.REC = np.ndarray((di_size, ii_size), dtype=float)
        self.REC.flat = np.nan
        self.DAREC = np.ndarray((di_size, ii_size), dtype=float)
        self.DAREC.flat = np.nan
        self.GREC = np.ndarray((di_size, ii_size), dtype=float)
        self.GREC.flat = np.nan
        self.FY12P = np.ndarray((di_size, ii_size), dtype=float)
        self.FY12P.flat = np.nan
        self.DAREV = np.ndarray((di_size, ii_size), dtype=float)
        self.DAREV.flat = np.nan
        self.GREV = np.ndarray((di_size, ii_size), dtype=float)
        self.GREV.flat = np.nan
        self.SFY12P = np.ndarray((di_size, ii_size), dtype=float)
        self.SFY12P.flat = np.nan
        self.DASREV = np.ndarray((di_size, ii_size), dtype=float)
        self.DASREV.flat = np.nan
        self.GSREV = np.ndarray((di_size, ii_size), dtype=float)
        self.GSREV.flat = np.nan
        self.FEARNG = np.ndarray((di_size, ii_size), dtype=float)
        self.FEARNG.flat = np.nan
        self.FSALESG = np.ndarray((di_size, ii_size), dtype=float)
        self.FSALESG.flat = np.nan
        self.AdminiExpenseRate = np.ndarray((di_size, ii_size), dtype=float)
        self.AdminiExpenseRate.flat = np.nan
        self.DebtEquityRatio = np.ndarray((di_size, ii_size), dtype=float)
        self.DebtEquityRatio.flat = np.nan
        self.EgibsLong = np.ndarray((di_size, ii_size), dtype=float)
        self.EgibsLong.flat = np.nan
        self.GainLossVarianceRatio20 = np.ndarray((di_size, ii_size), dtype=float)
        self.GainLossVarianceRatio20.flat = np.nan
        self.GainLossVarianceRatio60 = np.ndarray((di_size, ii_size), dtype=float)
        self.GainLossVarianceRatio60.flat = np.nan
        self.MoneyFlow20 = np.ndarray((di_size, ii_size), dtype=float)
        self.MoneyFlow20.flat = np.nan
        self.NetDebt = np.ndarray((di_size, ii_size), dtype=float)
        self.NetDebt.flat = np.nan
        self.NRProfitLoss = np.ndarray((di_size, ii_size), dtype=float)
        self.NRProfitLoss.flat = np.nan
        self.OBV = np.ndarray((di_size, ii_size), dtype=float)
        self.OBV.flat = np.nan
        self.OBV6 = np.ndarray((di_size, ii_size), dtype=float)
        self.OBV6.flat = np.nan
        self.OBV20 = np.ndarray((di_size, ii_size), dtype=float)
        self.OBV20.flat = np.nan
        self.TreynorRatio20 = np.ndarray((di_size, ii_size), dtype=float)
        self.TreynorRatio20.flat = np.nan
        self.TreynorRatio60 = np.ndarray((di_size, ii_size), dtype=float)
        self.TreynorRatio60.flat = np.nan
        self.TreynorRatio120 = np.ndarray((di_size, ii_size), dtype=float)
        self.TreynorRatio120.flat = np.nan

        self.register_data('REC', self.REC)
        self.register_data('DAREC', self.DAREC)
        self.register_data('GREC', self.GREC)
        self.register_data('FY12P', self.FY12P)
        self.register_data('DAREV', self.DAREV)
        self.register_data('GREV', self.GREV)
        self.register_data('SFY12P', self.SFY12P)
        self.register_data('DASREV', self.DASREV)
        self.register_data('GSREV', self.GSREV)
        self.register_data('FEARNG', self.FEARNG)
        self.register_data('FSALESG', self.FSALESG)
        self.register_data('AdminiExpenseRate', self.AdminiExpenseRate)
        self.register_data('DebtEquityRatio', self.DebtEquityRatio)
        self.register_data('EgibsLong', self.EgibsLong)
        self.register_data('GainLossVarianceRatio20', self.GainLossVarianceRatio20)
        self.register_data('GainLossVarianceRatio60', self.GainLossVarianceRatio60)
        self.register_data('MoneyFlow20', self.MoneyFlow20)
        self.register_data('NetDebt', self.NetDebt)
        self.register_data('NRProfitLoss', self.NRProfitLoss)
        self.register_data('OBV', self.OBV)
        self.register_data('OBV6', self.OBV6)
        self.register_data('OBV20', self.OBV20)
        self.register_data('TreynorRatio20', self.TreynorRatio20)
        self.register_data('TreynorRatio60', self.TreynorRatio60)
        self.register_data('TreynorRatio120', self.TreynorRatio120)

    def compute_day(self, di):
        pass

    def dependencies(self):
        # Do not need dependencies in DataManagerBaseData
        pass

    def caches(self):
        self.register_cache('REC')
        self.register_cache('DAREC')
        self.register_cache('GREC')
        self.register_cache('FY12P')
        self.register_cache('DAREV')
        self.register_cache('GREV')
        self.register_cache('SFY12P')
        self.register_cache('DASREV')
        self.register_cache('GSREV')
        self.register_cache('FEARNG')
        self.register_cache('FSALESG')
        self.register_cache('AdminiExpenseRate')
        self.register_cache('DebtEquityRatio')
        self.register_cache('EgibsLong')
        self.register_cache('GainLossVarianceRatio20')
        self.register_cache('GainLossVarianceRatio60')
        self.register_cache('MoneyFlow20')
        self.register_cache('NetDebt')
        self.register_cache('NRProfitLoss')
        self.register_cache('OBV')
        self.register_cache('OBV6')
        self.register_cache('OBV20')
        self.register_cache('TreynorRatio20')
        self.register_cache('TreynorRatio60')
        self.register_cache('TreynorRatio120')

    def freshes(self):
        self.register_fresh('REC')
        self.register_fresh('DAREC')
        self.register_fresh('GREC')
        self.register_fresh('FY12P')
        self.register_fresh('DAREV')
        self.register_fresh('GREV')
        self.register_fresh('SFY12P')
        self.register_fresh('DASREV')
        self.register_fresh('GSREV')
        self.register_fresh('FEARNG')
        self.register_fresh('FSALESG')
        self.register_fresh('AdminiExpenseRate')
        self.register_fresh('DebtEquityRatio')
        self.register_fresh('EgibsLong')
        self.register_fresh('GainLossVarianceRatio20')
        self.register_fresh('GainLossVarianceRatio60')
        self.register_fresh('MoneyFlow20')
        self.register_fresh('NetDebt')
        self.register_fresh('NRProfitLoss')
        self.register_fresh('OBV')
        self.register_fresh('OBV6')
        self.register_fresh('OBV20')
        self.register_fresh('TreynorRatio20')
        self.register_fresh('TreynorRatio60')
        self.register_fresh('TreynorRatio120')

