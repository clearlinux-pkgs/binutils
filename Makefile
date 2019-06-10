PKG_NAME := binutils
URL := https://mirrors.kernel.org/gnu/binutils/binutils-2.31.1.tar.xz
include ../common/Makefile.common

update:
	pushd ~/git/binutils-gdb ; git remote update -p ; git diff binutils-2_32..origin/binutils-2_32-branch  > ~/clear/packages/binutils/binutils-stable-branch.patch.in ; filterdiff  --exclude="*/bfd/version.h" ~/clear/packages/binutils/binutils-stable-branch.patch.in > ~/clear/packages/binutils/binutils-stable-branch.patch  ; rm ~/clear/packages/binutils/binutils-stable-branch.patch.in ; popd
	git diff --exit-code  binutils-stable-branch.patch || bash ./update.sh
