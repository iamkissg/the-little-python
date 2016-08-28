import os
import sys
import shlex  # A lexical analyzer class for simple shell-like syntaxes
from kgsh.constants import SHELL_STATUS_RUN, SHELL_STATUS_STOP
from kgsh.builtins import *

# Hash map to store built-in function name and refernence as key and value
built_in_cmds = {}

def register_command(name, func):
    """register built-in cmd"""
    built_in_cmds[name] = func

def init():
    register_command("cd", cd)
    register_command("exit", exit)


def tokenize(string):
    """Split string into list of shell-like strings"""
    return shlex.split(string)

def execute(cmd_tokens):
    """"""
    cmd_name = cmd_tokens[0]
    cmd_args = cmd_tokens[1:]
    if cmd_name in built_in_cmds:
        return built_in_cmds[cmd_name](cmd_args)

    # `os.fork()` - Fork a child process
    # 1 call, 2 return values
    # Return 0 to child process and pid of child to parent process
    # `fork` will allocate new memory for child process
    pid = os.fork()
    # Here we have actually 2 same process, the child and the parent
    if pid == 0:
        # replace the fork child process with cmd_tokens[0] process
        os.execvp(cmd_tokens[0], cmd_tokens)
    elif pid > 0:
        # parent process
        while True:
            # Wait response status from its child process (identified with pid)
            # `os.waitpid(pid, options)` wait for completion of a given child process
            wpid, status = os.waitpid(pid, 0)
            # WIFEXITED(status) -> bool
            # Return true if the process returning 'status' exited using the exit()
            # WIFSIGNALED(status) -> bool
            # Return True if the process returning 'status' was terminated by a signal
            if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                break
    return SHELL_STATUS_RUN

# Main loop ofshell
def shell_loop():
    status = SHELL_STATUS_RUN
    while status:
        # Display a command prompt
        # sys.stdout is a _io.TextIOWrapper instance
        sys.stdout.write('kissg> ')
        # Flush the write buffers of the stream if applicable
        # Does nothing for read-only and non-blocking streams
        sys.stdout.flush()

        # Read command input
        cmd = sys.stdin.readline()

        # Tokenize the command input
        cmd_tokens = tokenize(cmd)

        # Execute the command and retrieve new status
        status = execute(cmd_tokens)

def main():
    shell_loop()


if __name__ == '__main__':
    init()
    main()
