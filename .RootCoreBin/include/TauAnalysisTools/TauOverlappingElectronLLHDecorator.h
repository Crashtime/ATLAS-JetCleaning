// Dear emacs, this is -*- c++ -*-
#ifndef TAUANALYSISTOOLS_TAUOVERLAPPINGELECTRONLLHDECORATOR_H
#define TAUANALYSISTOOLS_TAUOVERLAPPINGELECTRONLLHDECORATOR_H

/*
  author: Dirk Duschinger
  mail: dirk.duschinger@cern.ch
  documentation in: ../README.rst
                    or
                    https://svnweb.cern.ch/trac/atlasoff/browser/PhysicsAnalysis/TauID/TauAnalysisTools/tags/TauAnalysisTools-<tag>/README.rst
		    or
                    https://svnweb.cern.ch/trac/atlasoff/browser/PhysicsAnalysis/TauID/TauAnalysisTools/trunk/README.rst
*/

// Framework include(s):
#include "AsgTools/AsgTool.h"
#include "ElectronPhotonSelectorTools/AsgElectronLikelihoodTool.h"

// EDM include(s):
#include "xAODEgamma/ElectronContainer.h"

// Local include(s):
#include "TauAnalysisTools/ITauOverlappingElectronLLHDecorator.h"

// ROOT include(s):
#include "TH2D.h"

namespace TauAnalysisTools
{

class TauOverlappingElectronLLHDecorator
  : public virtual ITauOverlappingElectronLLHDecorator
  , public asg::AsgTool
{

  /// Create a proper constructor for Athena
  ASG_TOOL_CLASS( TauOverlappingElectronLLHDecorator,
                  TauAnalysisTools::ITauOverlappingElectronLLHDecorator )

public:
  /// Create a constructor for standalone usage
  TauOverlappingElectronLLHDecorator( const std::string& name );

  ~TauOverlappingElectronLLHDecorator( );

  /// Function initialising the tool
  virtual StatusCode initialize();

  virtual StatusCode initializeEvent();

  virtual StatusCode decorate(const xAOD::TauJet& xTau);

private:
  AsgElectronLikelihoodTool* m_tEMLHTool;
  const xAOD::ElectronContainer* m_xElectronContainer;
  std::string m_sElectronContainerName;
  bool m_bElectonsAvailable;
  std::string m_sEleOLRFilePath;
  TH2D* m_hCutValues;

private:
  float getCutVal(float fEta, float fPt);
  StatusCode retrieveElectrons();

private:
  bool m_bEleOLRMatchAvailable;
  bool m_bEleOLRMatchAvailableChecked;

  std::string m_sElectronPhotonSelectorToolsConfigFile;

}; // class TauOverlappingElectronLLHDecorator

} // namespace TauAnalysisTools

#endif // TAUANALYSISTOOLS_TAUOVERLAPPINGELECTRONLLHDECORATOR_H
