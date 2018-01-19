import numpy as np
import pickle, os

with open('config_context.xml', 'r') as fp:
    cfg_context = fp.read().splitlines()

#names = os.listdir('data/cache/FdmtIndi')
#names = names[1:]
with open('FdmtIndi_good_result.txt', 'r') as fp:
    names = fp.read().splitlines()
alpha_modules = []
case_modules = {}

for name in names:
    alpha_modules.append('\t\t<Module id="AlphaFdmtIndi_'+name+'" class="alpha.alpha_FdmtIndi_'+name+'.AlphaFdmtIndi_'+name+'"/>')
    temp = []
    temp.append('\t\t<Case id="alpha_FdmtIndi_'+name+'_TOP2000" delay="1" method="1" ndays="5">')
    temp.append('\t\t\t<Universe moduleId="TOP2000"/>')
    temp.append('\t\t\t<Alpha moduleId="AlphaFdmtIndi_'+name+'"/>')
    temp.append('\t\t\t<Operations>')
    temp.append('\t\t\t\t<Operation moduleId="AlphaOpPower" exp="1"/>')
    temp.append('\t\t\t\t<Operation moduleId="AlphaOpDecay" days="1"/>')
    temp.append('\t\t\t\t<Operation moduleId="AlphaOpNeutral" group="sector"/>')
    temp.append('\t\t\t\t<Operation moduleId="AlphaOpTruncate" maxPercent="0.1"/>')
    temp.append('\t\t\t</Operations>')
    temp.append('\t\t\t<Performance moduleId="Performance"/>')
    temp.append('\t\t</Case>')
    temp.append('')
    case_modules[name] = temp

mark = 0
cnt = 0
for i in range(len(names)):
    if mark == 0:
        cfg = cfg_context.copy()

    cfg = cfg[:24]+[alpha_modules[i]]+cfg[24:]
    cfg = cfg+case_modules[names[i]]
    mark += 1
    if mark == 8:
        cnt += 1
        mark = 0
        cfg += ['\t</Sim>', '</zalpha>']
        context = ''
        for line in cfg:
            context += line+'\n'
        with open('config_FdmtIndi_'+str(cnt)+'.xml', 'w') as output:
            output.write(context)

if not mark == 0:
    cnt += 1
    cfg += ['\t</Sim>', '</zalpha>']
    context = ''
    for line in cfg:
        context += line+'\n'
    with open('config_FdmtIndi_'+str(cnt)+'.xml', 'w') as output:
        output.write(context)

with open('alpha/alpha_FdmtIndi.py', 'r') as fp:
    alpha_context = fp.read()

for name in names:
    temp = alpha_context
    temp = temp.replace('ROE',name)
    temp = temp.replace('FdmtIndi','FdmtIndi_'+name)
    with open('alpha/alpha_FdmtIndi_'+name+'.py', 'w') as output:
        output.write(temp)
