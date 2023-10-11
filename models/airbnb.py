#!/usr/bin/python3
import cmd 
import sys 

class MyConsole(cmd.Cmd):
    prompt = "$$"
    pass

    def do_create(self, line):
        print(line)

def precmd(self, line):
    #make app work non-interactively
    if not sys.stdin.isatty():
        print()
     
if __name__ == "__main__":
    MyConsole().cmdloop()