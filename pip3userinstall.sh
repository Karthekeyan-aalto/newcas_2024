#!/usr/bin/env bash
#############################################################################
# This is the script to install TheSyDeKick dependencies for the user 
# 
# Created by Marko Kosunen, 2017
# Modified for PCSystem use April 18,2022
#############################################################################
##Function to display help with -h argument and to control 
##The configuration from the command line
help_f()
{
cat << EOF
 PIP3USERINSTALL Release 1.0 (16.01.2020)
 TheSyDeKick dependency installer
 Written by Marko Pikkis Kosunen

 SYNOPSIS
   pip3userinstall.sh [OPTIONS]
 DESCRIPTION
   Installs required Python packages locally to users ~/.local
 OPTIONS
   -u  
       Upgrade also the existing packages. 
       Default: just install the missing ones.
   -h
       Show this help.
EOF
}
PIP="pip3 install --user"
UPGRADE=""
while getopts uh opt
do
  case "$opt" in
    u) UPGRADE="--upgrade";;
    h) help_f; exit 0;;
    \?) help_f; exit 0;;
  esac
  shift
done

#Installs the missing python modules locally with pip3
PACKAGES="\
    wheel \
    gnureadline \
    numpy \
    numpydoc \
    matplotlib \
    joblib \
    scipy \
    pandas \
    sphinx \
    sphinx_rtd_theme \
    PyQt5 \
    pyelftools \
    sortedcontainers \
    bitstring \
    openpyxl \
    xlrd \
    torch \
"

for package in ${PACKAGES}; do
    echo "Installing ${package}"
    ${PIP} ${UPGRADE} ${package}
done

exit 0

