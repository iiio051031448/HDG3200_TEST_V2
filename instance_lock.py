import socket
import os
ONE_INSTANCE_LOCK_FILE= "one.lock"


class OneInstanceLock():
    """
     try:
        s = socket.socket()
        s.bind(("127.0.0.1", 60123))
        print('only this instance')
        return True
     except Exception as e:
        print('already has an instance')
        return False
    """

    def __init__(self):
        self.file = None

    def is_locked(self):
        if not os.path.exists(ONE_INSTANCE_LOCK_FILE):
            self.file = open(ONE_INSTANCE_LOCK_FILE, "w+")
            self.file.write("running")
            self.file.close()
            return False
        else:
            return True

    def unlock(self):
        if self.file and os.path.exists(ONE_INSTANCE_LOCK_FILE):
            os.unlink(ONE_INSTANCE_LOCK_FILE)
