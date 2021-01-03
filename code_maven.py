#!/usr/bin/env python

# https://code-maven.com/interactive-shell-with-cmd-in-python

from cmd import Cmd 

class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = 'Welcome! Type ? to list commands.'

    def do_exit(self, inp):
        '''Exit the application.'''
        print("Bye")
        return True

    def help_exit(self):
        print('Exit the application. Shorthand: x q Ctrl-D.')

    def do_add(self, inp):
        print("Adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    MyPrompt().cmdloop()
