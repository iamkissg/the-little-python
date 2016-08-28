import os
# from ..constants import SHELL_STATUS_RUN, SHELL_STATUS_STOP
from kgsh.constants import SHELL_STATUS_RUN, SHELL_STATUS_STOP

def cd(args):
    os.chdir(args[0])
    return SHELL_STATUS_RUN
