#!/bin/bash
# define type of script

function nfe() {
  pwd | pbcopy

  cd /Users/Leina/Documents/PythonProgramming/NotesAutomation || return
  python notes.py $1 $2 $3

  cd $pbpaste || return
}


# source /Users/Leina/Documents/PythonProgramming/NotesAutomation/.my_commands.sh
# in order to call internal functions directly