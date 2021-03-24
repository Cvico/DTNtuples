# DTNtuples
Analysis tools to get the AM simulated performance plots. 

## Preliminary instructions
**Note**: 
In the present days this code is evolving fast, hence the installation recipe may change often. Please keep an eye on this page to check for updates.

### Installation:
```
cmsrel CMSSW_10_6_5_patch1
cd CMSSW_10_6_5_patch1/src/
cmsenv
git clone https://github.com/NTrevisani/DTNtuples.git -b unifiedPerf DTDPGAnalysis/DTNtuples
scramv1 b -j 5
```
### Analysis:

This repository groups 4 types of plotting tools, all available using python scripts: 
- Efficiency plots w.r.t segments (using ```runEffs.py```)
- Resolution plots w.r.t segments (using ```runResols.py```)
- Digi rates (using ```runDigis.py```)
- Primitive rates (using ```runRates.py```)

