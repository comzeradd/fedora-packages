%global _hardened_build 1

Name:           qtkeychain
Version:        0.7.0
Release:        1%{?dist}
Summary:        A password store library

License:        BSD
Url:            https://github.com/frankosterfeld/qtkeychain
Source0:        https://github.com/frankosterfeld/qtkeychain/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  qt5-linguist

%description
The qtkeychain library allows you to store passwords easy and secure.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development files for qtkeychain.

%package qt5
Summary:        A password store library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description qt5
The qt5keychain library allows you to store passwords easy and secure.

%package qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
%description qt5-devel
This package contains development files for qt5keychain.


%prep
%setup -q

%build
mkdir build
pushd build
%cmake .. \
    -DBUILD_WITH_QT4:BOOL=ON \
    -DCMAKE_BUILD_TYPE=Release

make %{?_smp_mflags}
popd

mkdir build-qt5
pushd build-qt5
%cmake .. \
    -DBUILD_WITH_QT4:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=Release

make %{?_smp_mflags}
popd


%install
make install DESTDIR=%{buildroot} -C build-qt5
make install DESTDIR=%{buildroot} -C build

%find_lang %{name} --with-qt

grep %{_qt4_translationdir} %{name}.lang > %{name}-qt4.lang
grep %{_qt5_translationdir} %{name}.lang > %{name}-qt5.lang


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}-qt4.lang
%doc ReadMe.txt
%license COPYING
%{_libdir}/libqtkeychain.so.0*

%files devel
%{_includedir}/qtkeychain/
%{_libdir}/cmake/QtKeychain/
%{_libdir}/libqtkeychain.so*

%post qt5 -p /sbin/ldconfig
%postun qt5 -p /sbin/ldconfig

%files qt5 -f %{name}-qt5.lang
%doc ReadMe.txt
%license COPYING
%{_libdir}/libqt5keychain.so*

%files qt5-devel
%{_includedir}/qt5keychain/
%{_libdir}/cmake/Qt5Keychain/
%{_libdir}/libqt5keychain.so


%changelog
* Mon May 23 2016 nikos roussos <comzeradd@fedoraproject.org> 0.7.0-1
- update to 0.7.0

* Sun May 22 2016 Nikos Roussos <comzeradd@fedoraproject.org> 0.6.2-2
- Bump release

* Thu Apr 28 2016 Nikos Roussos <comzeradd@fedoraproject.org> 0.6.2-1
- update to 0.6.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-1
- qtkeychain-0.5.0 (#1136285), enable Qt5 support

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-6.20140405git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.90-5.20140405git
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-4.20140405git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-3.20140405git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Rex Dieter <rdieter@fedoraproject.org> 0.3.90-2.20140405git
- track libqtkeychain soname
- use %%find_lang
- omit dup'd cmake defines

* Sun May 04 2014 <jmarrero@fedoraproject.org> 0.3.90-1
- Update to latest github commit.

* Sun Mar 16 2014 <jmarrero@fedoraproject.org> 0.3.0-1
- Update to latest upstream version

* Tue Jan 07 2014 <jmarrero@fedoraproject.org> 0.1.0-4.20130805git
- Remove gcc-c++ dep
- Fix Requires
- Remove unneeded line in devel description
- Leave black line between changelogs

* Sat Jan 04 2014 <jmarrero@fedoraproject.org> 0.1.0-3.20130805git
- Fix Version and Release
- Fix %%files devel's cmake ownership by pointing the subfiles 
- Fix Changelog to reflect version and release changes 

* Tue Dec 24 2013 <jmarrero@fedoraproject.org> 0.1.0-2.20130805git
- Fix descriptions

* Mon Dec 23 2013 <jmarrero@fedoraproject.org> 0.1.0-1.20130805git
- Initial Packaging
