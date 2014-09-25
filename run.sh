for file in $*; 
   do 
    rm -rf result/*.*;
    python2.7 openCVTest01.py $file;
    python2.7 openCVTest02.py $file;
    python2.7 openCVTest03.py $file;
    #sh runall.sh $file;
   done