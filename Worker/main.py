import time
import multiprocessing
from common import Config, printdebug, printsuccess, printerror, printheader, WorkerHandler
from constants import SCHEDULER_SERVER_URL, REQUEST_ERROR_WAIT_TIME, REQUEST_COUNT_LIMIT
from Worker import Worker

class WorkerProcess(multiprocessing.Process):
    
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.WorkerHandler = WorkerHandler()

    def run(self):
        while True:

            work_object = self.WorkerHandler.get_worker()
            
            # READY state - Wait for a task
            if work_object['status'] == Config.get('worker_status_list')[0]:
                
                work_object = self.WorkerHandler.post_worker(work_object)
                work_object['status'] == Config.get('worker_status_list')[1] and Worker(work_object, self.WorkerHandler).start()


            # WORKING state - do nothing
            elif work_object['status'] == Config.get('worker_status_list')[1]:
                pass

            # DONE state - Change to READY state and wait for a task
            # ERROR state - Change to READY state and wait for a task
            elif (work_object['status'] == Config.get('worker_status_list')[2]) or (work_object['status'] == Config.get('worker_status_list')[-1]):
                work_object['status'] = Config.get('worker_status_list')[0]
                work_object = self.WorkerHandler.post_worker(work_object)
                work_object['status'] == Config.get('worker_status_list')[1] and Worker(work_object, self.WorkerHandler).start()

            sleep_time = Config.get('worker_ready_poll_freq') if work_object['status'] == Config.get('worker_status_list')[0] else Config.get('worker_working_poll_freq')
            time.sleep(sleep_time)

if __name__ == '__main__':
    for _ in range(Config.get('worker_process_count')):
        WorkerProcess().start()