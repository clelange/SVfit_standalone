SVfit_standalone
================

SVfit algorithm for tau pair mass reconstruction (stand-alone version)

To build, it's convenient to set up a `CMSSW` release, here `CMSSW_8_0_23`, in parallel to the clone of the repository:
```
cmsrel CMSSW_8_0_23
cd CMSSW_8_0_23/src
cmsenv
```

Clone this repository and change to the `SVfit_standalone` directory.
```
mkdir build
cd build
cmake ../ -DCMAKE_INSTALL_PREFIX=../svFit
make -j4
make test ARGS="--output-on-failure"
make install
```

Now you should have the shared library `libSVfitStandaloneAlgorithm.so` and dictionary in the `../svFit` directory. To be able to load the library, you need to extend the `LD_LIBRARY_PATH`:
```
export LD_LIBRARY_PATH=${PWD}../svFit/lib:${LD_LIBRARY_PATH}
```
This export is needed whenever you open a new shell.
