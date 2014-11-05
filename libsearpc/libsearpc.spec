%global commit 8998e7b2c5587f0b94c48db24e2952d08def5add

Name:           libsearpc
Version:        3.0
Release:        2%{?dist}
Summary:        A simple and easy-to-use C language RPC framework

License:        GPLv3
URL:            https://github.com/haiwen/%{name}
Source0:        https://github.com/haiwen/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  jansson-devel


%description
Searpc is a simple C language RPC framework based on GObject system. Searpc
handles the serialization/deserialization part of RPC, the transport part is
left to users.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       jansson-devel >= 2.2.1


%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -qn %{name}-%{commit}
sed -i -e /\(DESTDIR\)/d %{name}.pc.in


%build
./autogen.sh
%configure --disable-static --disable-compile-demo
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README.markdown
%{_libdir}/%{name}.so.*
%{_bindir}/searpc-codegen.py
%{python_sitearch}/pysearpc/

%files devel
%{_includedir}/searpc*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-2
- Update to latest tag
- Remove merged patch

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-1
- Initial version of the package
