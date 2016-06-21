%global _hardened_build 1

Name:           ccnet
Version:        5.1.2
Release:        1%{?dist}
Summary:        A framework for writing networked applications in C

License:        GPLv3
URL:            https://github.com/haiwen/%{name}
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}-server.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  libevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  libsearpc-devel
BuildRequires:  libzdb-devel
BuildRequires:  python2-devel
BuildRequires:  vala


%description
Ccnet is a framework for writing networked applications in C. It provides the
following basic services:

* Peer identification
* Connection Management
* Service invocation
* Message sending

In ccnet network, there are two types of nodes, i.e., client and server.
Server has the following functions:

* User management
* Group management
* Cluster management


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       libevent-devel
Requires:       libsearpc-devel


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qn %{name}-%{version}-server
sed -i -e /\(DESTDIR\)/d libccnet.pc.in


%build
./autogen.sh --enable-server --enable-client
%configure --disable-static --disable-compile-demo
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"


%install
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
%{__make} check


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc COPYRIGHT HACKING README.markdown
%license LICENCE.txt
%{_libdir}/libccnet.so.*
%{_bindir}/%{name}*
%{python2_sitearch}/%{name}


%files devel
%license LICENCE.txt
%{_includedir}/*
%{_libdir}/libccnet.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Sat May 14 2016 Julien Enselme <jujens@jujens.eu> - 5.1.2-1
- Update to 5.1.2

* Tue Feb 02 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5

* Thu Dec 03 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0
- Add license to devel subpackage
- Add optflags
- Add libzdb-devel requirement
- Add python2-devel requirement
- unused-direct-shlib-dependency

* Wed Sep 16 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- Hardened build

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
