#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dnf
Version  : 2.7.3
Release  : 3
URL      : https://github.com/rpm-software-management/dnf/archive/2.7.3.tar.gz
Source0  : https://github.com/rpm-software-management/dnf/archive/2.7.3.tar.gz
Summary  : Package manager forked from Yum, using libsolv as a dependency resolver
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: dnf-bin
Requires: dnf-python3
Requires: dnf-config
Requires: dnf-locales
Requires: dnf-python
BuildRequires : cmake
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Package manager forked from Yum, using libsolv as a dependency resolver.

%package bin
Summary: bin components for the dnf package.
Group: Binaries
Requires: dnf-config

%description bin
bin components for the dnf package.


%package config
Summary: config components for the dnf package.
Group: Default

%description config
config components for the dnf package.


%package locales
Summary: locales components for the dnf package.
Group: Default

%description locales
locales components for the dnf package.


%package python
Summary: python components for the dnf package.
Group: Default
Requires: dnf-python3

%description python
python components for the dnf package.


%package python3
Summary: python3 components for the dnf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dnf package.


%prep
%setup -q -n dnf-2.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507316941
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DPYTHON_DESIRED="3" -DWITH_MAN=0
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1507316941
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang dnf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dnf-3
/usr/bin/dnf-automatic-3

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/dnf-automatic-download.service
%exclude /usr/lib/systemd/system/dnf-automatic-download.timer
%exclude /usr/lib/systemd/system/dnf-automatic-install.service
%exclude /usr/lib/systemd/system/dnf-automatic-install.timer
%exclude /usr/lib/systemd/system/dnf-automatic-notifyonly.service
%exclude /usr/lib/systemd/system/dnf-automatic-notifyonly.timer
%exclude /usr/lib/systemd/system/dnf-automatic.service
%exclude /usr/lib/systemd/system/dnf-automatic.timer
%exclude /usr/lib/systemd/system/dnf-makecache.service
%exclude /usr/lib/systemd/system/dnf-makecache.timer
/usr/lib/tmpfiles.d/dnf.conf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f dnf.lang
%defattr(-,root,root,-)

