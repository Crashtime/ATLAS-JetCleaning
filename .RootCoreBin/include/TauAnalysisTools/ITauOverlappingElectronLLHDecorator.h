// Dear emacs, this is -*- c++ -*-
#ifndef TAUANALYSISTOOLS_ITAUOVERLAPPINGELECTRONLLHDECORATOR_H
#define TAUANALYSISTOOLS_ITAUOVERLAPPINGELECTRONLLHDECORATOR_H

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
#include "AsgTools/IAsgTool.h"

// EDM include(s):
#include "xAODTau/TauJet.h"
#include "PATInterfaces/CorrectionCode.h"

namespace TauAnalysisTools
{

class ITauOverlappingElectronLLHDecorator : public virtual asg::IAsgTool
{

  /// Declare the interface that the class provides
  ASG_TOOL_INTERFACE( TauAnalysisTools::ITauOverlappingElectronLLHDecorator )

public:

  /// Function initialising the tool
  virtual StatusCode initialize() = 0;

  virtual StatusCode initializeEvent() = 0;

  virtual StatusCode decorate(const xAOD::TauJet& xTau) = 0;

}; // class ITauOverlappingElectronLLHDecorator

} // namespace TauAnalysisTools

#endif // TAUANALYSISTOOLS_ITAUOVERLAPPINGELECTRONLLHDECORATOR_H
