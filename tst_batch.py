import json
import os
import time
import errno
import logging
import hdt_logger

TST_BATCH_DBS_DIR_PATH="tst_dbs"
TST_BATCH_BATS_DIR_PATH="tst_batchs"


def check_bats_dir():
    if os.path.exists(TST_BATCH_BATS_DIR_PATH):
        if os.path.isdir(TST_BATCH_BATS_DIR_PATH):
            return True
        else:
            hdt_logger.HDLogger.logger.debug(TST_BATCH_BATS_DIR_PATH + "is not a dir")
            return False
    else:
        hdt_logger.HDLogger.logger.debug(TST_BATCH_BATS_DIR_PATH + "is not exist, create it")
        os.mkdir(TST_BATCH_BATS_DIR_PATH)
        return True


class TBatch:
    def __init__(self, batch_file_path):
        hdt_logger.HDLogger.logger.debug('-')
        self.file = None
        self.t_bat_msg = None
        self.batch_file_path = batch_file_path

    def load_batch(self, new):
        if new:
            if not os.path.exists(TST_BATCH_DBS_DIR_PATH):
                hdt_logger.HDLogger.logger.debug(TST_BATCH_DBS_DIR_PATH + "is not exist, create it")
                os.mkdir(TST_BATCH_DBS_DIR_PATH)
            else:
                if not os.path.isdir(TST_BATCH_DBS_DIR_PATH):
                    hdt_logger.HDLogger.logger.debug(TST_BATCH_DBS_DIR_PATH + "is not dir")
                    return False

            if os.path.exists(self.batch_file_path):
                hdt_logger.HDLogger.logger.debug("batch file[%s] is already exist !!!" % (self.batch_file_path))
                return False
            self.file = open(self.batch_file_path, "w+")
            time_str = time.strftime("%Y%m%d_%H%M%S")
            self.t_bat_msg = {"id": "HDGZ3200_" + time_str,
                         "time": time.strftime("%Y-%m-%d %H:%M:%S"),
                         "db_file": "./" + TST_BATCH_DBS_DIR_PATH + "/HDGZ3200_" + time_str + "_log.db",
                         "success": 0,
                         "failed": 0}
            t_bat_msg_strs = json.dumps(self.t_bat_msg)
            self.file.write(t_bat_msg_strs)
            self.file.close()
        else:
            try:
                self.file = open(self.batch_file_path, "r+")
            except OSError as e:
                if e.errno == errno.ENOENT:
                    hdt_logger.HDLogger.logger.debug("file %s is not exist!" % self.batch_file_path)
                    # do your FileNotFoundError code here
                    return False
                else:
                    raise
            hdt_logger.HDLogger.logger.debug(self.file)
            t_bat_msg_strs = self.file.read()
            hdt_logger.HDLogger.logger.debug(t_bat_msg_strs)
            self.file.close()
            self.t_bat_msg = json.loads(t_bat_msg_strs)
        return True

    def load_batch_new(self):
        return self.load_batch(True)

    def load_batch_exist(self):
        return self.load_batch(False)

    def upload_batch(self, success_count=None, failed_count=None):
        if success_count:
            self.t_bat_msg['success'] = success_count
        if failed_count:
            self.t_bat_msg['failed'] = failed_count
        t_bat_msg_strs = json.dumps(self.t_bat_msg)

        self.file = open(self.batch_file_path, "r+")
        self.file.write(t_bat_msg_strs)
        self.file.close()

    def get_db_file(self):
        return self.t_bat_msg['db_file']

    def get_bat_id(self):
        return self.t_bat_msg['id']

    def get_bat_time(self):
        return self.t_bat_msg['time']

    def get_success_count(self):
        return self.t_bat_msg['success']

    def get_failed_count(self):
        return self.t_bat_msg['failed']

if __name__ == "__main__":
    t_bat = TBatch("HDGZ3200_20180420_04201505.tbat") # HDGZ3200_20180420.tbat
    if t_bat.load_batch(False):
        t_bat.upload_batch(100, 3)
        hdt_logger.HDLogger.logger.debug(t_bat.get_db_file())



