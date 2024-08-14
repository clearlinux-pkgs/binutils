#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x13FCEF89DD9E3C4F (nickc@redhat.com)
#
Name     : binutils
Version  : 2.43
Release  : 549
URL      : https://mirrors.kernel.org/gnu/binutils/binutils-2.43.tar.xz
Source0  : https://mirrors.kernel.org/gnu/binutils/binutils-2.43.tar.xz
Source1  : https://mirrors.kernel.org/gnu/binutils/binutils-2.43.tar.xz.sig
Source2  : 13FCEF89DD9E3C4F.pkey
Summary  : zlib compression library
Group    : Development/Tools
License  : BSL-1.0 GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: clr-optimized-link-scripts
BuildRequires : expect
BuildRequires : glibc-staticdev
BuildRequires : gnupg
BuildRequires : lz4-dev
BuildRequires : lzo-dev
BuildRequires : zlib-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: binutils-stable-branch.patch
Patch2: binutils-add-LD_AS_NEEDED-global-env.patch
Patch3: v1-0001-Add-env-variable-as-fallback-linker-script-arg.patch
Patch4: v1-0002-gold-Add-env-variable-support.patch
Patch5: v1-0003-Add-support-for-ordering-maps.patch
Patch6: v1-0004-Removing-trailing-spaces-newline-from-mapped-scri.patch
Patch7: v1-0005-Ignore-version-from-.so-match.patch
Patch8: v1-0006-Add-support-for-target-filtering.patch
Patch9: v1-0007-With-text-ordering-file-support.patch
Patch10: v1-0008-ld-gold-Support-alignment-for-functions.patch
Patch11: binutils-apx.patch

%description
This directory contains various GNU compilers, assemblers, linkers,
debuggers, etc., plus their support routines, definitions, and documentation.

%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 13FCEF89DD9E3C4F' gpg.status
%setup -q -n binutils-2.43
cd %{_builddir}/binutils-2.43
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
pushd ..
cp -a binutils-2.43 buildavx2
popd

%build
## build_prepend content
rm -rf gdb libdecnumber readline sim
export SOURCE_DATE_EPOCH=1549215809
sed -i -e "s/#define BFD_VERSION_DATE.*/#define BFD_VERSION_DATE 20190203/g" bfd/version.h

# Force all man pages to regenerate... they were truncated in the 2.37 release
touch binutils/doc/binutils.texi
touch gas/doc/as.texi
touch gprof/gprof.texi
touch ld/ld.texi


# relro costs quite a bit for compile time
export CFLAGS="$CFLAGS -Wl,-z,norelro  -g1 -gno-column-info -gno-variable-location-views -gz"
export CXXFLAGS="$CXXFLAGS -Wl,-z,norelro  -g1 -gno-column-info -gno-variable-location-views -gz"

# Do not use a macro - breaks toolchain
./configure \
--prefix=/usr \
--libdir=/usr/lib64 \
--includedir=/usr/include \
--with-lib-path=/usr/lib64:/usr/lib32:/usr/lib \
--enable-shared --disable-static \
--target=x86_64-generic-linux \
--build=x86_64-generic-linux \
--enable-targets=all \
--enable-deterministic-archives \
--enable-lto \
--enable-plugins \
--enable-gold \
--enable-secureplt \
--disable-werror \
--enable-64-bit-bfd \
--with-system-zlib \
--without-debuginfod
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723234427
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}  -O tooldir=/usr

pushd ../buildavx2
## build_prepend content
rm -rf gdb libdecnumber readline sim
export SOURCE_DATE_EPOCH=1549215809
sed -i -e "s/#define BFD_VERSION_DATE.*/#define BFD_VERSION_DATE 20190203/g" bfd/version.h

# Force all man pages to regenerate... they were truncated in the 2.37 release
touch binutils/doc/binutils.texi
touch gas/doc/as.texi
touch gprof/gprof.texi
touch ld/ld.texi


# relro costs quite a bit for compile time
export CFLAGS="$CFLAGS -Wl,-z,norelro  -g1 -gno-column-info -gno-variable-location-views -gz"
export CXXFLAGS="$CXXFLAGS -Wl,-z,norelro  -g1 -gno-column-info -gno-variable-location-views -gz"

# Do not use a macro - breaks toolchain
./configure \
--prefix=/usr \
--libdir=/usr/lib64 \
--includedir=/usr/include \
--with-lib-path=/usr/lib64:/usr/lib32:/usr/lib \
--enable-shared --disable-static \
--target=x86_64-generic-linux \
--build=x86_64-generic-linux \
--enable-targets=all \
--enable-deterministic-archives \
--enable-lto \
--enable-plugins \
--enable-gold \
--enable-secureplt \
--disable-werror \
--enable-64-bit-bfd \
--with-system-zlib \
--without-debuginfod
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}  -O tooldir=/usr
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_flags} -O check tooldir=/usr || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723234427
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/binutils
cp %{_builddir}/binutils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/binutils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/binutils-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/binutils/0e8e850b0580fbaaa0872326cb1b8ad6adda9b0d || :
cp %{_builddir}/binutils-%{version}/COPYING3 %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/binutils-%{version}/COPYING3.LIB %{buildroot}/usr/share/package-licenses/binutils/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9 || :
cp %{_builddir}/binutils-%{version}/bfd/COPYING %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/binutils-%{version}/gas/COPYING %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/binutils-%{version}/include/COPYING %{buildroot}/usr/share/package-licenses/binutils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/binutils-%{version}/include/COPYING3 %{buildroot}/usr/share/package-licenses/binutils/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/binutils-%{version}/libiberty/COPYING.LIB %{buildroot}/usr/share/package-licenses/binutils/597bf5f9c0904bd6c48ac3a3527685818d11246d || :
cp %{_builddir}/binutils-%{version}/zlib/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/binutils/892b34f7865d90a6f949f50d95e49625a10bc7f0 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3 tooldir=/usr
popd
GOAMD64=v2
%make_install tooldir=/usr
## Remove excluded files
rm -f %{buildroot}*/usr/bin/dlltool
rm -f %{buildroot}*/usr/bin/windres
rm -f %{buildroot}*/usr/lib/ldscripts/i386pe.x
rm -f %{buildroot}*/usr/lib/ldscripts/i386pe.xa
rm -f %{buildroot}*/usr/lib/ldscripts/i386pe.xbn
rm -f %{buildroot}*/usr/lib/ldscripts/i386pe.xe
rm -f %{buildroot}*/usr/lib/ldscripts/i386pe.xn
rm -f %{buildroot}*/usr/lib/ldscripts/i386pe.xr
rm -f %{buildroot}*/usr/lib/ldscripts/i386pe.xu
rm -f %{buildroot}*/usr/lib/ldscripts/i386pep.x
rm -f %{buildroot}*/usr/lib/ldscripts/i386pep.xa
rm -f %{buildroot}*/usr/lib/ldscripts/i386pep.xbn
rm -f %{buildroot}*/usr/lib/ldscripts/i386pep.xe
rm -f %{buildroot}*/usr/lib/ldscripts/i386pep.xn
rm -f %{buildroot}*/usr/lib/ldscripts/i386pep.xr
rm -f %{buildroot}*/usr/lib/ldscripts/i386pep.xu
rm -f %{buildroot}*/usr/etc/gprofng.rc
## install_append content
install -d %{buildroot}/usr/include

# Manually install libiberty - can be fixed post glibc/gcc fixups
install -m 0644 libiberty/libiberty.a %{buildroot}/usr/lib64

# Find out who is using these headers and reduce their usage.
install -m 644 include/ansidecl.h %{buildroot}/usr/include/
install -m 644 include/libiberty.h %{buildroot}/usr/include/
install -m 644 include/plugin-api.h %{buildroot}/usr/include/

install -d %{buildroot}/usr/include/libiberty
install -m 644 include/*.h %{buildroot}/usr/include/libiberty/

install -d %{buildroot}/usr/lib64/gcc/x86_64-generic-linux/12/
cp -a %{buildroot}/usr/bin/as %{buildroot}/usr/lib64/gcc/x86_64-generic-linux/12/as
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
