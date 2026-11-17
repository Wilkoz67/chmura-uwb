#!/usr/bin/env bash
# Pomocnik: wypisuje polecenie, wykonuje je i dopisuje polecenie + wynik do dowody/polecenia-lstk.txt
LOG="$(dirname "$0")/../dowody/polecenia-lstk.txt"
{
  echo "\$ $*"
  "$@" 2>&1 | grep -v -e "File association not found" -e "No AWS profile found"
  echo
} | tee -a "$LOG"
