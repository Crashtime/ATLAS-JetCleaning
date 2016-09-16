// Dear emacs, this is -*-c++-*-

#ifndef __ASGELECTRONISEMSELECTOR__
#define __ASGELECTRONISEMSELECTOR__

/**
   @class AsgElectronIsEMSelector
   @brief Tool to select objects.

   @author Jovan Mitrevski (UCSC) Karsten Koeneke (CERN)
   @date   Dec 2011 - Fab 2012

   Based on egammaElectronCutIDTool, by F. Derue.

   11-MAR-2014, convert to ASGTool (Jovan Mitrevski)

*/

// Atlas includes
#include "AsgTools/AsgTool.h"

// Include the interfaces
#include "ElectronPhotonSelectorTools/IAsgElectronIsEMSelector.h"
// Include the return object and the underlying ROOT tool
#include "PATCore/TAccept.h"
#include "ElectronPhotonSelectorTools/TElectronIsEMSelector.h"
#include <string>

class AsgElectronIsEMSelector :  public asg::AsgTool, 
				 virtual public IAsgElectronIsEMSelector
{

  ASG_TOOL_CLASS3(AsgElectronIsEMSelector, IAsgElectronIsEMSelector,
		  IAsgEGammaIsEMSelector,IAsgSelectionTool)

  public:
  /** Standard constructor */
  AsgElectronIsEMSelector(std::string myname);

  /** Standard destructor */
  virtual ~AsgElectronIsEMSelector();

  /** Gaudi Service Interface method implementations */
  virtual StatusCode initialize();

  /** Gaudi Service Interface method implementations */
  virtual StatusCode finalize();

  // Main methods for IAsgSelectionTool interface


  /** Accept with generic interface */
  virtual const Root::TAccept& accept( const xAOD::IParticle* part ) const ;

  /** Accept with generic interface */
  virtual const Root::TAccept& accept( const xAOD::IParticle& part ) const {
    return accept(&part);
  }
  
  /** Accept with Egamma objects */
  virtual const Root::TAccept& accept( const xAOD::Egamma* part) const ;

  /** Accept with Egamma objects */
  virtual const Root::TAccept& accept( const xAOD::Egamma& part) const {
    return accept(&part);
  }

  /** Accept with Photon objects */
  virtual const Root::TAccept& accept( const xAOD::Photon* part ) const ;

  /** Accept with Photon objects */
  virtual const Root::TAccept& accept( const xAOD::Photon& part ) const {
    return accept(&part);
  }

  /** Accept with Electron objects */
  virtual const Root::TAccept& accept( const xAOD::Electron* part ) const ;

  /** Accept with Electron objects */
  virtual const Root::TAccept& accept( const xAOD::Electron& part ) const{
    return accept(&part);
  }

  /** The value of the isem **/
  unsigned int IsemValue() const {return m_rootTool->isEM(); };

  /** Method to get the operating point */
  virtual std::string getOperatingPointName( ) const;

  //The main execute method
  StatusCode execute(const xAOD::Egamma* eg) const;

  /** Method to get the plain TAccept */
  virtual const Root::TAccept& getTAccept( ) const{
    return m_rootTool->getTAccept();
  }


  // Private member variables
private:

  unsigned int calocuts_electrons(const xAOD::Egamma* eg, 
				  float eta2, double et,
				  double trigEtTh,
				  unsigned int iflag) const;

  unsigned int TrackCut(const xAOD::Electron* eg, 
			float eta2, double et, double energy,
			unsigned int iflag) const;

  /** Config File */
  std::string m_configFile;

  /** Pointer to the underlying ROOT based tool */
  Root::TElectronIsEMSelector* m_rootTool;

  /** @brief use f3core or f3 (default: use f3)*/
  bool m_useF3core;

  /** A dummy return TAccept object */
  Root::TAccept m_acceptDummy;

  /// Flag for calo only cut-base 
  bool m_caloOnly; 
  float m_trigEtTh;

  
}; // End: class definition


#endif
