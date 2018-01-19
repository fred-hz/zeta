from operation.operation_base import OperationBase
import numpy as np


class OperationDecay(OperationBase):
    def initialize(self):
        self.days = int(self.params['days'])
        if 'dense' not in self.params:
            self.dense = True
        else:
            self.dense = ('True' == self.params['dense'])
        self.is_valid = self.context.is_valid  # need to revise
        self.ii_size = len(self.context.ii_list)
        self.hist = np.zeros((self.days, self.ii_size))
        self.hist.flat = np.nan
        self.num = np.zeros(self.ii_size, dtype=int)
        self.sum = np.zeros(self.ii_size)
        self.sum.flat = np.nan
        self.diff = np.zeros(self.ii_size)
        self.diff.flat = np.nan

    def compute_day(self, di, alpha):
        # Should return alpha as a list
        self.sum -= self.diff
        tmp = np.where(self.num == self.days)
        self.diff[tmp] -= self.hist[self.days - 1][tmp] / float(self.days)
        self.num[tmp] -= 1
        self.hist = np.vstack((alpha, self.hist[:-1]))

        tmp = ~np.isnan(self.hist[0])
        tmp_zero = np.where(self.num == 0 & ~np.isnan(self.hist[0]))
        self.sum[tmp_zero] = 0
        self.diff[tmp_zero] = 0
        self.num[tmp] += 1
        self.sum[tmp] += self.hist[0][tmp]
        self.diff[tmp] += self.hist[0][tmp] / float(self.days)

        tmp_nan = np.isnan(self.hist[0])
        if not self.dense:
            tmp = np.where(self.num > 0 & self.is_valid[di] == 1 & np.isnan(self.hist[0]))
            self.num[tmp] += 1
            self.hist[0][tmp] = 0
        else:
            self.num[tmp_nan] = 0
            self.sum[tmp_nan] = np.nan
            self.diff[tmp_nan] = np.nan

        alpha[:] = self.sum[:]

        if self.dense:
            denom = (2 * self.days - self.num) * (self.num + 1) / 2 / self.days
            tmp = (denom > 0)
            alpha[tmp] = alpha[tmp] / denom[tmp]
        return alpha
