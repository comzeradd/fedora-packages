%global _hardened_build 1

Name:           seafile-client
Version:        5.1.1
Release:        3%{?dist}
Summary:        Seafile cloud storage desktop client

License:        ASL 2.0
URL:            https://www.seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz
Source1:        %{name}.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake
BuildRequires:  sqlite-devel
BuildRequires:  jansson-devel
BuildRequires:  openssl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libsearpc-devel
BuildRequires:  ccnet-devel
BuildRequires:  seafile-devel
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-devel


%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.


%prep
%setup -qn %{name}-%{version}


%build
%cmake -DUSE_QT5=ON -DCMAKE_BUILD_TYPE=Release .
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/seafile.desktop
mkdir -p %{buildroot}%{_datarootdir}/appdata/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc README.md
%license LICENSE
%{_bindir}/seafile-applet
%{_datadir}/applications/seafile.desktop
%{_datadir}/icons/hicolor/scalable/apps/seafile.svg
%{_datadir}/icons/hicolor/16x16/apps/seafile.png
%{_datadir}/icons/hicolor/22x22/apps/seafile.png
%{_datadir}/icons/hicolor/24x24/apps/seafile.png
%{_datadir}/icons/hicolor/32x32/apps/seafile.png
%{_datadir}/icons/hicolor/48x48/apps/seafile.png
%{_datadir}/icons/hicolor/128x128/apps/seafile.png
%{_datadir}/pixmaps/seafile.png
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Fri Jun 03 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.1-3
- Update icons cache

* Fri Jun 03 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.1-2
- Use https for upstream url
- Add appdata file

* Wed Jun 01 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.1-1
- Update to 5.1.1
- Switch to qt5

* Mon Feb 08 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4

* Wed Sep 16 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- Hardened build

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
