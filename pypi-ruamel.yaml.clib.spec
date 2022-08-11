#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ruamel.yaml.clib
Version  : 0.2.6
Release  : 26
URL      : https://files.pythonhosted.org/packages/8b/25/08e5ad2431a028d0723ca5540b3af6a32f58f25e83c6dda4d0fcef7288a3/ruamel.yaml.clib-0.2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/25/08e5ad2431a028d0723ca5540b3af6a32f58f25e83c6dda4d0fcef7288a3/ruamel.yaml.clib-0.2.6.tar.gz
Summary  : C version of reader, parser and emitter for ruamel.yaml derived from libyaml
Group    : Development/Tools
License  : MIT
Requires: pypi-ruamel.yaml.clib-filemap = %{version}-%{release}
Requires: pypi-ruamel.yaml.clib-lib = %{version}-%{release}
Requires: pypi-ruamel.yaml.clib-license = %{version}-%{release}
Requires: pypi-ruamel.yaml.clib-python = %{version}-%{release}
Requires: pypi-ruamel.yaml.clib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
ruamel.yaml.clib
        ================
        
        ``ruamel.yaml.clib`` is the C based reader/scanner and emitter for ruamel.yaml

%package filemap
Summary: filemap components for the pypi-ruamel.yaml.clib package.
Group: Default

%description filemap
filemap components for the pypi-ruamel.yaml.clib package.


%package lib
Summary: lib components for the pypi-ruamel.yaml.clib package.
Group: Libraries
Requires: pypi-ruamel.yaml.clib-license = %{version}-%{release}
Requires: pypi-ruamel.yaml.clib-filemap = %{version}-%{release}

%description lib
lib components for the pypi-ruamel.yaml.clib package.


%package license
Summary: license components for the pypi-ruamel.yaml.clib package.
Group: Default

%description license
license components for the pypi-ruamel.yaml.clib package.


%package python
Summary: python components for the pypi-ruamel.yaml.clib package.
Group: Default
Requires: pypi-ruamel.yaml.clib-python3 = %{version}-%{release}

%description python
python components for the pypi-ruamel.yaml.clib package.


%package python3
Summary: python3 components for the pypi-ruamel.yaml.clib package.
Group: Default
Requires: pypi-ruamel.yaml.clib-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(ruamel.yaml.clib)

%description python3
python3 components for the pypi-ruamel.yaml.clib package.


%prep
%setup -q -n ruamel.yaml.clib-0.2.6
cd %{_builddir}/ruamel.yaml.clib-0.2.6
pushd ..
cp -a ruamel.yaml.clib-0.2.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656405761
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ruamel.yaml.clib
cp %{_builddir}/ruamel.yaml.clib-0.2.6/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ruamel.yaml.clib/f209babee9d393d099223687d6a44b7725097cd1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-ruamel.yaml.clib

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ruamel.yaml.clib/f209babee9d393d099223687d6a44b7725097cd1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
