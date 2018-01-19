import numpy as np
from pipeline.module import DailyLoopModule
import math, pickle, os

TRADE_DAYS = 242
PATH = '/Users/zhaozibo/Zalpha/zalpha'

class Performance(DailyLoopModule):

    def initialize(self):
        self.alpha = self.context.alpha
        self.long_capital = self.params['longcapital']
        self.short_capital = self.params['shortcapital']
        self.adj_cps = self.context.fetch_data('adj_close')
        self.adj_vwap = self.context.fetch_data('adj_vwap')
        self.start_di = self.context.start_di
        self.end_di = self.context.end_di
        self.di_size = len(self.context.di_list) + 1
        self.ii_size = len(self.context.ii_list)
        self.shares = np.zeros((self.di_size, self.ii_size))
        self.position = np.zeros((self.di_size, self.ii_size))
        self.cumpnl = 0
        self.cumtvr = 0
        self.cumcapital = 0
        self.count = 0
        self.r_sum = 0
        self.r2_sum = 0
        self.alphaId = self.params['alpha_id']
        self.alphaMap = {}
        # self.mode = self.params['mode']

    def start_day(self, di):
        pass

    def intro_day(self, di):
        pass

    def end_day(self, di):
        if di > self.end_di or di < self.start_di:
            raise Exception('date error: beyond simulation date range!!!')

        if di == self.end_di:
            self.alphaMap['0'] = self.alpha.copy() 
            with open(PATH + '/log/' + self.alphaId, 'wb') as output:
                pickle.dump(self.alphaMap, output)
            return
        date = self.context.di_list[di]
        self.alphaMap[date] = self.alpha.copy()

        #self.count += 1
        long_num = np.sum(self.alpha > 1e-5)
        if long_num > 0:
            long_sum = np.sum(self.alpha[self.alpha > 1e-5])
            self.position[di][self.alpha > 1e-5] = float(self.long_capital) * self.alpha[self.alpha > 1e-5] / long_sum

        short_num = np.sum(self.alpha < -1e-5)
        if short_num > 0:
            short_sum = np.sum(self.alpha[self.alpha < -1e-5])
            self.position[di][self.alpha < -1e-5] = -float(self.short_capital) * self.alpha[self.alpha < -1e-5] / short_sum

        tmp = np.where(~np.isnan(self.adj_cps[di - 1]))[0]
        #self.shares[di][tmp] = np.round(tposition[tmp] / self.adj_cps[di - 1][tmp])
        self.shares[di][tmp] = self.position[di][tmp] / self.adj_cps[di - 1][tmp]

        total_shares = np.sum(np.absolute(self.shares[di]))
        long_num = np.sum(self.shares[di] > 1e-5)
        short_num = np.sum(self.shares[di] < -1e-5)

        #self.position[di][tmp] = self.shares[di][tmp] * self.adj_cps[di-1][tmp]

        tvr = np.sum(np.absolute(self.position[di] - self.position[di-1]))
        self.cumtvr += tvr

        l_capital = np.sum(self.position[di][self.position[di] > 1e-5])
        s_capital = -np.sum(self.position[di][self.position[di] < -1e-5])
        if l_capital > 1 or s_capital > 1:
            self.count += 1
            self.cumcapital += l_capital + s_capital

            holding_pnl = np.nansum(self.shares[di-1] * (self.adj_cps[di] - self.adj_cps[di-1]))
            trading_pnl = np.nansum((self.shares[di] - self.shares[di-1]) * (self.adj_cps[di] - self.adj_vwap[di]))
            pnl = holding_pnl + trading_pnl
            self.cumpnl += pnl

            if l_capital > 1:
                ret = pnl / l_capital
            else:
                ret = pnl / s_capital
            if self.count == 1:
                self.T = ret
                self.Vmin = ret
                self.Tmax = max(0, self.T)
            else:
                self.T += ret
                if self.T - self.Tmax < self.Vmin:
                    self.Vmin = self.T - self.Tmax
                if self.T > self.Tmax:
                    self.Tmax = self.T

            self.r_sum += ret
            self.r2_sum += ret * ret
        else:
            ret = 0
            pnl = 0
        IR = 0
        if self.count > 2:
            avg = self.r_sum / self.count
            std = math.sqrt((self.r2_sum - self.r_sum * self.r_sum / self.count) / (self.count - 1))
            if std > 0:
                IR = avg /std
        
        print("%81s X %7s %10s %15s %25s %7s %7s %7s %7s" % ("LONG", "SHORT", "SHARES", "PNL", "CUMPNL", "TVR", "RET", "DD", "IR"))
        if not self.count == 0:
            print("%8s %30s %15d X %15d %7d X %7d %10d %15d %25d %7.3f %7.3f %7.3f %7.3f" % (date, self.alphaId, int(l_capital), -int(s_capital), int(long_num), int(short_num), int(total_shares), int(pnl), int(self.cumpnl), self.cumtvr / self.cumcapital, self.r_sum / self.count * TRADE_DAYS, min(0, self.Vmin) ,IR))
        else:
            print("%8s %30s %15d X %15d %7d X %7d %10d %15d %25d %7.3f %7.3f %7.3f %7.3f" % (date, self.alphaId, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            
        if di == self.start_di and os.path.isfile(PATH + '/pnl/' + self.alphaId + '.csv'):
            os.remove(PATH + '/pnl/' + self.alphaId + '.csv')
        with open(PATH + '/pnl/' + self.alphaId + '.csv', 'a') as output:
            output.write("%8s %15f %15f %15f %15f %15f\n" % (date, pnl, ret, tvr, l_capital, s_capital))

    def dependencies(self):
        self.register_dependency('adj_close')
        self.register_dependency('adj_vwap')


"""
Alpha based functions should return in the form of
{
    'type': 'alpha_based',
    'pnl': xxx,
    'long_capital': xxx,
    'short_capital': xxx,
    'long_num': xxx,
    'short_num': xxx,
    'tvr': xxx
}
di: date index
alpha: alpha values for each stock on di
is_long: True for long and False for short
capital: capitals to be positioned
context: prices data for calculating positions
history_position: capital position for each stock in history
start_di: di of the start date of backtest
end_di: di of the last date of backtest
threhold: only deal with the top n stocks
"""
