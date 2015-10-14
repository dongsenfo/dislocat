#!/bin/bash
for i in $(ls); do
	cd ~/fall15/defect/CONC/host/Mg
	cd $i
	rm ./Ti__*
	cd ~/fall15/defect/PSEUDOS/potpaw_PBE.52
	cat Ti_sv/POTCAR $i/POTCAR > Mg__$i.pot
	mv Mg__$i.pot ~/fall15/defect/CONC/host/Mg/$i
done
