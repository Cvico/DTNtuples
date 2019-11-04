#ifndef DTTnPBaseAnalysis_h
#define DTTnPBaseAnalysis_h

#include "DTNtupleBaseAnalyzer.h"

#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TEfficiency.h"
#include "TMath.h"

#include <string>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <map>

class DTNtupleTPGSimAnalyzer : public DTNtupleBaseAnalyzer 
{
  
public:
  
  DTNtupleTPGSimAnalyzer(const TString & inFileName,
			 const TString & outFileName);
  ~DTNtupleTPGSimAnalyzer();

  void virtual Loop() override;

protected:
  
  void book();
  void fill();
  void endJob();

private:
  
  Double_t trigPhiInRad(Double_t trigPhi, Int_t sector);
  
  TFile m_outFile;
  
  std::map<std::string, TH1*> m_plots;
  std::map<std::string, TH2*> m_plots2;
  std::map<std::string, TEfficiency*> m_effs;
  
  TH1F* makeHistoPer( std::string, std::string, vector<std::string>, std::string);  
  TH1F* makeHistoPerCorrelated( std::string, std::string, vector<std::string>, std::string);  
  Double_t m_minMuPt;
  Double_t m_maxMuPt;
  
  Double_t m_maxMuSegDPhi;
  Double_t m_maxMuSegDEta;
  
  Int_t m_minSegHits;
  Int_t m_minSegZHits;

  Double_t m_maxSegTrigDPhi;
  Double_t m_maxMuTrigDPhi;

  bool unique; 
  Int_t numberOfEntries;  
  
};

#endif
