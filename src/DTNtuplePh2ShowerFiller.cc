/** \class DTNtuplePh2ShowerFiller DTNtuplePh2ShowerFiller.cc DTDPGAnalysis/DTNtuples/src/DTNtuplePh2ShowerFiller.cc
 *  
 * Helper class : the Phase-2 local showerger filler for shower information 
 *
 *
 * \author C. Vico (Uniovi ES)
 *
 *
 */

#include "DTDPGAnalysis/DTNtuples/src/DTNtuplePh2ShowerFiller.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include <iostream>

DTNtuplePh2ShowerFiller::DTNtuplePh2ShowerFiller(edm::ConsumesCollector && collector,
			     const std::shared_ptr<DTNtupleConfig> config, 
			     std::shared_ptr<TTree> tree, const std::string & label, 
			     TriggerTag tag) : 
  DTNtupleBaseFiller(config, tree, label), m_tag(tag)
{

  edm::InputTag iTag = m_config->m_inputTags["ph2ShowerTag"];
  m_dtShowerToken = collector.consumes<L1Phase2MuDTShowerContainer>(iTag);
}

DTNtuplePh2ShowerFiller::~DTNtuplePh2ShowerFiller() 
{ 

};

void DTNtuplePh2ShowerFiller::initialize()
{
  m_tree->Branch((m_label + "_wheel").c_str(),   &m_wheel);
  m_tree->Branch((m_label + "_sector").c_str(),  &m_sector);
  m_tree->Branch((m_label + "_station").c_str(), &m_station);
  m_tree->Branch((m_label + "_BX").c_str(),    &m_bx);
  m_tree->Branch((m_label + "_ndigis").c_str(),    &m_ndigis);
  m_tree->Branch((m_label + "_avg_pos").c_str(),    &m_avg_pos);
  m_tree->Branch((m_label + "_avg_time").c_str(),    &m_avg_time);
  
}

void DTNtuplePh2ShowerFiller::clear()
{

  m_wheel.clear();
  m_sector.clear();
  m_station.clear();

  m_bx.clear();
  m_ndigis.clear();
  m_avg_pos.clear();
  m_avg_time.clear();

}

void DTNtuplePh2ShowerFiller::fill(const edm::Event & ev)
{

  clear();

  auto showerColl = conditionalGet<L1Phase2MuDTShowerContainer>(ev, m_dtShowerToken,"L1Phase2MuDTShowerContainer");

  if (showerColl.isValid()) 
    {      
      const auto showers = showerColl->getContainer();
      for(const auto & shower : (*showers))
	{

	  m_wheel.push_back(shower.whNum());
	  m_sector.push_back(shower.scNum() + 1); 
	  m_station.push_back(shower.stNum());
	  

	  m_bx.push_back(shower.bxNum());

	  m_ndigis.push_back(shower.ndigis());
	  m_avg_time.push_back(shower.avg_time());
	  m_avg_pos.push_back(shower.avg_pos());
	
	}
    }
  
  return;

}

