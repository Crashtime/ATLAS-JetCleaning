// Dear emacs, this is -*- c++ -*-
// $Id: TauJetContainer.h 665021 2015-05-05 15:52:38Z janus $
#ifndef XAODTAU_TAUJETCONTAINER_H
#define XAODTAU_TAUJETCONTAINER_H

// Local include(s):
#include "xAODTau/TauJet.h"
#include "xAODTau/versions/TauJetContainer_v2.h"

namespace xAOD {
   /// Definition of the current "taujet container version"
   typedef TauJetContainer_v2 TauJetContainer;
}

// Set up a CLID for the container:
#include "xAODCore/CLASS_DEF.h"
CLASS_DEF( xAOD::TauJetContainer, 1177172564, 1 )

#endif // XAODTAU_TAUJETCONTAINER_H
