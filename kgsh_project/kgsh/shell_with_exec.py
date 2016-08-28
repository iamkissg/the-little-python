import os
import sys
import shlex  # A lexical analyzer class for simple shell-like syntaxes

SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0


def tokenize(string):
    """Split string into list of shell-like strings"""
    return shlex.split(string)

def execute(cmd_tokens):
    # `execvp(file, args)`, is a variant of system call `exec
    # `v` means the second arg is a list (or tuple) of program args
    # `p` means searching along $PATH
    # Execute the executable file (which is searched for along $PATH)
    # with argument list args, replacing the current process.
    os.execvp(cmd_tokens[0], cmd_tokens)
    # `exec` will replace the memory of current process with the new process
    # the new process becomes the main process, and the "current" on is exited
    # That's why, the shell can just execute one command only.

    # Return status indicating to wait for next command in shell_loop
    return SHELL_STATUS_RUN

# Main loop ofshell
def shell_loop():
    status = SHELL_STATUS_RUN
    while status:
        # Display a command prompt
        # sys.stdout is a _io.TextIOWrapper instance
        sys.stdout.write('>')
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

    main()
