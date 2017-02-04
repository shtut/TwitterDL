"""
The summary worker handles the creation of the final core-set.
Holds a regular worker.
"""
from worker import Worker
import message_codes as codes


class SummaryWorker(Worker):
    def __init__(self, server):
        Worker.__init__(self, server)

    def _worker_code(self):
        return codes.REGISTER_SUMMARY_WORKER
