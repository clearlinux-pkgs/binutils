# IMPORTANT NOTE: It is required to rebuild the linux-tools and cairo packages
# after a version change! These packages use "libbfd".
#

%define binutils_target %{_arch}-generic-linux

Name:           binutils
Version:        2.29.1
Release:        55
License:        GPL-3.0
Summary:        GNU binary utilities
Url:            http://www.gnu.org/software/binutils/
Group:          devel
Source0:        https://ftp.gnu.org/gnu/binutils/binutils-2.29.1.tar.xz
BuildRequires:  flex
BuildRequires:  libstdc++-dev
BuildRequires:  dejagnu
BuildRequires:  expect
BuildRequires:  tcl
BuildRequires:  glibc-staticdev
BuildRequires:  zlib-dev
BuildRequires:  texinfo
BuildRequires:  bison
Requires:	binutils-doc

#Patch1:         switch-build-flow-to-production.patch
Patch2:         binutils-add-LD_AS_NEEDED-global-env.patch

# CVEs
Patch101:   cve-2017-16826.patch
Patch102:   cve-2017-16827.patch
Patch103:   cve-2017-16829.patch
Patch104:   cve-2017-16832.patch
Patch105:   cve-2017-16828.patch
Patch106:   cve-2017-16828-2.patch
Patch107:   cve-2017-16830.patch
Patch108:   cve-2017-16831.patch
Patch109:   cve-2017-16831-2.patch
Patch110:   cve-2017-17121.patch
Patch111:   cve-2017-17122.patch
Patch112:   cve-2017-17123.patch
Patch113:   cve-2017-17124.patch
Patch114:   cve-2017-17125.patch
Patch115:   cve-2017-17126.patch
Patch116:   cve-2017-17080.patch


%description
GNU binary utilities.

%package -n binutils-dev
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          devel
Provides: binutils-devel

%description -n binutils-dev
GNU binary utilities.

%package -n binutils-doc
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          doc

%description -n binutils-doc
GNU binary utilities.

%package -n binutils-locale
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          libs

%description -n binutils-locale
GNU binary utilities.

%prep
%setup -q -n binutils-2.29.1

#%patch1 -p1
%patch2 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1


rm -rf gdb libdecnumber readline sim

%build
export SOURCE_DATE_EPOCH=1502738392
# Do not use a macro - breaks toolchain
./configure --prefix=/usr \
    --enable-shared --disable-static \
    --target=%{binutils_target} \
    --build=%{binutils_target} \
    --libdir=/usr/lib64 \
    --includedir=/usr/include \
    --enable-deterministic-archives \
    --enable-lto \
    --enable-plugins \
    --enable-gold \
    --enable-secureplt \
    --with-lib-path=/usr/lib64:/usr/lib32:/usr/lib \
    --enable-targets=i386-linux,x86_64-linux,x86_64-pc-mingw64 \
    --disable-werror
make %{?_smp_flags} tooldir=/usr

%check
make %{?_smp_flags} check tooldir=/usr || :

%install
export SOURCE_DATE_EPOCH=1502738392
make %{?_smp_flags} tooldir=/usr DESTDIR=%{buildroot} install
install -d %{buildroot}%{_prefix}/include

# Manually install libiberty - can be fixed post glibc/gcc fixups
install -m 0644 libiberty/libiberty.a %{buildroot}%{_libdir}/

# Find out who is using these headers and reduce their usage.
install -m 644 include/ansidecl.h %{buildroot}%{_includedir}/
install -m 644 include/libiberty.h %{buildroot}%{_prefix}/include
install -m 644 include/plugin-api.h %{buildroot}%{_includedir}/
install -d %{buildroot}%{_includedir}/libiberty
install -m 644 include/*.h %{buildroot}%{_includedir}/libiberty/


# no .la files please
rm -f %{buildroot}/usr/lib64/*.la 

%find_lang %{name} bin.lang
%find_lang bfd bfd.lang
%find_lang gas gas.lang
%find_lang gprof gprof.lang
%find_lang ld ld.lang
%find_lang opcodes opcodes.lang
%find_lang gold gold.lang
cat *.lang > %{name}.lang

%files
%{_bindir}/ar
%{_bindir}/addr2line
%{_bindir}/c++filt
%{_bindir}/elfedit
%{_bindir}/gprof
%{_bindir}/ld
%{_bindir}/nm
%{_bindir}/as
%{_bindir}/readelf
%{_bindir}/strip
%{_bindir}/objdump
%{_bindir}/objcopy
%{_bindir}/ranlib
%{_bindir}/size
%{_bindir}/strings
%{_bindir}/ld.bfd
%{_libdir}/libopcodes-*.*.so
%{_libdir}/libbfd-*.*.so
/usr/bin/dwp
/usr/bin/ld.gold
/usr/lib/ldscripts
/usr/bin/dlltool
/usr/bin/dllwrap
/usr/bin/windmc
/usr/bin/windres

%files -n binutils-dev
%{_libdir}/libbfd.so
%{_libdir}/libopcodes.so
%{_includedir}/libiberty.h
%{_includedir}/ansidecl.h
%{_includedir}/dis-asm.h
%{_includedir}/symcat.h
%{_includedir}/bfdlink.h
%{_includedir}/bfd.h
%{_includedir}/plugin-api.h
%{_includedir}/libiberty/
/usr/lib64/libiberty.a


%files -n binutils-doc
%{_mandir}/man1/objdump.1
%{_mandir}/man1/gprof.1
%{_mandir}/man1/as.1
%{_mandir}/man1/size.1
%{_mandir}/man1/nm.1
%{_mandir}/man1/addr2line.1
%{_mandir}/man1/strings.1
%{_mandir}/man1/elfedit.1
%{_mandir}/man1/strip.1
%{_mandir}/man1/windmc.1
%{_mandir}/man1/objcopy.1
%{_mandir}/man1/ar.1
%{_mandir}/man1/ld.1
%{_mandir}/man1/windres.1
%{_mandir}/man1/ranlib.1
%{_mandir}/man1/nlmconv.1
%{_mandir}/man1/readelf.1
%{_mandir}/man1/c++filt.1
%{_mandir}/man1/dlltool.1
%{_infodir}/bfd.info
%{_infodir}/binutils.info
%{_infodir}/as.info
%{_infodir}/ld.info
%{_infodir}/gprof.info

%files -n binutils-locale -f %{name}.lang
