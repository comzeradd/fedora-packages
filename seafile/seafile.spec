%global commit c81b8c8ef32dae6ae9b8cc9d3a2bb8cbada08c13

Name:           seafile
Version:        3.1.8
Release:        1%{?dist}
Summary:        Cloud storage system

License:        GPLv3
URL:            http://seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  glib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  libevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  ccnet-devel
BuildRequires:  vala


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
%setup -qn %{name}-%{commit}
sed -i -e /\(DESTDIR\)/d lib/libseafile.pc.in


%build
./autogen.sh
%configure --disable-static --disable-server --enable-client --disable-fuse
make


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name 'seafile.desktop' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc LICENCE.txt README.markdown
%{_libdir}/*
%{python_sitearch}/%{name}/
%{python_sitearch}/seaserv/
%{_bindir}/seaf-cli
%{_bindir}/seaf-daemon
%{_bindir}/%{name}
%{_mandir}/man1/*.1.gz


%files devel
%{_includedir}/%{name}/
%{_libdir}/*
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Thu Aug 28 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
