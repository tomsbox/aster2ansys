ansys2aster
=============
The objective of this project is to calculate
an ansys mechanical input file (.dat) with code aster.


Aster@Docker
============

* https://code-aster.org/forum2/viewtopic.php?id=23453
* https://github.com/tianyikillua/code_aster_on_docker
 
Start docker and bind local directory
-------------------------------------
* C:/Users/../aster2ansys/docker_volume is the directory where you have to put your files
* docker run -ti --rm -v C:/Users/../aster2ansys/docker_volume:/home/aster/shared -w /home/aster/shared quay.io/tianyikillua/code_aster
* as_run test.export