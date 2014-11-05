%global commit 2b29f489d316e1d2faee0642242d9ddce2b21ae0

Name:           seafile-client
Version:        3.1.4
Release:        1%{?dist}
Summary:        Seafile cloud storage desktop client

License:        ASL 2.0
URL:            http://seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 2.6
BuildRequires:  qt4-devel
BuildRequires:  sqlite-devel
BuildRequires:  jansson-devel
BuildRequires:  openssl-devel
BuildRequires:  libsearpc-devel
BuildRequires:  ccnet-devel
BuildRequires:  seafile-devel
BuildRequires:  qtwebkit-devel


%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.


%prep
%setup -qn %{name}-%{commit}


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_SYSTEM_NAME=Linux .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/seafile.desktop


%files
%doc LICENSE README.md
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


%changelog
* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
