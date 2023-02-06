# DTNtuples
Ntuples for the analysis of the CMS drift tubes detector performance

## Preliminary instructions
**Note**: 
In the present days this code is evolving fast, hence the installation recipe may change often. Please keep an eye on this page to check for updates.

### Installation:
```bash
cmsrel CMSSW_12_4_2
cd CMSSW_12_4_2/src/
cmsenv

git cms-init
# To be updated
# git cms-merge-topic oglez:Phase2_DTAB7Unpacker_v11.2
git clone https://github.com/cvico/DTNtuples.git DTDPGAnalysis/DTNtuples

scramv1 b -j 5
```

### Ntuple production with cmsRun:
```
cd DTDPGAnalysis/DTNtuples/test/
cmsRun dtDpgNtuples_slicetest_cfg.py nEvents=10000
# or
cmsRun dtDpgNtuples_phase2_cfg.py nEvents=10000
# or
cmsRun dtDpgNtuples_phase2conc_cfg.py nEvents=10000
```

### Ntuple production with cmsRun:
```
source /cvmfs/cms.cern.ch/common/crab-setup.sh dev
python3 multicrab_concentrator.py 
```

### Analysis:
```
root -b
root [0] .x loadExampleAnalysis.C

root [1] DTNtupleExampleAnalyzer analysis("DTDPGNtuple_run333510.root","results.root")
// or
root [1] DTNtupleExampleAnalyzer analysis("DTDPGNtuple_11_0_2_Phase2_Simulation.root","results.root")

root [2] analysis.Loop()
```
