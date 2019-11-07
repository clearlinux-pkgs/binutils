#!/bin/bash

git commit -m "Stable branch update" binutils-stable-branch.patch
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
pushd ../mingw-binutils &> /dev/bull
git commit -m "Stable branch update" binutils-stable-branch.patch
make autospec
make koji-nowait
popd
