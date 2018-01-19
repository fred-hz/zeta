from operation.operation_base import OperationBase
import util
import numpy as np


class OperationHump(OperationBase):
    def initialize(self):
        self.topN = int(self.params['topN'])
        self.threshold = int(self.params['threshold'])
        if 'equal' not in self.params:
            self.equal = True
        else:
            self.equal = ('True' == self.params['equal'])
        self.ii_size = len(self.context.ii_list)
        self.mark = True
        self.old_topN = np.zeros(self.topN, dtype=int)

    def compute_day(self, di, alpha):
        # Should return alpha as a list
        new_alpha = np.zeros(self.ii_size)
        if self.mark:
            self.mark = False
            self.old_topN = np.argpartition(-alpha, self.topN)[:self.topN]
            if self.equal:
                new_alpha[self.old_topN] = 1.
            else:
                new_alpha[self.old_topN] = alpha[self.old_topN]
        else:
            new_thre = np.argpartition(-alpha, self.threshold)[:self.threshold]
            part1 = np.intersect1d(self.old_topN, new_thre)
            diff = self.topN - part1.size
            if not diff == 0:
                temp = alpha.copy()
                temp[part1] = np.min(alpha)-1.
                part1 = np.hstack((part1, np.argpartition(-temp, diff)[:diff]))
            if self.equal:
                new_alpha[part1] = 1.
            else:
                new_alpha[part1] = alpha[part1]
        alpha[:] = new_alpha[:]
        return alpha
