#!/bin/bash
set -e -o pipefail

BINUTILS_GIT=~/git/binutils-gdb
BINUTILS_VER=2.38

BINUTILS_TAG="binutils-${BINUTILS_VER}"
BINUTILS_BRANCH=origin/binutils-$(echo "${BINUTILS_VER}" | sed -re "s|([0-9]+)\.([0-9]+)(\.[0-9]+)?|\1_\2|")-branch

[ -d "$BINUTILS_GIT" ] || git clone https://sourceware.org/git/binutils-gdb.git "$BINUTILS_GIT"
git -C "$BINUTILS_GIT" remote update -p
git -C "$BINUTILS_GIT" rev-parse --verify --quiet refs/tags/"${BINUTILS_TAG}" > /dev/null
git -C "$BINUTILS_GIT" rev-parse --verify --quiet "$BINUTILS_BRANCH" > /dev/null
git -C "$BINUTILS_GIT" shortlog "${BINUTILS_TAG}".."${BINUTILS_BRANCH}" -- . ':!/bfd/version.h' ':!/bfd/development.sh' ':!/src-release.sh' > new.patch~
git -C "$BINUTILS_GIT" diff "${BINUTILS_TAG}".."${BINUTILS_BRANCH}" -- . ':!/bfd/version.h' ':!/bfd/development.sh' ':!/src-release.sh' >> new.patch~
diff binutils-stable-branch.patch new.patch~ > /dev/null && rm new.patch~ && exit
mv new.patch~ binutils-stable-branch.patch
git -C "$BINUTILS_GIT" describe --abbrev=10 --match 'binutils-*' "$BINUTILS_BRANCH" > REVISION
git commit -m "stable update to `cat REVISION`" -a
make autospec CLEANUP=1
make koji
nvr=$(rpmspec --srpm --query --queryformat='%{NVR}\n' binutils.spec)
koji wait-repo --build=$nvr dist-clear-build

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
