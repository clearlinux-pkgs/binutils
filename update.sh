#!/bin/bash

make autospec
make koji
nvr=$(rpmspec --srpm --query --queryformat='%{NVR}\n' binutils.spec)
koji wait-repo --build=$nvr dist-clear-build || exit 1

for pkg in linux-tools gdb dropwatch; do
	make -C ../$pkg bump
	make -C ../$pkg koji-nowait
done

pkg=mingw-binutils
patch=binutils-stable-branch.patch
spec=mingw-binutils.spec

cp $patch ../$pkg
cp REVISION ../$pkg
pushd ../$pkg
make bumpnogit
git commit -m "Stable branch update" $spec $patch release REVISION
make koji-nowait
popd
