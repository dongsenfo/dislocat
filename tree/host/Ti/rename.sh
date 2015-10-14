#!/bin/bash
for i in $(ls); do
	cd $i
	mv Ti__$i Ti__$i.pot
	cd ..
done
