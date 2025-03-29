import sys
import os
import tarfile
from datetime import datetime

logs_archive_dir = '/var/log/logs_archive_' + datetime.now().strftime('%Y%m%d_%H%M%S') + 'tar.gz' # save file path (under /var/log/ directory)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        log_dir = sys.argv[1] # directory argument
        if os.path.isdir(log_dir):
            if len(os.listdir(log_dir)) == 0: # if log dir empty
                print("log directory", '"' + log_dir + '"', "is empty!")
                sys.exit()

            with tarfile.open(logs_archive_dir, 'w:gz') as tar:
                for root, dirs, logs in os.walk(log_dir):
                    for log in logs:
                        log_path = os.path.join(root, log)
                        tar.add(log_path, arcname=os.path.relpath(log_path, log_dir))
                        os.remove(log_path) # remove log after archiving
        else:
            print("Directory", log_dir, "does not exist!")
    else:
        print("Please provide exactly one argument - log directory")
