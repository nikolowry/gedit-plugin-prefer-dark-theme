#!/bin/sh

#Plugin Vars
pluginname="prefer-dark-theme"
pluginsdir="share/gedit/plugins"

#Src dir
src="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$pluginname"

#Dest dir
if [ $(id -u) = "0" ]; then
    #if root
    dest="/usr/$pluginsdir"
else
    #if user
    dest="$HOME/.local/$pluginsdir"
fi

#Install
cp -avr $src $dest
