from data_manager.dm_base import DataManagerBase
import numpy as np
import re, os


class DataManagerFdmtIndi(DataManagerBase):
    def __init__(self, params, context):
        super(DataManagerFdmtIndi, self).__init__(params=params, context=context)
        # Fetch data from context and identify values to variables
        self.data_path = self.params['dataPath']

    def initialize(self):
        self.ii_list = self.context.ii_list
        self.di_list = self.context.di_list

    def provide_data(self):
        di_size = len(self.context.di_list)
        ii_size = len(self.context.ii_list)

        self.APTurnover = np.ndarray((di_size, ii_size), dtype=float)
        self.APTurnover.flat = np.nan
        self.ARTurnover = np.ndarray((di_size, ii_size), dtype=float)
        self.ARTurnover.flat = np.nan
        self.basicEPS = np.ndarray((di_size, ii_size), dtype=float)
        self.basicEPS.flat = np.nan
        self.basicEPSYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.basicEPSYOY.flat = np.nan
        self.caTurnover = np.ndarray((di_size, ii_size), dtype=float)
        self.caTurnover.flat = np.nan
        self.cReserPS = np.ndarray((di_size, ii_size), dtype=float)
        self.cReserPS.flat = np.nan
        self.DA = np.ndarray((di_size, ii_size), dtype=float)
        self.DA.flat = np.nan
        self.daysAP = np.ndarray((di_size, ii_size), dtype=float)
        self.daysAP.flat = np.nan
        self.daysAR = np.ndarray((di_size, ii_size), dtype=float)
        self.daysAR.flat = np.nan
        self.daysInven = np.ndarray((di_size, ii_size), dtype=float)
        self.daysInven.flat = np.nan
        self.dilutedEPS = np.ndarray((di_size, ii_size), dtype=float)
        self.dilutedEPS.flat = np.nan
        self.dilutedEPSYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.dilutedEPSYOY.flat = np.nan
        self.EBIAT = np.ndarray((di_size, ii_size), dtype=float)
        self.EBIAT.flat = np.nan
        self.EBIT = np.ndarray((di_size, ii_size), dtype=float)
        self.EBIT.flat = np.nan
        self.EBITDA = np.ndarray((di_size, ii_size), dtype=float)
        self.EBITDA.flat = np.nan
        self.EBITPS = np.ndarray((di_size, ii_size), dtype=float)
        self.EBITPS.flat = np.nan
        self.EPS = np.ndarray((di_size, ii_size), dtype=float)
        self.EPS.flat = np.nan
        self.faTurnover = np.ndarray((di_size, ii_size), dtype=float)
        self.faTurnover.flat = np.nan
        self.FCFE = np.ndarray((di_size, ii_size), dtype=float)
        self.FCFE.flat = np.nan
        self.FCFEPS = np.ndarray((di_size, ii_size), dtype=float)
        self.FCFEPS.flat = np.nan
        self.FCFF = np.ndarray((di_size, ii_size), dtype=float)
        self.FCFF.flat = np.nan
        self.FCFFPS = np.ndarray((di_size, ii_size), dtype=float)
        self.FCFFPS.flat = np.nan
        self.grossMARgin = np.ndarray((di_size, ii_size), dtype=float)
        self.grossMARgin.flat = np.nan
        self.grossProfit = np.ndarray((di_size, ii_size), dtype=float)
        self.grossProfit.flat = np.nan
        self.IC = np.ndarray((di_size, ii_size), dtype=float)
        self.IC.flat = np.nan
        self.intCl = np.ndarray((di_size, ii_size), dtype=float)
        self.intCl.flat = np.nan
        self.intDebt = np.ndarray((di_size, ii_size), dtype=float)
        self.intDebt.flat = np.nan
        self.intFreeCl = np.ndarray((di_size, ii_size), dtype=float)
        self.intFreeCl.flat = np.nan
        self.intFreeNcl = np.ndarray((di_size, ii_size), dtype=float)
        self.intFreeNcl.flat = np.nan
        self.invenTurnover = np.ndarray((di_size, ii_size), dtype=float)
        self.invenTurnover.flat = np.nan
        self.naPSYTD = np.ndarray((di_size, ii_size), dtype=float)
        self.naPSYTD.flat = np.nan
        self.nAssetPS = np.ndarray((di_size, ii_size), dtype=float)
        self.nAssetPS.flat = np.nan
        self.naYTD = np.ndarray((di_size, ii_size), dtype=float)
        self.naYTD.flat = np.nan
        self.nCfOpaPSYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.nCfOpaPSYOY.flat = np.nan
        self.nCfOpaYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.nCfOpaYOY.flat = np.nan
        self.nCfOperAPS = np.ndarray((di_size, ii_size), dtype=float)
        self.nCfOperAPS.flat = np.nan
        self.nCInCashPS = np.ndarray((di_size, ii_size), dtype=float)
        self.nCInCashPS.flat = np.nan
        self.nDebt = np.ndarray((di_size, ii_size), dtype=float)
        self.nDebt.flat = np.nan
        self.niAttrPCut = np.ndarray((di_size, ii_size), dtype=float)
        self.niAttrPCut.flat = np.nan
        self.niAttrPCutYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.niAttrPCutYOY.flat = np.nan
        self.niAttrPYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.niAttrPYOY.flat = np.nan
        self.nIntExp = np.ndarray((di_size, ii_size), dtype=float)
        self.nIntExp.flat = np.nan
        self.niYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.niYOY.flat = np.nan
        self.npMARgin = np.ndarray((di_size, ii_size), dtype=float)
        self.npMARgin.flat = np.nan
        self.nrProfitLoss = np.ndarray((di_size, ii_size), dtype=float)
        self.nrProfitLoss.flat = np.nan
        self.nTanAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.nTanAssets.flat = np.nan
        self.nWorkCapital = np.ndarray((di_size, ii_size), dtype=float)
        self.nWorkCapital.flat = np.nan
        self.opaProfit = np.ndarray((di_size, ii_size), dtype=float)
        self.opaProfit.flat = np.nan
        self.operCycle = np.ndarray((di_size, ii_size), dtype=float)
        self.operCycle.flat = np.nan
        self.operProfitYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.operProfitYOY.flat = np.nan
        self.opPS = np.ndarray((di_size, ii_size), dtype=float)
        self.opPS.flat = np.nan
        self.rePS = np.ndarray((di_size, ii_size), dtype=float)
        self.rePS.flat = np.nan
        self.reserPS = np.ndarray((di_size, ii_size), dtype=float)
        self.reserPS.flat = np.nan
        self.revenueYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.revenueYOY.flat = np.nan
        self.revPS = np.ndarray((di_size, ii_size), dtype=float)
        self.revPS.flat = np.nan
        self.ROA = np.ndarray((di_size, ii_size), dtype=float)
        self.ROA.flat = np.nan
        self.ROAEBIT = np.ndarray((di_size, ii_size), dtype=float)
        self.ROAEBIT.flat = np.nan
        self.ROE = np.ndarray((di_size, ii_size), dtype=float)
        self.ROE.flat = np.nan
        self.ROEA = np.ndarray((di_size, ii_size), dtype=float)
        self.ROEA.flat = np.nan
        self.ROECut = np.ndarray((di_size, ii_size), dtype=float)
        self.ROECut.flat = np.nan
        self.ROECutW = np.ndarray((di_size, ii_size), dtype=float)
        self.ROECutW.flat = np.nan
        self.ROEW = np.ndarray((di_size, ii_size), dtype=float)
        self.ROEW.flat = np.nan
        self.ROEYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.ROEYOY.flat = np.nan
        self.ROIC = np.ndarray((di_size, ii_size), dtype=float)
        self.ROIC.flat = np.nan
        self.sReserPS = np.ndarray((di_size, ii_size), dtype=float)
        self.sReserPS.flat = np.nan
        self.taTurnover = np.ndarray((di_size, ii_size), dtype=float)
        self.taTurnover.flat = np.nan
        self.taYTD = np.ndarray((di_size, ii_size), dtype=float)
        self.taYTD.flat = np.nan
        self.teAttrPYTD = np.ndarray((di_size, ii_size), dtype=float)
        self.teAttrPYTD.flat = np.nan
        self.tfaTurnover = np.ndarray((di_size, ii_size), dtype=float)
        self.tfaTurnover.flat = np.nan
        self.tFixedAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.tFixedAssets.flat = np.nan
        self.tProfitYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.tProfitYOY.flat = np.nan
        self.tRe = np.ndarray((di_size, ii_size), dtype=float)
        self.tRe.flat = np.nan
        self.tRePS = np.ndarray((di_size, ii_size), dtype=float)
        self.tRePS.flat = np.nan
        self.tRevenueYOY = np.ndarray((di_size, ii_size), dtype=float)
        self.tRevenueYOY.flat = np.nan
        self.tRevPS = np.ndarray((di_size, ii_size), dtype=float)
        self.tRevPS.flat = np.nan
        self.valChgProfit = np.ndarray((di_size, ii_size), dtype=float)
        self.valChgProfit.flat = np.nan
        self.workCapital = np.ndarray((di_size, ii_size), dtype=float)
        self.workCapital.flat = np.nan

        self.register_data('APTurnover', self.APTurnover)
        self.register_data('ARTurnover', self.ARTurnover)
        self.register_data('basicEPS', self.basicEPS)
        self.register_data('basicEPSYOY', self.basicEPSYOY)
        self.register_data('caTurnover', self.caTurnover)
        self.register_data('cReserPS', self.cReserPS)
        self.register_data('DA', self.DA)
        self.register_data('daysAP', self.daysAP)
        self.register_data('daysAR', self.daysAR)
        self.register_data('daysInven', self.daysInven)
        self.register_data('dilutedEPS', self.dilutedEPS)
        self.register_data('dilutedEPSYOY', self.dilutedEPSYOY)
        self.register_data('EBIAT', self.EBIAT)
        self.register_data('EBIT', self.EBIT)
        self.register_data('EBITDA', self.EBITDA)
        self.register_data('EBITPS', self.EBITPS)
        self.register_data('EPS', self.EPS)
        self.register_data('faTurnover', self.faTurnover)
        self.register_data('FCFE', self.FCFE)
        self.register_data('FCFEPS', self.FCFEPS)
        self.register_data('FCFF', self.FCFF)
        self.register_data('FCFFPS', self.FCFFPS)
        self.register_data('grossMARgin', self.grossMARgin)
        self.register_data('grossProfit', self.grossProfit)
        self.register_data('IC', self.IC)
        self.register_data('intCl', self.intCl)
        self.register_data('intDebt', self.intDebt)
        self.register_data('intFreeCl', self.intFreeCl)
        self.register_data('intFreeNcl', self.intFreeNcl)
        self.register_data('invenTurnover', self.invenTurnover)
        self.register_data('naPSYTD', self.naPSYTD)
        self.register_data('nAssetPS', self.nAssetPS)
        self.register_data('naYTD', self.naYTD)
        self.register_data('nCfOpaPSYOY', self.nCfOpaPSYOY)
        self.register_data('nCfOpaYOY', self.nCfOpaYOY)
        self.register_data('nCfOperAPS', self.nCfOperAPS)
        self.register_data('nCInCashPS', self.nCInCashPS)
        self.register_data('nDebt', self.nDebt)
        self.register_data('niAttrPCut', self.niAttrPCut)
        self.register_data('niAttrPCutYOY', self.niAttrPCutYOY)
        self.register_data('niAttrPYOY', self.niAttrPYOY)
        self.register_data('nIntExp', self.nIntExp)
        self.register_data('niYOY', self.niYOY)
        self.register_data('npMARgin', self.npMARgin)
        self.register_data('nrProfitLoss', self.nrProfitLoss)
        self.register_data('nTanAssets', self.nTanAssets)
        self.register_data('nWorkCapital', self.nWorkCapital)
        self.register_data('opaProfit', self.opaProfit)
        self.register_data('operCycle', self.operCycle)
        self.register_data('operProfitYOY', self.operProfitYOY)
        self.register_data('opPS', self.opPS)
        self.register_data('rePS', self.rePS)
        self.register_data('reserPS', self.reserPS)
        self.register_data('revenueYOY', self.revenueYOY)
        self.register_data('revPS', self.revPS)
        self.register_data('ROA', self.ROA)
        self.register_data('ROAEBIT', self.ROAEBIT)
        self.register_data('ROE', self.ROE)
        self.register_data('ROEA', self.ROEA)
        self.register_data('ROECut', self.ROECut)
        self.register_data('ROECutW', self.ROECutW)
        self.register_data('ROEW', self.ROEW)
        self.register_data('ROEYOY', self.ROEYOY)
        self.register_data('ROIC', self.ROIC)
        self.register_data('sReserPS', self.sReserPS)
        self.register_data('taTurnover', self.taTurnover)
        self.register_data('taYTD', self.taYTD)
        self.register_data('teAttrPYTD', self.teAttrPYTD)
        self.register_data('tfaTurnover', self.tfaTurnover)
        self.register_data('tFixedAssets', self.tFixedAssets)
        self.register_data('tProfitYOY', self.tProfitYOY)
        self.register_data('tRe', self.tRe)
        self.register_data('tRePS', self.tRePS)
        self.register_data('tRevenueYOY', self.tRevenueYOY)
        self.register_data('tRevPS', self.tRevPS)
        self.register_data('valChgProfit', self.valChgProfit)
        self.register_data('workCapital', self.workCapital)

    def compute_day(self, di):
        pass

    def dependencies(self):
        # Do not need dependencies in DataManagerBaseData
        pass

    def caches(self):
        self.register_cache('APTurnover')
        self.register_cache('ARTurnover')
        self.register_cache('basicEPS')
        self.register_cache('basicEPSYOY')
        self.register_cache('caTurnover')
        self.register_cache('cReserPS')
        self.register_cache('DA')
        self.register_cache('daysAP')
        self.register_cache('daysAR')
        self.register_cache('daysInven')
        self.register_cache('dilutedEPS')
        self.register_cache('dilutedEPSYOY')
        self.register_cache('EBIAT')
        self.register_cache('EBIT')
        self.register_cache('EBITDA')
        self.register_cache('EBITPS')
        self.register_cache('EPS')
        self.register_cache('faTurnover')
        self.register_cache('FCFE')
        self.register_cache('FCFEPS')
        self.register_cache('FCFF')
        self.register_cache('FCFFPS')
        self.register_cache('grossMARgin')
        self.register_cache('grossProfit')
        self.register_cache('IC')
        self.register_cache('intCl')
        self.register_cache('intDebt')
        self.register_cache('intFreeCl')
        self.register_cache('intFreeNcl')
        self.register_cache('invenTurnover')
        self.register_cache('naPSYTD')
        self.register_cache('nAssetPS')
        self.register_cache('naYTD')
        self.register_cache('nCfOpaPSYOY')
        self.register_cache('nCfOpaYOY')
        self.register_cache('nCfOperAPS')
        self.register_cache('nCInCashPS')
        self.register_cache('nDebt')
        self.register_cache('niAttrPCut')
        self.register_cache('niAttrPCutYOY')
        self.register_cache('niAttrPYOY')
        self.register_cache('nIntExp')
        self.register_cache('niYOY')
        self.register_cache('npMARgin')
        self.register_cache('nrProfitLoss')
        self.register_cache('nTanAssets')
        self.register_cache('nWorkCapital')
        self.register_cache('opaProfit')
        self.register_cache('operCycle')
        self.register_cache('operProfitYOY')
        self.register_cache('opPS')
        self.register_cache('rePS')
        self.register_cache('reserPS')
        self.register_cache('revenueYOY')
        self.register_cache('revPS')
        self.register_cache('ROA')
        self.register_cache('ROAEBIT')
        self.register_cache('ROE')
        self.register_cache('ROEA')
        self.register_cache('ROECut')
        self.register_cache('ROECutW')
        self.register_cache('ROEW')
        self.register_cache('ROEYOY')
        self.register_cache('ROIC')
        self.register_cache('sReserPS')
        self.register_cache('taTurnover')
        self.register_cache('taYTD')
        self.register_cache('teAttrPYTD')
        self.register_cache('tfaTurnover')
        self.register_cache('tFixedAssets')
        self.register_cache('tProfitYOY')
        self.register_cache('tRe')
        self.register_cache('tRePS')
        self.register_cache('tRevenueYOY')
        self.register_cache('tRevPS')
        self.register_cache('valChgProfit')
        self.register_cache('workCapital')

    def freshes(self):
        self.register_fresh('APTurnover')
        self.register_fresh('ARTurnover')
        self.register_fresh('basicEPS')
        self.register_fresh('basicEPSYOY')
        self.register_fresh('caTurnover')
        self.register_fresh('cReserPS')
        self.register_fresh('DA')
        self.register_fresh('daysAP')
        self.register_fresh('daysAR')
        self.register_fresh('daysInven')
        self.register_fresh('dilutedEPS')
        self.register_fresh('dilutedEPSYOY')
        self.register_fresh('EBIAT')
        self.register_fresh('EBIT')
        self.register_fresh('EBITDA')
        self.register_fresh('EBITPS')
        self.register_fresh('EPS')
        self.register_fresh('faTurnover')
        self.register_fresh('FCFE')
        self.register_fresh('FCFEPS')
        self.register_fresh('FCFF')
        self.register_fresh('FCFFPS')
        self.register_fresh('grossMARgin')
        self.register_fresh('grossProfit')
        self.register_fresh('IC')
        self.register_fresh('intCl')
        self.register_fresh('intDebt')
        self.register_fresh('intFreeCl')
        self.register_fresh('intFreeNcl')
        self.register_fresh('invenTurnover')
        self.register_fresh('naPSYTD')
        self.register_fresh('nAssetPS')
        self.register_fresh('naYTD')
        self.register_fresh('nCfOpaPSYOY')
        self.register_fresh('nCfOpaYOY')
        self.register_fresh('nCfOperAPS')
        self.register_fresh('nCInCashPS')
        self.register_fresh('nDebt')
        self.register_fresh('niAttrPCut')
        self.register_fresh('niAttrPCutYOY')
        self.register_fresh('niAttrPYOY')
        self.register_fresh('nIntExp')
        self.register_fresh('niYOY')
        self.register_fresh('npMARgin')
        self.register_fresh('nrProfitLoss')
        self.register_fresh('nTanAssets')
        self.register_fresh('nWorkCapital')
        self.register_fresh('opaProfit')
        self.register_fresh('operCycle')
        self.register_fresh('operProfitYOY')
        self.register_fresh('opPS')
        self.register_fresh('rePS')
        self.register_fresh('reserPS')
        self.register_fresh('revenueYOY')
        self.register_fresh('revPS')
        self.register_fresh('ROA')
        self.register_fresh('ROAEBIT')
        self.register_fresh('ROE')
        self.register_fresh('ROEA')
        self.register_fresh('ROECut')
        self.register_fresh('ROECutW')
        self.register_fresh('ROEW')
        self.register_fresh('ROEYOY')
        self.register_fresh('ROIC')
        self.register_fresh('sReserPS')
        self.register_fresh('taTurnover')
        self.register_fresh('taYTD')
        self.register_fresh('teAttrPYTD')
        self.register_fresh('tfaTurnover')
        self.register_fresh('tFixedAssets')
        self.register_fresh('tProfitYOY')
        self.register_fresh('tRe')
        self.register_fresh('tRePS')
        self.register_fresh('tRevenueYOY')
        self.register_fresh('tRevPS')
        self.register_fresh('valChgProfit')
        self.register_fresh('workCapital')
