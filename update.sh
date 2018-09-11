#!/usr/bin/bash
git commit -m "stable branch update" binutils-stable-branch.patch
make bump
make koji-nowait
