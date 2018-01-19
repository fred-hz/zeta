from data_manager.dm_base import DataManagerBase
import numpy as np
import re, os


class DataManagerFinance(DataManagerBase):
    def __init__(self, params, context):
        super(DataManagerFinance, self).__init__(params=params, context=context)
        # Fetch data from context and identify values to variables
        self.data_path = self.params['dataPath']

    def initialize(self):
        self.ii_list = self.context.ii_list
        self.di_list = self.context.di_list

    def provide_data(self):
        di_size = len(self.context.di_list)
        ii_size = len(self.context.ii_list)

        self.adminExp = np.ndarray((di_size, ii_size), dtype=float)
        self.adminExp.flat = np.nan
        self.advanceReceipts = np.ndarray((di_size, ii_size), dtype=float)
        self.advanceReceipts.flat = np.nan
        self.AJInvestIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.AJInvestIncome.flat = np.nan
        self.AP = np.ndarray((di_size, ii_size), dtype=float)
        self.AP.flat = np.nan
        self.AR = np.ndarray((di_size, ii_size), dtype=float)
        self.AR.flat = np.nan
        self.assetsImpairLoss = np.ndarray((di_size, ii_size), dtype=float)
        self.assetsImpairLoss.flat = np.nan
        self.availForSaleFa = np.ndarray((di_size, ii_size), dtype=float)
        self.availForSaleFa.flat = np.nan
        self.basicEPS = np.ndarray((di_size, ii_size), dtype=float)
        self.basicEPS.flat = np.nan
        self.bizTaxSurchg = np.ndarray((di_size, ii_size), dtype=float)
        self.bizTaxSurchg.flat = np.nan
        self.bondPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.bondPayable.flat = np.nan
        self.capitalReser = np.ndarray((di_size, ii_size), dtype=float)
        self.capitalReser.flat = np.nan
        self.cashCEquiv = np.ndarray((di_size, ii_size), dtype=float)
        self.cashCEquiv.flat = np.nan
        self.CBBorr = np.ndarray((di_size, ii_size), dtype=float)
        self.CBBorr.flat = np.nan
        self.CFrBorr = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrBorr.flat = np.nan
        self.CFrCapContr = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrCapContr.flat = np.nan
        self.CFrIssueBond = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrIssueBond.flat = np.nan
        self.CFrMinoSSubs = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrMinoSSubs.flat = np.nan
        self.CFrOthFinanA = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrOthFinanA.flat = np.nan
        self.CFrOthInvestA = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrOthInvestA.flat = np.nan
        self.CFrOthOperateA = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrOthOperateA.flat = np.nan
        self.CFrSaleGS = np.ndarray((di_size, ii_size), dtype=float)
        self.CFrSaleGS.flat = np.nan
        self.CInfFrFinanA = np.ndarray((di_size, ii_size), dtype=float)
        self.CInfFrFinanA.flat = np.nan
        self.CInfFrInvestA = np.ndarray((di_size, ii_size), dtype=float)
        self.CInfFrInvestA.flat = np.nan
        self.CInfFrOperateA = np.ndarray((di_size, ii_size), dtype=float)
        self.CInfFrOperateA.flat = np.nan
        self.CIP = np.ndarray((di_size, ii_size), dtype=float)
        self.CIP.flat = np.nan
        self.COGS = np.ndarray((di_size, ii_size), dtype=float)
        self.COGS.flat = np.nan
        self.commisExp = np.ndarray((di_size, ii_size), dtype=float)
        self.commisExp.flat = np.nan
        self.commisIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.commisIncome.flat = np.nan
        self.commisPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.commisPayable.flat = np.nan
        self.comprIncAttrMS = np.ndarray((di_size, ii_size), dtype=float)
        self.comprIncAttrMS.flat = np.nan
        self.comprIncAttrP = np.ndarray((di_size, ii_size), dtype=float)
        self.comprIncAttrP.flat = np.nan
        self.constMaterials = np.ndarray((di_size, ii_size), dtype=float)
        self.constMaterials.flat = np.nan
        self.COutfFrFinanA = np.ndarray((di_size, ii_size), dtype=float)
        self.COutfFrFinanA.flat = np.nan
        self.COutfFrInvestA = np.ndarray((di_size, ii_size), dtype=float)
        self.COutfFrInvestA.flat = np.nan
        self.COutfOperateA = np.ndarray((di_size, ii_size), dtype=float)
        self.COutfOperateA.flat = np.nan
        self.CPaidDivProfInt = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidDivProfInt.flat = np.nan
        self.CPaidForDebts = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidForDebts.flat = np.nan
        self.CPaidForOthOpA = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidForOthOpA.flat = np.nan
        self.CPaidForTaxes = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidForTaxes.flat = np.nan
        self.CPaidGS = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidGS.flat = np.nan
        self.CPaidIFC = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidIFC.flat = np.nan
        self.CPaidInvest = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidInvest.flat = np.nan
        self.CPaidOthFinanA = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidOthFinanA.flat = np.nan
        self.CPaidOthInvestA = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidOthInvestA.flat = np.nan
        self.CPaidPolDiv = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidPolDiv.flat = np.nan
        self.CPaidToForEmpl = np.ndarray((di_size, ii_size), dtype=float)
        self.CPaidToForEmpl.flat = np.nan
        self.deferTaxAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.deferTaxAssets.flat = np.nan
        self.deferTaxLiab = np.ndarray((di_size, ii_size), dtype=float)
        self.deferTaxLiab.flat = np.nan
        self.depos = np.ndarray((di_size, ii_size), dtype=float)
        self.depos.flat = np.nan
        self.dilutedEPS = np.ndarray((di_size, ii_size), dtype=float)
        self.dilutedEPS.flat = np.nan
        self.disburLA = np.ndarray((di_size, ii_size), dtype=float)
        self.disburLA.flat = np.nan
        self.dispFixAssetsOth = np.ndarray((di_size, ii_size), dtype=float)
        self.dispFixAssetsOth.flat = np.nan
        self.divPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.divPayable.flat = np.nan
        self.divProfSubsMinoS = np.ndarray((di_size, ii_size), dtype=float)
        self.divProfSubsMinoS.flat = np.nan
        self.divReceiv = np.ndarray((di_size, ii_size), dtype=float)
        self.divReceiv.flat = np.nan
        self.estimatedLiab = np.ndarray((di_size, ii_size), dtype=float)
        self.estimatedLiab.flat = np.nan
        self.finanExp = np.ndarray((di_size, ii_size), dtype=float)
        self.finanExp.flat = np.nan
        self.fixedAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.fixedAssets.flat = np.nan
        self.fixedAssetsDisp = np.ndarray((di_size, ii_size), dtype=float)
        self.fixedAssetsDisp.flat = np.nan
        self.forexDiffer = np.ndarray((di_size, ii_size), dtype=float)
        self.forexDiffer.flat = np.nan
        self.forexEffects = np.ndarray((di_size, ii_size), dtype=float)
        self.forexEffects.flat = np.nan
        self.forexGain = np.ndarray((di_size, ii_size), dtype=float)
        self.forexGain.flat = np.nan
        self.fundsSecTradAgen = np.ndarray((di_size, ii_size), dtype=float)
        self.fundsSecTradAgen.flat = np.nan
        self.fundsSecUndwAgen = np.ndarray((di_size, ii_size), dtype=float)
        self.fundsSecUndwAgen.flat = np.nan
        self.fValueChgGain = np.ndarray((di_size, ii_size), dtype=float)
        self.fValueChgGain.flat = np.nan
        self.gainInvest = np.ndarray((di_size, ii_size), dtype=float)
        self.gainInvest.flat = np.nan
        self.goodwill = np.ndarray((di_size, ii_size), dtype=float)
        self.goodwill.flat = np.nan
        self.htmInvest = np.ndarray((di_size, ii_size), dtype=float)
        self.htmInvest.flat = np.nan
        self.IFCCashIncr = np.ndarray((di_size, ii_size), dtype=float)
        self.IFCCashIncr.flat = np.nan
        self.incomeTax = np.ndarray((di_size, ii_size), dtype=float)
        self.incomeTax.flat = np.nan
        self.insurReser = np.ndarray((di_size, ii_size), dtype=float)
        self.insurReser.flat = np.nan
        self.intanAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.intanAssets.flat = np.nan
        self.intExp = np.ndarray((di_size, ii_size), dtype=float)
        self.intExp.flat = np.nan
        self.intIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.intIncome.flat = np.nan
        self.intPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.intPayable.flat = np.nan
        self.intReceiv = np.ndarray((di_size, ii_size), dtype=float)
        self.intReceiv.flat = np.nan
        self.inventories = np.ndarray((di_size, ii_size), dtype=float)
        self.inventories.flat = np.nan
        self.investIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.investIncome.flat = np.nan
        self.investRealEstate = np.ndarray((di_size, ii_size), dtype=float)
        self.investRealEstate.flat = np.nan
        self.loanFrOthBankFi = np.ndarray((di_size, ii_size), dtype=float)
        self.loanFrOthBankFi.flat = np.nan
        self.loanToOthBankFi = np.ndarray((di_size, ii_size), dtype=float)
        self.loanToOthBankFi.flat = np.nan
        self.LTAmorExp = np.ndarray((di_size, ii_size), dtype=float)
        self.LTAmorExp.flat = np.nan
        self.LTBorr = np.ndarray((di_size, ii_size), dtype=float)
        self.LTBorr.flat = np.nan
        self.LTEquityInvest = np.ndarray((di_size, ii_size), dtype=float)
        self.LTEquityInvest.flat = np.nan
        self.LTPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.LTPayable.flat = np.nan
        self.LTReceive = np.ndarray((di_size, ii_size), dtype=float)
        self.LTReceive.flat = np.nan
        self.minorityGain = np.ndarray((di_size, ii_size), dtype=float)
        self.minorityGain.flat = np.nan
        self.minorityInt = np.ndarray((di_size, ii_size), dtype=float)
        self.minorityInt.flat = np.nan
        self.NCADisploss = np.ndarray((di_size, ii_size), dtype=float)
        self.NCADisploss.flat = np.nan
        self.NCApIncrRepur = np.ndarray((di_size, ii_size), dtype=float)
        self.NCApIncrRepur.flat = np.nan
        self.NCAWithin1Y = np.ndarray((di_size, ii_size), dtype=float)
        self.NCAWithin1Y.flat = np.nan
        self.NCEBegBal = np.ndarray((di_size, ii_size), dtype=float)
        self.NCEBegBal.flat = np.nan
        self.NCEEndBal = np.ndarray((di_size, ii_size), dtype=float)
        self.NCEEndBal.flat = np.nan
        self.NCFFrFinanA = np.ndarray((di_size, ii_size), dtype=float)
        self.NCFFrFinanA.flat = np.nan
        self.NCFFrInvestA = np.ndarray((di_size, ii_size), dtype=float)
        self.NCFFrInvestA.flat = np.nan
        self.NCFOperateA = np.ndarray((di_size, ii_size), dtype=float)
        self.NCFOperateA.flat = np.nan
        self.NChangeInCash = np.ndarray((di_size, ii_size), dtype=float)
        self.NChangeInCash.flat = np.nan
        self.NCLWithin1Y = np.ndarray((di_size, ii_size), dtype=float)
        self.NCLWithin1Y.flat = np.nan
        self.NCompensPayout = np.ndarray((di_size, ii_size), dtype=float)
        self.NCompensPayout.flat = np.nan
        self.NCPaidAcquis = np.ndarray((di_size, ii_size), dtype=float)
        self.NCPaidAcquis.flat = np.nan
        self.NDeposIncrCFI = np.ndarray((di_size, ii_size), dtype=float)
        self.NDeposIncrCFI.flat = np.nan
        self.NDispSubsOthBizC = np.ndarray((di_size, ii_size), dtype=float)
        self.NDispSubsOthBizC.flat = np.nan
        self.NIncBorrOthFI = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncBorrOthFI.flat = np.nan
        self.NIncDisburOfLA = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncDisburOfLA.flat = np.nan
        self.NIncDispTradFA = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncDispTradFA.flat = np.nan
        self.NIncFrBorr = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncFrBorr.flat = np.nan
        self.NIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncome.flat = np.nan
        self.NIncomeAttrP = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncomeAttrP.flat = np.nan
        self.NIncPhDeposInv = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncPhDeposInv.flat = np.nan
        self.NIncrBorrFrCB = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncrBorrFrCB.flat = np.nan
        self.NIncrDeposInFI = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncrDeposInFI.flat = np.nan
        self.NIncrPledgeLoan = np.ndarray((di_size, ii_size), dtype=float)
        self.NIncrPledgeLoan.flat = np.nan
        self.NoperateExp = np.ndarray((di_size, ii_size), dtype=float)
        self.NoperateExp.flat = np.nan
        self.NoperateIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.NoperateIncome.flat = np.nan
        self.NotesPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.NotesPayable.flat = np.nan
        self.NotesReceiv = np.ndarray((di_size, ii_size), dtype=float)
        self.NotesReceiv.flat = np.nan
        self.NReinsurPrem = np.ndarray((di_size, ii_size), dtype=float)
        self.NReinsurPrem.flat = np.nan
        self.oilAndGasAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.oilAndGasAssets.flat = np.nan
        self.operateProfit = np.ndarray((di_size, ii_size), dtype=float)
        self.operateProfit.flat = np.nan
        self.ordinRiskReser = np.ndarray((di_size, ii_size), dtype=float)
        self.ordinRiskReser.flat = np.nan
        self.origContrCIndem = np.ndarray((di_size, ii_size), dtype=float)
        self.origContrCIndem.flat = np.nan
        self.othCA = np.ndarray((di_size, ii_size), dtype=float)
        self.othCA.flat = np.nan
        self.othCL = np.ndarray((di_size, ii_size), dtype=float)
        self.othCL.flat = np.nan
        self.othCompreIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.othCompreIncome.flat = np.nan
        self.othComprIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.othComprIncome.flat = np.nan
        self.othEquityInstr = np.ndarray((di_size, ii_size), dtype=float)
        self.othEquityInstr.flat = np.nan
        self.othNCA = np.ndarray((di_size, ii_size), dtype=float)
        self.othNCA.flat = np.nan
        self.othNCL = np.ndarray((di_size, ii_size), dtype=float)
        self.othNCL.flat = np.nan
        self.othPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.othPayable.flat = np.nan
        self.othReceiv = np.ndarray((di_size, ii_size), dtype=float)
        self.othReceiv.flat = np.nan
        self.paidInCapital = np.ndarray((di_size, ii_size), dtype=float)
        self.paidInCapital.flat = np.nan
        self.payrollPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.payrollPayable.flat = np.nan
        self.perpetualBondE = np.ndarray((di_size, ii_size), dtype=float)
        self.perpetualBondE.flat = np.nan
        self.perpetualBondL = np.ndarray((di_size, ii_size), dtype=float)
        self.perpetualBondL.flat = np.nan
        self.policyDivPayt = np.ndarray((di_size, ii_size), dtype=float)
        self.policyDivPayt.flat = np.nan
        self.preferredStockE = np.ndarray((di_size, ii_size), dtype=float)
        self.preferredStockE.flat = np.nan
        self.preferredStockL = np.ndarray((di_size, ii_size), dtype=float)
        self.preferredStockL.flat = np.nan
        self.premEarned = np.ndarray((di_size, ii_size), dtype=float)
        self.premEarned.flat = np.nan
        self.premFrOrigContr = np.ndarray((di_size, ii_size), dtype=float)
        self.premFrOrigContr.flat = np.nan
        self.premiumReceiv = np.ndarray((di_size, ii_size), dtype=float)
        self.premiumReceiv.flat = np.nan
        self.premRefund = np.ndarray((di_size, ii_size), dtype=float)
        self.premRefund.flat = np.nan
        self.prepayment = np.ndarray((di_size, ii_size), dtype=float)
        self.prepayment.flat = np.nan
        self.procSellInvest = np.ndarray((di_size, ii_size), dtype=float)
        self.procSellInvest.flat = np.nan
        self.producBiolAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.producBiolAssets.flat = np.nan
        self.purFixAssetsOth = np.ndarray((di_size, ii_size), dtype=float)
        self.purFixAssetsOth.flat = np.nan
        self.purResaleFa = np.ndarray((di_size, ii_size), dtype=float)
        self.purResaleFa.flat = np.nan
        self.RD = np.ndarray((di_size, ii_size), dtype=float)
        self.RD.flat = np.nan
        self.refundOfTax = np.ndarray((di_size, ii_size), dtype=float)
        self.refundOfTax.flat = np.nan
        self.reinsurExp = np.ndarray((di_size, ii_size), dtype=float)
        self.reinsurExp.flat = np.nan
        self.reinsurPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.reinsurPayable.flat = np.nan
        self.reinsurReceiv = np.ndarray((di_size, ii_size), dtype=float)
        self.reinsurReceiv.flat = np.nan
        self.reinsurReserReceiv = np.ndarray((di_size, ii_size), dtype=float)
        self.reinsurReserReceiv.flat = np.nan
        self.reserInsurContr = np.ndarray((di_size, ii_size), dtype=float)
        self.reserInsurContr.flat = np.nan
        self.retainedEarnings = np.ndarray((di_size, ii_size), dtype=float)
        self.retainedEarnings.flat = np.nan
        self.revenue = np.ndarray((di_size, ii_size), dtype=float)
        self.revenue.flat = np.nan
        self.sellExp = np.ndarray((di_size, ii_size), dtype=float)
        self.sellExp.flat = np.nan
        self.settProv = np.ndarray((di_size, ii_size), dtype=float)
        self.settProv.flat = np.nan
        self.soldForRepurFa = np.ndarray((di_size, ii_size), dtype=float)
        self.soldForRepurFa.flat = np.nan
        self.specialReser = np.ndarray((di_size, ii_size), dtype=float)
        self.specialReser.flat = np.nan
        self.specificPayables = np.ndarray((di_size, ii_size), dtype=float)
        self.specificPayables.flat = np.nan
        self.STBorr = np.ndarray((di_size, ii_size), dtype=float)
        self.STBorr.flat = np.nan
        self.surplusReser = np.ndarray((di_size, ii_size), dtype=float)
        self.surplusReser.flat = np.nan
        self.TAssets = np.ndarray((di_size, ii_size), dtype=float)
        self.TAssets.flat = np.nan
        self.taxesPayable = np.ndarray((di_size, ii_size), dtype=float)
        self.taxesPayable.flat = np.nan
        self.TCA = np.ndarray((di_size, ii_size), dtype=float)
        self.TCA.flat = np.nan
        self.TCL = np.ndarray((di_size, ii_size), dtype=float)
        self.TCL.flat = np.nan
        self.TCogs = np.ndarray((di_size, ii_size), dtype=float)
        self.TCogs.flat = np.nan
        self.TComprIncome = np.ndarray((di_size, ii_size), dtype=float)
        self.TComprIncome.flat = np.nan
        self.TEquityAttrP = np.ndarray((di_size, ii_size), dtype=float)
        self.TEquityAttrP.flat = np.nan
        self.TLiab = np.ndarray((di_size, ii_size), dtype=float)
        self.TLiab.flat = np.nan
        self.TLiabEquity = np.ndarray((di_size, ii_size), dtype=float)
        self.TLiabEquity.flat = np.nan
        self.TNCA = np.ndarray((di_size, ii_size), dtype=float)
        self.TNCA.flat = np.nan
        self.TNCL = np.ndarray((di_size, ii_size), dtype=float)
        self.TNCL.flat = np.nan
        self.TProfit = np.ndarray((di_size, ii_size), dtype=float)
        self.TProfit.flat = np.nan
        self.tradingFA = np.ndarray((di_size, ii_size), dtype=float)
        self.tradingFA.flat = np.nan
        self.tradingFL = np.ndarray((di_size, ii_size), dtype=float)
        self.tradingFL.flat = np.nan
        self.treasuryShare = np.ndarray((di_size, ii_size), dtype=float)
        self.treasuryShare.flat = np.nan
        self.tRevenue = np.ndarray((di_size, ii_size), dtype=float)
        self.tRevenue.flat = np.nan
        self.TShEquity = np.ndarray((di_size, ii_size), dtype=float)
        self.TShEquity.flat = np.nan

        self.register_data('adminExp', self.adminExp)
        self.register_data('advanceReceipts', self.advanceReceipts)
        self.register_data('AJInvestIncome', self.AJInvestIncome)
        self.register_data('AP', self.AP)
        self.register_data('AR', self.AR)
        self.register_data('assetsImpairLoss', self.assetsImpairLoss)
        self.register_data('availForSaleFa', self.availForSaleFa)
        self.register_data('basicEPS', self.basicEPS)
        self.register_data('bizTaxSurchg', self.bizTaxSurchg)
        self.register_data('bondPayable', self.bondPayable)
        self.register_data('capitalReser', self.capitalReser)
        self.register_data('cashCEquiv', self.cashCEquiv)
        self.register_data('CBBorr', self.CBBorr)
        self.register_data('CFrBorr', self.CFrBorr)
        self.register_data('CFrCapContr', self.CFrCapContr)
        self.register_data('CFrIssueBond', self.CFrIssueBond)
        self.register_data('CFrMinoSSubs', self.CFrMinoSSubs)
        self.register_data('CFrOthFinanA', self.CFrOthFinanA)
        self.register_data('CFrOthInvestA', self.CFrOthInvestA)
        self.register_data('CFrOthOperateA', self.CFrOthOperateA)
        self.register_data('CFrSaleGS', self.CFrSaleGS)
        self.register_data('CInfFrFinanA', self.CInfFrFinanA)
        self.register_data('CInfFrInvestA', self.CInfFrInvestA)
        self.register_data('CInfFrOperateA', self.CInfFrOperateA)
        self.register_data('CIP', self.CIP)
        self.register_data('COGS', self.COGS)
        self.register_data('commisExp', self.commisExp)
        self.register_data('commisIncome', self.commisIncome)
        self.register_data('commisPayable', self.commisPayable)
        self.register_data('comprIncAttrMS', self.comprIncAttrMS)
        self.register_data('comprIncAttrP', self.comprIncAttrP)
        self.register_data('constMaterials', self.constMaterials)
        self.register_data('COutfFrFinanA', self.COutfFrFinanA)
        self.register_data('COutfFrInvestA', self.COutfFrInvestA)
        self.register_data('COutfOperateA', self.COutfOperateA)
        self.register_data('CPaidDivProfInt', self.CPaidDivProfInt)
        self.register_data('CPaidForDebts', self.CPaidForDebts)
        self.register_data('CPaidForOthOpA', self.CPaidForOthOpA)
        self.register_data('CPaidForTaxes', self.CPaidForTaxes)
        self.register_data('CPaidGS', self.CPaidGS)
        self.register_data('CPaidIFC', self.CPaidIFC)
        self.register_data('CPaidInvest', self.CPaidInvest)
        self.register_data('CPaidOthFinanA', self.CPaidOthFinanA)
        self.register_data('CPaidOthInvestA', self.CPaidOthInvestA)
        self.register_data('CPaidPolDiv', self.CPaidPolDiv)
        self.register_data('CPaidToForEmpl', self.CPaidToForEmpl)
        self.register_data('deferTaxAssets', self.deferTaxAssets)
        self.register_data('deferTaxLiab', self.deferTaxLiab)
        self.register_data('depos', self.depos)
        self.register_data('dilutedEPS', self.dilutedEPS)
        self.register_data('disburLA', self.disburLA)
        self.register_data('dispFixAssetsOth', self.dispFixAssetsOth)
        self.register_data('divPayable', self.divPayable)
        self.register_data('divProfSubsMinoS', self.divProfSubsMinoS)
        self.register_data('divReceiv', self.divReceiv)
        self.register_data('estimatedLiab', self.estimatedLiab)
        self.register_data('finanExp', self.finanExp)
        self.register_data('fixedAssets', self.fixedAssets)
        self.register_data('fixedAssetsDisp', self.fixedAssetsDisp)
        self.register_data('forexDiffer', self.forexDiffer)
        self.register_data('forexEffects', self.forexEffects)
        self.register_data('forexGain', self.forexGain)
        self.register_data('fundsSecTradAgen', self.fundsSecTradAgen)
        self.register_data('fundsSecUndwAgen', self.fundsSecUndwAgen)
        self.register_data('fValueChgGain', self.fValueChgGain)
        self.register_data('gainInvest', self.gainInvest)
        self.register_data('goodwill', self.goodwill)
        self.register_data('htmInvest', self.htmInvest)
        self.register_data('IFCCashIncr', self.IFCCashIncr)
        self.register_data('incomeTax', self.incomeTax)
        self.register_data('insurReser', self.insurReser)
        self.register_data('intanAssets', self.intanAssets)
        self.register_data('intExp', self.intExp)
        self.register_data('intIncome', self.intIncome)
        self.register_data('intPayable', self.intPayable)
        self.register_data('intReceiv', self.intReceiv)
        self.register_data('inventories', self.inventories)
        self.register_data('investIncome', self.investIncome)
        self.register_data('investRealEstate', self.investRealEstate)
        self.register_data('loanFrOthBankFi', self.loanFrOthBankFi)
        self.register_data('loanToOthBankFi', self.loanToOthBankFi)
        self.register_data('LTAmorExp', self.LTAmorExp)
        self.register_data('LTBorr', self.LTBorr)
        self.register_data('LTEquityInvest', self.LTEquityInvest)
        self.register_data('LTPayable', self.LTPayable)
        self.register_data('LTReceive', self.LTReceive)
        self.register_data('minorityGain', self.minorityGain)
        self.register_data('minorityInt', self.minorityInt)
        self.register_data('NCADisploss', self.NCADisploss)
        self.register_data('NCApIncrRepur', self.NCApIncrRepur)
        self.register_data('NCAWithin1Y', self.NCAWithin1Y)
        self.register_data('NCEBegBal', self.NCEBegBal)
        self.register_data('NCEEndBal', self.NCEEndBal)
        self.register_data('NCFFrFinanA', self.NCFFrFinanA)
        self.register_data('NCFFrInvestA', self.NCFFrInvestA)
        self.register_data('NCFOperateA', self.NCFOperateA)
        self.register_data('NChangeInCash', self.NChangeInCash)
        self.register_data('NCLWithin1Y', self.NCLWithin1Y)
        self.register_data('NCompensPayout', self.NCompensPayout)
        self.register_data('NCPaidAcquis', self.NCPaidAcquis)
        self.register_data('NDeposIncrCFI', self.NDeposIncrCFI)
        self.register_data('NDispSubsOthBizC', self.NDispSubsOthBizC)
        self.register_data('NIncBorrOthFI', self.NIncBorrOthFI)
        self.register_data('NIncDisburOfLA', self.NIncDisburOfLA)
        self.register_data('NIncDispTradFA', self.NIncDispTradFA)
        self.register_data('NIncFrBorr', self.NIncFrBorr)
        self.register_data('NIncome', self.NIncome)
        self.register_data('NIncomeAttrP', self.NIncomeAttrP)
        self.register_data('NIncPhDeposInv', self.NIncPhDeposInv)
        self.register_data('NIncrBorrFrCB', self.NIncrBorrFrCB)
        self.register_data('NIncrDeposInFI', self.NIncrDeposInFI)
        self.register_data('NIncrPledgeLoan', self.NIncrPledgeLoan)
        self.register_data('NoperateExp', self.NoperateExp)
        self.register_data('NoperateIncome', self.NoperateIncome)
        self.register_data('NotesPayable', self.NotesPayable)
        self.register_data('NotesReceiv', self.NotesReceiv)
        self.register_data('NReinsurPrem', self.NReinsurPrem)
        self.register_data('oilAndGasAssets', self.oilAndGasAssets)
        self.register_data('operateProfit', self.operateProfit)
        self.register_data('ordinRiskReser', self.ordinRiskReser)
        self.register_data('origContrCIndem', self.origContrCIndem)
        self.register_data('othCA', self.othCA)
        self.register_data('othCL', self.othCL)
        self.register_data('othCompreIncome', self.othCompreIncome)
        self.register_data('othComprIncome', self.othComprIncome)
        self.register_data('othEquityInstr', self.othEquityInstr)
        self.register_data('othNCA', self.othNCA)
        self.register_data('othNCL', self.othNCL)
        self.register_data('othPayable', self.othPayable)
        self.register_data('othReceiv', self.othReceiv)
        self.register_data('paidInCapital', self.paidInCapital)
        self.register_data('payrollPayable', self.payrollPayable)
        self.register_data('perpetualBondE', self.perpetualBondE)
        self.register_data('perpetualBondL', self.perpetualBondL)
        self.register_data('policyDivPayt', self.policyDivPayt)
        self.register_data('preferredStockE', self.preferredStockE)
        self.register_data('preferredStockL', self.preferredStockL)
        self.register_data('premEarned', self.premEarned)
        self.register_data('premFrOrigContr', self.premFrOrigContr)
        self.register_data('premiumReceiv', self.premiumReceiv)
        self.register_data('premRefund', self.premRefund)
        self.register_data('prepayment', self.prepayment)
        self.register_data('procSellInvest', self.procSellInvest)
        self.register_data('producBiolAssets', self.producBiolAssets)
        self.register_data('purFixAssetsOth', self.purFixAssetsOth)
        self.register_data('purResaleFa', self.purResaleFa)
        self.register_data('RD', self.RD)
        self.register_data('refundOfTax', self.refundOfTax)
        self.register_data('reinsurExp', self.reinsurExp)
        self.register_data('reinsurPayable', self.reinsurPayable)
        self.register_data('reinsurReceiv', self.reinsurReceiv)
        self.register_data('reinsurReserReceiv', self.reinsurReserReceiv)
        self.register_data('reserInsurContr', self.reserInsurContr)
        self.register_data('retainedEarnings', self.retainedEarnings)
        self.register_data('revenue', self.revenue)
        self.register_data('sellExp', self.sellExp)
        self.register_data('settProv', self.settProv)
        self.register_data('soldForRepurFa', self.soldForRepurFa)
        self.register_data('specialReser', self.specialReser)
        self.register_data('specificPayables', self.specificPayables)
        self.register_data('STBorr', self.STBorr)
        self.register_data('surplusReser', self.surplusReser)
        self.register_data('TAssets', self.TAssets)
        self.register_data('taxesPayable', self.taxesPayable)
        self.register_data('TCA', self.TCA)
        self.register_data('TCL', self.TCL)
        self.register_data('TCogs', self.TCogs)
        self.register_data('TComprIncome', self.TComprIncome)
        self.register_data('TEquityAttrP', self.TEquityAttrP)
        self.register_data('TLiab', self.TLiab)
        self.register_data('TLiabEquity', self.TLiabEquity)
        self.register_data('TNCA', self.TNCA)
        self.register_data('TNCL', self.TNCL)
        self.register_data('TProfit', self.TProfit)
        self.register_data('tradingFA', self.tradingFA)
        self.register_data('tradingFL', self.tradingFL)
        self.register_data('treasuryShare', self.treasuryShare)
        self.register_data('tRevenue', self.tRevenue)
        self.register_data('TShEquity', self.TShEquity)

    def compute_day(self, di):
        pass

    def dependencies(self):
        # Do not need dependencies in DataManagerBaseData
        pass

    def caches(self):
        self.register_cache('adminExp')
        self.register_cache('advanceReceipts')
        self.register_cache('AJInvestIncome')
        self.register_cache('AP')
        self.register_cache('AR')
        self.register_cache('assetsImpairLoss')
        self.register_cache('availForSaleFa')
        self.register_cache('basicEPS')
        self.register_cache('bizTaxSurchg')
        self.register_cache('bondPayable')
        self.register_cache('capitalReser')
        self.register_cache('cashCEquiv')
        self.register_cache('CBBorr')
        self.register_cache('CFrBorr')
        self.register_cache('CFrCapContr')
        self.register_cache('CFrIssueBond')
        self.register_cache('CFrMinoSSubs')
        self.register_cache('CFrOthFinanA')
        self.register_cache('CFrOthInvestA')
        self.register_cache('CFrOthOperateA')
        self.register_cache('CFrSaleGS')
        self.register_cache('CInfFrFinanA')
        self.register_cache('CInfFrInvestA')
        self.register_cache('CInfFrOperateA')
        self.register_cache('CIP')
        self.register_cache('COGS')
        self.register_cache('commisExp')
        self.register_cache('commisIncome')
        self.register_cache('commisPayable')
        self.register_cache('comprIncAttrMS')
        self.register_cache('comprIncAttrP')
        self.register_cache('constMaterials')
        self.register_cache('COutfFrFinanA')
        self.register_cache('COutfFrInvestA')
        self.register_cache('COutfOperateA')
        self.register_cache('CPaidDivProfInt')
        self.register_cache('CPaidForDebts')
        self.register_cache('CPaidForOthOpA')
        self.register_cache('CPaidForTaxes')
        self.register_cache('CPaidGS')
        self.register_cache('CPaidIFC')
        self.register_cache('CPaidInvest')
        self.register_cache('CPaidOthFinanA')
        self.register_cache('CPaidOthInvestA')
        self.register_cache('CPaidPolDiv')
        self.register_cache('CPaidToForEmpl')
        self.register_cache('deferTaxAssets')
        self.register_cache('deferTaxLiab')
        self.register_cache('depos')
        self.register_cache('dilutedEPS')
        self.register_cache('disburLA')
        self.register_cache('dispFixAssetsOth')
        self.register_cache('divPayable')
        self.register_cache('divProfSubsMinoS')
        self.register_cache('divReceiv')
        self.register_cache('estimatedLiab')
        self.register_cache('finanExp')
        self.register_cache('fixedAssets')
        self.register_cache('fixedAssetsDisp')
        self.register_cache('forexDiffer')
        self.register_cache('forexEffects')
        self.register_cache('forexGain')
        self.register_cache('fundsSecTradAgen')
        self.register_cache('fundsSecUndwAgen')
        self.register_cache('fValueChgGain')
        self.register_cache('gainInvest')
        self.register_cache('goodwill')
        self.register_cache('htmInvest')
        self.register_cache('IFCCashIncr')
        self.register_cache('incomeTax')
        self.register_cache('insurReser')
        self.register_cache('intanAssets')
        self.register_cache('intExp')
        self.register_cache('intIncome')
        self.register_cache('intPayable')
        self.register_cache('intReceiv')
        self.register_cache('inventories')
        self.register_cache('investIncome')
        self.register_cache('investRealEstate')
        self.register_cache('loanFrOthBankFi')
        self.register_cache('loanToOthBankFi')
        self.register_cache('LTAmorExp')
        self.register_cache('LTBorr')
        self.register_cache('LTEquityInvest')
        self.register_cache('LTPayable')
        self.register_cache('LTReceive')
        self.register_cache('minorityGain')
        self.register_cache('minorityInt')
        self.register_cache('NCADisploss')
        self.register_cache('NCApIncrRepur')
        self.register_cache('NCAWithin1Y')
        self.register_cache('NCEBegBal')
        self.register_cache('NCEEndBal')
        self.register_cache('NCFFrFinanA')
        self.register_cache('NCFFrInvestA')
        self.register_cache('NCFOperateA')
        self.register_cache('NChangeInCash')
        self.register_cache('NCLWithin1Y')
        self.register_cache('NCompensPayout')
        self.register_cache('NCPaidAcquis')
        self.register_cache('NDeposIncrCFI')
        self.register_cache('NDispSubsOthBizC')
        self.register_cache('NIncBorrOthFI')
        self.register_cache('NIncDisburOfLA')
        self.register_cache('NIncDispTradFA')
        self.register_cache('NIncFrBorr')
        self.register_cache('NIncome')
        self.register_cache('NIncomeAttrP')
        self.register_cache('NIncPhDeposInv')
        self.register_cache('NIncrBorrFrCB')
        self.register_cache('NIncrDeposInFI')
        self.register_cache('NIncrPledgeLoan')
        self.register_cache('NoperateExp')
        self.register_cache('NoperateIncome')
        self.register_cache('NotesPayable')
        self.register_cache('NotesReceiv')
        self.register_cache('NReinsurPrem')
        self.register_cache('oilAndGasAssets')
        self.register_cache('operateProfit')
        self.register_cache('ordinRiskReser')
        self.register_cache('origContrCIndem')
        self.register_cache('othCA')
        self.register_cache('othCL')
        self.register_cache('othCompreIncome')
        self.register_cache('othComprIncome')
        self.register_cache('othEquityInstr')
        self.register_cache('othNCA')
        self.register_cache('othNCL')
        self.register_cache('othPayable')
        self.register_cache('othReceiv')
        self.register_cache('paidInCapital')
        self.register_cache('payrollPayable')
        self.register_cache('perpetualBondE')
        self.register_cache('perpetualBondL')
        self.register_cache('policyDivPayt')
        self.register_cache('preferredStockE')
        self.register_cache('preferredStockL')
        self.register_cache('premEarned')
        self.register_cache('premFrOrigContr')
        self.register_cache('premiumReceiv')
        self.register_cache('premRefund')
        self.register_cache('prepayment')
        self.register_cache('procSellInvest')
        self.register_cache('producBiolAssets')
        self.register_cache('purFixAssetsOth')
        self.register_cache('purResaleFa')
        self.register_cache('RD')
        self.register_cache('refundOfTax')
        self.register_cache('reinsurExp')
        self.register_cache('reinsurPayable')
        self.register_cache('reinsurReceiv')
        self.register_cache('reinsurReserReceiv')
        self.register_cache('reserInsurContr')
        self.register_cache('retainedEarnings')
        self.register_cache('revenue')
        self.register_cache('sellExp')
        self.register_cache('settProv')
        self.register_cache('soldForRepurFa')
        self.register_cache('specialReser')
        self.register_cache('specificPayables')
        self.register_cache('STBorr')
        self.register_cache('surplusReser')
        self.register_cache('TAssets')
        self.register_cache('taxesPayable')
        self.register_cache('TCA')
        self.register_cache('TCL')
        self.register_cache('TCogs')
        self.register_cache('TComprIncome')
        self.register_cache('TEquityAttrP')
        self.register_cache('TLiab')
        self.register_cache('TLiabEquity')
        self.register_cache('TNCA')
        self.register_cache('TNCL')
        self.register_cache('TProfit')
        self.register_cache('tradingFA')
        self.register_cache('tradingFL')
        self.register_cache('treasuryShare')
        self.register_cache('tRevenue')
        self.register_cache('TShEquity')

    def freshes(self):
        self.register_fresh('adminExp')
        self.register_fresh('advanceReceipts')
        self.register_fresh('AJInvestIncome')
        self.register_fresh('AP')
        self.register_fresh('AR')
        self.register_fresh('assetsImpairLoss')
        self.register_fresh('availForSaleFa')
        self.register_fresh('basicEPS')
        self.register_fresh('bizTaxSurchg')
        self.register_fresh('bondPayable')
        self.register_fresh('capitalReser')
        self.register_fresh('cashCEquiv')
        self.register_fresh('CBBorr')
        self.register_fresh('CFrBorr')
        self.register_fresh('CFrCapContr')
        self.register_fresh('CFrIssueBond')
        self.register_fresh('CFrMinoSSubs')
        self.register_fresh('CFrOthFinanA')
        self.register_fresh('CFrOthInvestA')
        self.register_fresh('CFrOthOperateA')
        self.register_fresh('CFrSaleGS')
        self.register_fresh('CInfFrFinanA')
        self.register_fresh('CInfFrInvestA')
        self.register_fresh('CInfFrOperateA')
        self.register_fresh('CIP')
        self.register_fresh('COGS')
        self.register_fresh('commisExp')
        self.register_fresh('commisIncome')
        self.register_fresh('commisPayable')
        self.register_fresh('comprIncAttrMS')
        self.register_fresh('comprIncAttrP')
        self.register_fresh('constMaterials')
        self.register_fresh('COutfFrFinanA')
        self.register_fresh('COutfFrInvestA')
        self.register_fresh('COutfOperateA')
        self.register_fresh('CPaidDivProfInt')
        self.register_fresh('CPaidForDebts')
        self.register_fresh('CPaidForOthOpA')
        self.register_fresh('CPaidForTaxes')
        self.register_fresh('CPaidGS')
        self.register_fresh('CPaidIFC')
        self.register_fresh('CPaidInvest')
        self.register_fresh('CPaidOthFinanA')
        self.register_fresh('CPaidOthInvestA')
        self.register_fresh('CPaidPolDiv')
        self.register_fresh('CPaidToForEmpl')
        self.register_fresh('deferTaxAssets')
        self.register_fresh('deferTaxLiab')
        self.register_fresh('depos')
        self.register_fresh('dilutedEPS')
        self.register_fresh('disburLA')
        self.register_fresh('dispFixAssetsOth')
        self.register_fresh('divPayable')
        self.register_fresh('divProfSubsMinoS')
        self.register_fresh('divReceiv')
        self.register_fresh('estimatedLiab')
        self.register_fresh('finanExp')
        self.register_fresh('fixedAssets')
        self.register_fresh('fixedAssetsDisp')
        self.register_fresh('forexDiffer')
        self.register_fresh('forexEffects')
        self.register_fresh('forexGain')
        self.register_fresh('fundsSecTradAgen')
        self.register_fresh('fundsSecUndwAgen')
        self.register_fresh('fValueChgGain')
        self.register_fresh('gainInvest')
        self.register_fresh('goodwill')
        self.register_fresh('htmInvest')
        self.register_fresh('IFCCashIncr')
        self.register_fresh('incomeTax')
        self.register_fresh('insurReser')
        self.register_fresh('intanAssets')
        self.register_fresh('intExp')
        self.register_fresh('intIncome')
        self.register_fresh('intPayable')
        self.register_fresh('intReceiv')
        self.register_fresh('inventories')
        self.register_fresh('investIncome')
        self.register_fresh('investRealEstate')
        self.register_fresh('loanFrOthBankFi')
        self.register_fresh('loanToOthBankFi')
        self.register_fresh('LTAmorExp')
        self.register_fresh('LTBorr')
        self.register_fresh('LTEquityInvest')
        self.register_fresh('LTPayable')
        self.register_fresh('LTReceive')
        self.register_fresh('minorityGain')
        self.register_fresh('minorityInt')
        self.register_fresh('NCADisploss')
        self.register_fresh('NCApIncrRepur')
        self.register_fresh('NCAWithin1Y')
        self.register_fresh('NCEBegBal')
        self.register_fresh('NCEEndBal')
        self.register_fresh('NCFFrFinanA')
        self.register_fresh('NCFFrInvestA')
        self.register_fresh('NCFOperateA')
        self.register_fresh('NChangeInCash')
        self.register_fresh('NCLWithin1Y')
        self.register_fresh('NCompensPayout')
        self.register_fresh('NCPaidAcquis')
        self.register_fresh('NDeposIncrCFI')
        self.register_fresh('NDispSubsOthBizC')
        self.register_fresh('NIncBorrOthFI')
        self.register_fresh('NIncDisburOfLA')
        self.register_fresh('NIncDispTradFA')
        self.register_fresh('NIncFrBorr')
        self.register_fresh('NIncome')
        self.register_fresh('NIncomeAttrP')
        self.register_fresh('NIncPhDeposInv')
        self.register_fresh('NIncrBorrFrCB')
        self.register_fresh('NIncrDeposInFI')
        self.register_fresh('NIncrPledgeLoan')
        self.register_fresh('NoperateExp')
        self.register_fresh('NoperateIncome')
        self.register_fresh('NotesPayable')
        self.register_fresh('NotesReceiv')
        self.register_fresh('NReinsurPrem')
        self.register_fresh('oilAndGasAssets')
        self.register_fresh('operateProfit')
        self.register_fresh('ordinRiskReser')
        self.register_fresh('origContrCIndem')
        self.register_fresh('othCA')
        self.register_fresh('othCL')
        self.register_fresh('othCompreIncome')
        self.register_fresh('othComprIncome')
        self.register_fresh('othEquityInstr')
        self.register_fresh('othNCA')
        self.register_fresh('othNCL')
        self.register_fresh('othPayable')
        self.register_fresh('othReceiv')
        self.register_fresh('paidInCapital')
        self.register_fresh('payrollPayable')
        self.register_fresh('perpetualBondE')
        self.register_fresh('perpetualBondL')
        self.register_fresh('policyDivPayt')
        self.register_fresh('preferredStockE')
        self.register_fresh('preferredStockL')
        self.register_fresh('premEarned')
        self.register_fresh('premFrOrigContr')
        self.register_fresh('premiumReceiv')
        self.register_fresh('premRefund')
        self.register_fresh('prepayment')
        self.register_fresh('procSellInvest')
        self.register_fresh('producBiolAssets')
        self.register_fresh('purFixAssetsOth')
        self.register_fresh('purResaleFa')
        self.register_fresh('RD')
        self.register_fresh('refundOfTax')
        self.register_fresh('reinsurExp')
        self.register_fresh('reinsurPayable')
        self.register_fresh('reinsurReceiv')
        self.register_fresh('reinsurReserReceiv')
        self.register_fresh('reserInsurContr')
        self.register_fresh('retainedEarnings')
        self.register_fresh('revenue')
        self.register_fresh('sellExp')
        self.register_fresh('settProv')
        self.register_fresh('soldForRepurFa')
        self.register_fresh('specialReser')
        self.register_fresh('specificPayables')
        self.register_fresh('STBorr')
        self.register_fresh('surplusReser')
        self.register_fresh('TAssets')
        self.register_fresh('taxesPayable')
        self.register_fresh('TCA')
        self.register_fresh('TCL')
        self.register_fresh('TCogs')
        self.register_fresh('TComprIncome')
        self.register_fresh('TEquityAttrP')
        self.register_fresh('TLiab')
        self.register_fresh('TLiabEquity')
        self.register_fresh('TNCA')
        self.register_fresh('TNCL')
        self.register_fresh('TProfit')
        self.register_fresh('tradingFA')
        self.register_fresh('tradingFL')
        self.register_fresh('treasuryShare')
        self.register_fresh('tRevenue')
        self.register_fresh('TShEquity')
