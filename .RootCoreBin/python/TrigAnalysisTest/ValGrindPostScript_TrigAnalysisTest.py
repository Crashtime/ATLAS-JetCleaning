# Simple wrapper for specific RttScriptRunner instances
# This is done to get "pretty" names on the RTT web pages

from RecExConfig.RecFlags import rec
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags as acf

import sys, os
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

from RttScriptRunner_TrigAnalysisTest import RttScriptRunner_TrigAnalysisTest

class ValGrindPostScript_TrigAnalysisTest(RttScriptRunner_TrigAnalysisTest):
    pass

#add tony's python post script for valgrind after this:
#sed -e '/    definitely lost: / { N; d; }' Valgrind_*_log > Valgrind_test_log_1
#!!!