%global _hardened_build 1

Name:           seafile
Version:        5.1.2
Release:        3%{?dist}
Summary:        Cloud storage cli client

License:        GPLv2
URL:            http://seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}-server.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  glib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libcurl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libzdb-devel
BuildRequires:  fuse-devel >= 2.7.3
BuildRequires:  ccnet-devel == %{version}
BuildRequires:  vala
BuildRequires:  python2-devel
BuildRequires:  libevent-devel
BuildRequires:  jansson-devel


%description
Seafile is a next-generation open source cloud storage system with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team. 


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qn %{name}-%{version}-server
sed -i -e /\(DESTDIR\)/d lib/libseafile.pc.in


%build
./autogen.sh
%configure --disable-static
make CFLAGS="%{optflags}" %{?_smp_mflags} 


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name 'seafile.desktop' -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig


%files
%doc README.markdown
%license LICENSE.txt
%{python2_sitearch}/%{name}/
%{python2_sitearch}/seaserv/
%{_libdir}/lib%{name}.so.*
%{_bindir}/seaf-cli
%{_bindir}/seaf-daemon
%{_mandir}/man1/*.1.*


%files devel
%doc README.markdown
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Tue May 31 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.2-3
- Fix license

* Fri May 27 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.2-2
- Fix shared libraries

* Tue May 17 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2
- Add missing requiremnts
- Add missing license file from subpackage
- Add tests

* Mon Feb 08 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5

* Wed Sep 16 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- Hardened build

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Thu Aug 28 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
