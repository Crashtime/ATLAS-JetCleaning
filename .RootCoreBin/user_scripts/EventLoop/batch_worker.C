#ifndef __CINT__
#include <EventLoop/BatchWorker.h>
#endif

void batch_worker (unsigned job_id, const char *confFile)
{
  EL::BatchWorker::execute (job_id, confFile);
}
