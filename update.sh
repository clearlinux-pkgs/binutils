#!/usr/bin/bash
git commit -m "stable branch update" binutils-stable-branch.patch
make bump
make koji
sleep 120
pushd ../linux-tools
make bump
make koji-nowait
popd
pushd ../gdb
make bump
make koji-nowait
popd
