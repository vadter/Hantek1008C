To get it work you need to install python 3, the pyusb, overrides, matplotlib and pyqtgraph libraries for scripts with the appropriate names (I use it under conda environment conda-forge).

Ubuntu: copy 60-hantek-1008C.rules to /lib/udev/rules.d/ and reboot.

A variant of only the 8-channel operation mode has been implemented.
Sample rate is set from 300 ksamples / s to 5 ksamples / s. Channels are placed in the middle of the range (~ 2048 / 4096 bit). There is a problem with offset (it is not solved).

Driver was made on the basis of https://github.com/mfg92/hantek1008py
