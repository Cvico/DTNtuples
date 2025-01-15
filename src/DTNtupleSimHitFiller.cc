/** \class DTNtupleSimHitFiller DTNtupleSimHitFiller.h DTDPGAnalysis/DTNtuples/src/DTNtupleSimHitFiller.h
 *  
 * Helper class : the sim hit filler for Phase-1 / Phase2 SimHits (the DataFormat is the same)
 *
 * \author C. Vico (Uniovi)
 *
 *
 */

#include "DTDPGAnalysis/DTNtuples/src/DTNtupleSimHitFiller.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/DetId/interface/DetId.h"


// PSimHits_g4SimHits_MuonDTHits_SIM.obj

DTNtupleSimHitFiller::DTNtupleSimHitFiller(edm::ConsumesCollector && collector,
				       const std::shared_ptr<DTNtupleConfig> config, 
				       std::shared_ptr<TTree> tree, const std::string & label,
				       SimHitTag tag) : 
  DTNtupleBaseFiller(config, tree, label), m_tag(tag)
{

  edm::InputTag & iTag = m_tag == SimHitTag::dt ?
                                  m_config->m_inputTags["dtSimMuonHit"] :
                                  m_config->m_inputTags["rpcSimMuonHit"];

  // Set up the reference detector and subdetector ID tags
  RefSubdetIdTag = m_tag == SimHitTag::dt ? 
	  MuonSubdetId::DT : MuonSubdetId::RPC;	

  if (iTag.label() != "none") m_simHitToken = collector.consumes<edm::PSimHitContainer>(iTag);

}

DTNtupleSimHitFiller::~DTNtupleSimHitFiller() 
{ 

};

void DTNtupleSimHitFiller::initialize()
{
  
  m_tree->Branch((m_label + "_nSimHits").c_str(), &m_nSimHits, (m_label + "_nSimHits/i").c_str());
  m_tree->Branch((m_label + "_processType").c_str(), &m_processType);   
  m_tree->Branch((m_label + "_particleType").c_str(), &m_particleType);  
  m_tree->Branch((m_label + "_trackMomentum").c_str(), &m_trackMomentum);  
  m_tree->Branch((m_label + "_wheel").c_str(), &m_simHit_wheel);   
  m_tree->Branch((m_label + "_sector").c_str(), &m_simHit_sector);  
  m_tree->Branch((m_label + "_station").c_str(), &m_simHit_station); 
  m_tree->Branch((m_label + "_superLayer").c_str(), &m_simHit_superLayer); 
  m_tree->Branch((m_label + "_layer").c_str(), &m_simHit_layer);      
  m_tree->Branch((m_label + "_wire").c_str(), &m_simHit_wire);
  
}

void DTNtupleSimHitFiller::clear()
{

  m_nSimHits = 0;
  m_processType.clear();   
  m_particleType.clear();  
  m_trackMomentum.clear();  
  m_simHit_wheel.clear();   
  m_simHit_sector.clear();  
  m_simHit_station.clear(); 
  m_simHit_superLayer.clear(); 
  m_simHit_layer.clear();      
  m_simHit_wire.clear();       

}

void DTNtupleSimHitFiller::fill(const edm::Event & ev)
{

 clear();

 auto simHits = conditionalGet<edm::PSimHitContainer>(ev, m_simHitToken, "PSimHitContainer");

 if (simHits.isValid()) {
        // Loop over each hit
        for (const auto& hit : *simHits) {
            // Access hit properties


	    // Try to find where the hit is from
	    DetId detId = hit.detUnitId();  // Detector ID to track down where the simHit comes from
	    auto SubDetId = detId.subdetId();  // Detector ID to track down where the simHit comes from

	    // Filter out hits that do not belong to the muon system	
	    if ( detId.det() == RefDetIdTag && SubDetId == RefSubdetIdTag ) { 
		    // std::cout << "Hit detected in Muon system" << std::endl;
		    //const DTChamberId chamb = DTChamberId( detId );
		    //const DTSuperLayerId sl = DTSuperLayerId( detId );
		    const DTWireId wireID = DTWireId( detId );

		    // Unpack the location
		    // Wire:
		    auto wire = wireID.wire();

		    // Layer:
		    const DTLayerId layerID = wireID.layerId();
		    auto layer = layerID.layer();

		    // SuperLayer:
		    const DTSuperLayerId superlayerID = layerID.superlayerId();
		    auto superlayer = superlayerID.superlayer();

		    // full chamber:
		    const DTChamberId chamberID = superlayerID.chamberId();
		    auto wheel = chamberID.wheel();
		    auto sector = chamberID.sector();
		    auto station = chamberID.station();

		    //std::cout << "This hit belongs to Wh " << wheel << " Sc: " << sector << " St: " << station << " SL: " << superlayer << " L: " << layer << " w: " << wire << std::endl;

		    // Now get the parameters of the hit
         	    auto trackMomentum = hit.pabs(); // Momentum magnitude for the track that originated the simHit
                    auto processType  = hit.processType(); // Geant4 process see cmssw/SimG4Core/Physics/src/G4ProcessTypeEnumerator.cc
                    auto particleType = hit.particleType(); // Geant4 process see cmssw/SimG4Core/Physics/src/G4ProcessTypeEnumerator.cc
                    //short trackId = hit.trackId(); // Geant4 process see cmssw/SimG4Core/Physics/src/G4ProcessTypeEnumerator.cc
                    //short originalTrackId = hit.originalTrackId(); // Geant4 process see cmssw/SimG4Core/Physics/src/G4ProcessTypeEnumerator.cc

		    //std::cout << "  - ProcessType " << processType << std::endl;
		    //std::cout << "  - ParticleType " << particleType << std::endl;
		    //std::cout << "  - trackMomentum " << trackMomentum << std::endl;
		    //std::cout << "  - trackId " << trackId << std::endl;
		    //std::cout << "  - originalTrackId " << originalTrackId << std::endl;
		    
		    // Fill the properties of the simHit
		    m_processType.push_back( processType );   
                    m_particleType.push_back( particleType );  
                    m_trackMomentum.push_back( trackMomentum );  
                    m_simHit_wheel.push_back( wheel );   
                    m_simHit_sector.push_back( sector);  
                    m_simHit_station.push_back( station ); 
                    m_simHit_superLayer.push_back( superlayer ); 
                    m_simHit_layer.push_back( layer );      
                    m_simHit_wire.push_back( wire );       

		    m_nSimHits++;

	    }
        }
  }

  return;

}

