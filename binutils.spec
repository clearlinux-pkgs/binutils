# IMPORTANT NOTE: It is required to rebuild the linux-tools and cairo packages
# after a version change! These packages use "libbfd".
#

%define binutils_target %{_arch}-generic-linux

Name:           binutils
Version:        2.31
Release:        104
License:        GPL-3.0
Summary:        GNU binary utilities
Url:            http://www.gnu.org/software/binutils/
Group:          devel
Source0:        https://mirrors.kernel.org/gnu/binutils/binutils-2.31.tar.xz
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

Patch1:		binutils-stable-branch.patch
Patch2:         binutils-add-LD_AS_NEEDED-global-env.patch
Patch3:		handle-elf-compressed-align.patch
Patch4:		initialize-uncompressed_align_pow_p-to-0.patch
Patch5:		gold-get-alignment-of-uncompressed-section.patch

# CVEs

Patch101:      Add-recursion-limit-to-libiberty.patch
Patch102:      CVE-2018-18605.patch
Patch103:      CVE-2018-18606.patch
Patch104:      CVE-2018-18607.patch
Patch105:      CVE-2018-19932.patch
Patch106:      CVE-2018-20002.patch
Patch107:      CVE-2018-1000876.patch

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


%package extras
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          libs

%description extras
GNU binary utilities.



%prep
%setup -q -n binutils-2.31

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# CVEs
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1

rm -rf gdb libdecnumber readline sim

%build
export SOURCE_DATE_EPOCH=1502738392
sed -i -e "s/#define BFD_VERSION_DATE.*/#define BFD_VERSION_DATE 20180922/g" bfd/version.h
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
/usr/bin/ar
/usr/bin/addr2line
/usr/bin/c++filt
/usr/bin/elfedit
/usr/bin/gprof
/usr/bin/ld
/usr/bin/nm
/usr/bin/as
/usr/bin/readelf
/usr/bin/strip
/usr/bin/objdump
/usr/bin/objcopy
/usr/bin/ranlib
/usr/bin/size
/usr/bin/strings
/usr/bin/ld.bfd
/usr/lib64/libopcodes-*.*.so
/usr/lib64/libbfd-*.*.so
/usr/bin/dwp
/usr/lib/ldscripts
/usr/bin/dlltool
/usr/bin/dllwrap
/usr/bin/windmc
/usr/bin/windres

%files extras
/usr/bin/ld.gold

%files -n binutils-dev
/usr/include/libiberty.h
/usr/include/ansidecl.h
/usr/include/dis-asm.h
/usr/include/symcat.h
/usr/include/bfdlink.h
/usr/include/bfd.h
/usr/include/plugin-api.h
/usr/include/libiberty/
/usr/include/diagnostics.h
/usr/lib64/libiberty.a
/usr/lib64/libbfd.so
/usr/lib64/libopcodes.so

%files -n binutils-doc
/usr/share/man/man1/objdump.1
/usr/share/man/man1/gprof.1
/usr/share/man/man1/as.1
/usr/share/man/man1/size.1
/usr/share/man/man1/nm.1
/usr/share/man/man1/addr2line.1
/usr/share/man/man1/strings.1
/usr/share/man/man1/elfedit.1
/usr/share/man/man1/strip.1
/usr/share/man/man1/windmc.1
/usr/share/man/man1/objcopy.1
/usr/share/man/man1/ar.1
/usr/share/man/man1/ld.1
/usr/share/man/man1/windres.1
/usr/share/man/man1/ranlib.1
/usr/share/man/man1/readelf.1
/usr/share/man/man1/c++filt.1
/usr/share/man/man1/dlltool.1
/usr/share/info/bfd.info
/usr/share/info/binutils.info
/usr/share/info/as.info
/usr/share/info/ld.info
/usr/share/info/gprof.info

%files -n binutils-locale -f %{name}.lang
