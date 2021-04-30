#!/bin/bash

make autospec
make koji
sleep 120

make -C ../linux-tools bump
make -C ../linux-tools koji-nowait

make -C ../gdb bump
make -C ../gdb koji-nowait

make -C ../dropwatch bump
make -C ../dropwatch koji-nowait

cp binutils-stable-branch.patch ../mingw-binutils
cp REVISION ../mingw-binutils
pushd ../mingw-binutils
git commit -m "Stable branch update" binutils-stable-branch.patch REVISION
make bump
make koji-nowait
popd
