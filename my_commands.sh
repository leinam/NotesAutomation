#!/bin/bash
# define type of script

function nfe() {
  pwd | pbcopy

  cd /Users/Leina/Documents/PythonProgramming/NotesAutomation || return
  python notes.py $1 $2 $3

  cd $pbpaste || return
}

function autogit(){
  cd /Users/Leina/Documents/PythonProgramming/ || return

  mkdir "$1"
  cd "$1" || return


  touch me.txt

  git init
  git add .

  git commit -m "testing.. testing"

  /Users/Leina/Documents/PythonProgramming/NotesAutomation/venv/bin/python3 /Users/Leina/Documents/PythonProgramming/NotesAutomation/gitRep.py "$1"
  # paste text from clipboard (remote URL) to variable
  origin=$(pbpaste)

  # add remote using above URL and push committed(versioned files)
  git remote add origin "$origin"
  git push -u origin master

  # go back to parent directory
  cd ../
}


# source /Users/Leina/Documents/PythonProgramming/NotesAutomation/.my_commands.sh
# in order to call internal functions directly