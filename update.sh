#!/bin/bash

git commit -m "Stable branch update" binutils-stable-branch.patch
make autospec
make koji
sleep 120

make -C ../linux-tools bump
make -C ../linux-tools koji

make -C ../gdb bump
make -C ../gdb koji-nowait
