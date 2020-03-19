#!/bin/bash
# define type of script

function nfe() {
  pwd | pbcopy

  cd /Users/Leina/Documents/PythonProgramming/NotesAutomation || return
  python notes.py $1 $2 $3

  cd $pbpaste || return
}

function autogit(){
  cd /Users/Leina/Documents/PythonProgramming/NotesAutomation/ || return

  script_output=$(/Users/Leina/Documents/PythonProgramming/NotesAutomation/venv/bin/python3 gitRep.py "$1")
  echo $script_output


}


# source /Users/Leina/Documents/PythonProgramming/NotesAutomation/.my_commands.sh
# in order to call internal functions directly