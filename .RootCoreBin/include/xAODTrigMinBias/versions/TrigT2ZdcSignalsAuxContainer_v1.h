#ifndef xAODTrigMinBias_TrigT2ZdcSignalsAUXCONTAINTER_V1_H
#define xAODTrigMinBias_TrigT2ZdcSignalsAUXCONTAINTER_V1_H

#include "xAODCore/AuxContainerBase.h"

#include <vector>

namespace xAOD {

  class TrigT2ZdcSignalsAuxContainer_v1 : public AuxContainerBase {

  public:
    TrigT2ZdcSignalsAuxContainer_v1();

  private:
    std::vector<std::vector<float> > triggerEnergies;
    std::vector<std::vector<float> > triggerTimes;
  };

}

#include "xAODCore/BaseInfo.h"
SG_BASE(   xAOD::TrigT2ZdcSignalsAuxContainer_v1, xAOD::AuxContainerBase );

#endif
