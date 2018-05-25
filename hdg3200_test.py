import logging
import win
import instance_lock as i_lock
import atexit
import hdt_logger

one_lock = None
hdt_logger.HDLogger.logger.debug("--------------- STARTING ---------------")


def exit_cleanup():
    hdt_logger.HDLogger.logger.error("=======exit_cleanup========")
    if one_lock:
        one_lock.unlock()

atexit.register(exit_cleanup)

one_lock = i_lock.OneInstanceLock()

main_win = win.hdg3200_win()
if not one_lock.is_locked():
    main_win.show_win()
else:
    main_win.show_one_instance_warning_box()

hdt_logger.HDLogger.logger.debug("--------------- EXITING ---------------")

one_lock.unlock()
