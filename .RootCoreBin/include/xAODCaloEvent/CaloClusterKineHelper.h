//Dear emacs, this is -*- c++ -*-
#ifndef XAOD_ANALYSIS
#ifndef CALOCLUSTERKINEHELPER_H
#define CALOCLUSTERKINEHELPER_H

#include "xAODCaloEvent/CaloCluster.h"

class CaloClusterKineHelper {

  /// Helper class to calculate cluster kinematics based on cells
  /// @author Walter Lampl <Walter.Lampl@cern.ch>

 public:

  ///Calculate cluster kinematics from contained cells
  static void calculateKine(xAOD::CaloCluster* clu, const bool useweight=true, const bool updateLayers=true );

};

#endif
#endif
