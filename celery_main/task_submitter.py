import sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '../data')))

from src.setting import TARGET_FILE
from .task_receiver import do_work


def submit_handles(handles):
    for handle in handles:
        handle = handle.strip()
        handle = handle.strip(".!,")
        do_work.delay(handle)
        print("submitted " + handle)


if __name__ == '__main__':
    handles = list()
    with open(f'{TARGET_FILE}', "r") as f:
        handles = f.readlines()

    submit_handles(handles)
