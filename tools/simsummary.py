import os, sys, re, math, getopt
import numpy as np

def doStats(XX, date, pnl, ret, tvr, long, short):
    if XX not in stats:
        stats[XX] = {}
        stats[XX]['dates'] = []
        stats[XX]['pnl'] = 0
        stats[XX]['tvr'] = 0
        stats[XX]['long'] = 0
        stats[XX]['short'] = 0
        stats[XX]['avg_ret'] = 0
        stats[XX]['drawdown'] = 0
        stats[XX]['dd_start'] = 0
        stats[XX]['dd_end'] = 0
        stats[XX]['up_days'] = 0
        stats[XX]['days'] = 0
        stats[XX]['xsy'] = 0
        stats[XX]['xsyy'] = 0

    stats[XX]['dates'].append(date)
    stats[XX]['pnl'] += pnl
    stats[XX]['tvr'] += tvr
    stats[XX]['long'] += long
    stats[XX]['short'] += short
    stats[XX]['avg_ret'] += ret
    stats[XX]['xsy'] += ret
    stats[XX]['xsyy'] += ret * ret
    if pnl > 0:
        stats[XX]['up_days'] += 1
    if not long == 0 or not short == 0:
        stats[XX]['days'] += 1

LONGSHORT_SCALE = 1e6
PNL_SCALE = 1e6
TRADE_DAYS = 242

DD_start = 0
DD_setst = 0
DD_sum = 0
stats = {}

pnlfile = ''
pnlname = ''
type = 'yearly'
sdate = -1
edate = -1
pattern = re.compile(r'\s+')

try:
    opts, args = getopt.getopt(sys.argv[1:], "s:e:p:t:", ["sdate=", "edate=", "pnl=", "type="])
    for o, a in opts:
        if o in ("-s", "--sdate"):
            sdate = int(a)
        elif o in ("-e", "--edate"):
            edate = int(a)
        elif o in ("-p", "--pnl"):
            pnlname = a
            pnlfile = os.path.abspath(a)
        elif o in ("-t", "--type"):
            type = a
    if pnlfile == "":
        pnlname = args[0]
        pnlfile = os.path.abspath(args[0])
except getopt.GetoptError as err:
    print(sring(err))
    sys.exit(0)

if os.path.isfile(pnlfile) == False:
    print("Pnl file '%s' no exists" % pnlfile)
    sys.exit(0)

with open(pnlfile, 'r') as fp:
    cont = fp.read().splitlines()
for line in cont:
    items = line.split()
    date = int(items[0])
    pnl = float(items[1])
    ret = float(items[2])
    if np.isnan(ret):
        continue
    tvr = float(items[3])
    long = float(items[4])
    short = float(items[5])
    if (sdate > 0 and date < sdate) or (edate > 0 and date > edate):
        continue
    XX = items[0][:4]
    if type == 'monthly':
        XX = items[0][:6]
    doStats(XX, date, pnl, ret, tvr, long, short)
    doStats('ALL', date, pnl, ret, tvr, long, short)

    if DD_setst == 1:
        DD_start = date
        DD_setst = 0
    DD_sum += pnl
    if DD_sum >= 0:
        DD_sum = 0
        DD_start = date
        DD_setst = 1

    if DD_sum < stats[XX]['drawdown']:
        stats[XX]['drawdown'] = DD_sum
        stats[XX]['dd_start'] = DD_start
        stats[XX]['dd_end'] = date

    if DD_sum < stats['ALL']['drawdown']:
        stats['ALL']['drawdown'] = DD_sum
        stats['ALL']['dd_start'] = DD_start
        stats['ALL']['dd_end'] = date

print("%44s" % ('simsummary_' + pnlname))
print("%17s %7s %8s %7s %7s %7s %12s %5s %5s %7s" % ("dates", "long(M)", "short(M)", "pnl(M)", "%ret", "%tvr", "shrp(IR)", "%dd", "%win", "fitness"))

for XX in sorted(stats):
    if XX == 'ALL':
        print('')
    d = float(stats[XX]['days'])
    if d < 1:
        continue
    long = stats[XX]['long'] / d
    short = stats[XX]['short'] / d
    ret = stats[XX]['avg_ret'] / d * TRADE_DAYS
    perwin = stats[XX]['up_days'] / d
    turnover = stats[XX]['tvr'] / (stats[XX]['long'] + stats[XX]['short'])
    drawdown = stats[XX]['drawdown'] / long * -100 if long > 0 else 0
    ir = 0
    if d > 2:
        avg = stats[XX]['xsy'] / d
        std = math.sqrt((stats[XX]['xsyy'] - stats[XX]['xsy'] * stats[XX]['xsy'] / d) / (d-1))
        ir = avg / std if std > 0 else 0
    fitness = ir * math.sqrt(TRADE_DAYS) * math.sqrt(math.fabs(ret/turnover)) if turnover > 0 else 0
    print("%8d-%8d %7.2f %8.2f %7.3f %7.2f %7.2f %6.2f(%4.2f) %5.2f %5.2f %7.2f" % (stats[XX]['dates'][0], stats[XX]['dates'][-1], long / LONGSHORT_SCALE, short / LONGSHORT_SCALE, stats[XX]['pnl'] / PNL_SCALE, ret * 100, turnover * 100, ir * math.sqrt(TRADE_DAYS), ir, drawdown, perwin, fitness))
