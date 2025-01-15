#ifndef DTNtuple_DTNtupleSimHitFiller_h
#define DTNtuple_DTNtupleSimHitFiller_h

/** \class DTNtupleSimHitFiller DTNtupleSimHitFiller.h DTDPGAnalysis/DTNtuples/src/DTNtupleSimHitFiller.h
 *  
 * Helper class : the sim hit filler for Phase-1 / Phase2 SimHits (the DataFormat is the same)
 *
 * \author C. Vico (Uniovi)
 *
 *
 */

#include "DTDPGAnalysis/DTNtuples/src/DTNtupleBaseFiller.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/MuonDetId/interface/MuonSubdetId.h"
#include "DataFormats/MuonDetId/interface/DTChamberId.h"
#include "DataFormats/MuonDetId/interface/DTSuperLayerId.h"
#include "DataFormats/MuonDetId/interface/DTLayerId.h"
#include "DataFormats/MuonDetId/interface/DTWireId.h"
#include <vector>

class DTNtupleSimHitFiller : public DTNtupleBaseFiller
{

 public:

  enum class SimHitTag { dt = 0, rpc };

  /// Constructor
  DTNtupleSimHitFiller(edm::ConsumesCollector && collector,
		     const std::shared_ptr<DTNtupleConfig> config, 
		     std::shared_ptr<TTree> tree, const std::string & label, 
		     SimHitTag tag);

  ///Destructor
  virtual ~DTNtupleSimHitFiller();
 
  /// Intialize function : setup tree branches etc ... 
  virtual void initialize() final;
  
  /// Clear branches before event filling 
  virtual void clear() final;

  /// Fill tree branches for a given events
  virtual void fill(const edm::Event & ev) final;    

 private :

  SimHitTag m_tag;
  const int RefDetIdTag = DetId::Muon; // Always get hits from the Muon system
  int RefSubdetIdTag;

  /// The simHit token
  edm::EDGetTokenT<edm::PSimHitContainer> m_simHitToken;

  /// The variables holding
  /// all simhit related information

  int m_nSimHits; // the # of simHits (size of all following vectors)
  std::vector<short> m_processType;
  std::vector<int> m_particleType;
  std::vector<float> m_trackMomentum;
  std::vector<short> m_simHit_wheel;
  std::vector<short> m_simHit_sector;
  std::vector<short> m_simHit_station;
  std::vector<short> m_simHit_superLayer;
  std::vector<short> m_simHit_layer;
  std::vector<short> m_simHit_wire;
  

};
  
#endif

