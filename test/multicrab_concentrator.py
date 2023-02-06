''' Crab configuration file for Phase2 concentrator studies '''

# For CMSSW_12_2_0_pre2 a special configuration must be done:
# source /cvmfs/cms.cern.ch/common/crab-setup.sh dev
# python3 multicrab.py

name = 'ZtoMuMu_Run3sample'  #Part of the name of your output directory, adapt as needed.  
running_options = ["nEvents=1000"]
runATCAF = False


# Dictionary to store metadata
dataset = {
   # Z -> mumu prompt muons
   "ZprimeToMuMu_M-6000_TuneCP5_14TeV-pythia8" : "/ZprimeToMuMu_M-6000_TuneCP5_14TeV-pythia8/Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2/GEN-SIM-DIGI-RAW",
}

# Samples to run (these are keys in the above dictionary)
listOfSamples = [
   'ZprimeToMuMu_M-6000_TuneCP5_14TeV-pythia8',
]

if __name__ == '__main__':
   # import crab stuff
   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   
   def submit(config):
       ''' Function to handle job submission '''
       res = crabCommand('submit', config = config )

   config.General.workArea = 'analysis_'+name
   config.General.transferLogs = True
   config.General.transferOutputs = True

   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'dtDpgNtuples_phase2conc_cfg.py'

   config.JobType.pyCfgParams = running_options
   config.JobType.allowUndistributedCMSSW = True

   config.Data.inputDBS = 'global' 
   config.Data.splitting = 'FileBased'
   config.Data.publication = False
   config.Data.unitsPerJob = 1
   config.Site.storageSite = 'T3_CH_CERNBOX'
   config.Site.blacklist = ['T2_US_Wisconsin', 'T1_RU_JINR', 'T2_RU_JINR', 'T2_EE_Estonia']
   if runATCAF :
      config.Site.whitelist = ['T3_CH_CERN_CAF']
      config.Site.ignoreGlobalBlacklist = True
      config.Data.ignoreLocality = True

   for sample in listOfSamples:
       
      config.General.requestName = sample
      config.Data.inputDataset = dataset[sample]
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()
