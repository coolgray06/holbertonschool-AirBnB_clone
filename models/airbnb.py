#!/usr/bin/python3
import cmd 


class MyConsole(cmd.Cmd):
    prompt = "$$"
    pass

    def do_create(self, line):
        print("")

if __name__ == "__main__":
    MyConsole().cmdloop()