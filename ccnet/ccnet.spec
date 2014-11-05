%global commit 6b55658280da8c74d9a41fee7d0d0bc1cb7c8c5f

Name:           ccnet
Version:        3.1.4
Release:        1%{?dist}
Summary:        A framework for writing networked applications in C

License:        GPLv3
URL:            https://github.com/haiwen/%{name}
Source0:        https://github.com/haiwen/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  libevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  libsearpc-devel
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
%setup -qn %{name}-%{commit}
sed -i -e /\(DESTDIR\)/d libccnet.pc.in


%build
./autogen.sh
%configure --disable-static --disable-compile-demo
make


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc COPYRIGHT LICENCE.txt HACKING README.markdown
%{_libdir}/libccnet.so.*
%{_bindir}/%{name}*
%{python_sitearch}/%{name}


%files devel
%{_includedir}/*
%{_libdir}/libccnet.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.1.4-1
- Initial version of the package
