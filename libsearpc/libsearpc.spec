%global _hardened_build 1

Name:           libsearpc
Version:        3.0.7
Release:        1%{?dist}
Summary:        A simple and easy-to-use C language RPC framework

License:        LGPLv3
URL:            https://github.com/haiwen/%{name}
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glib2-devel
BuildRequires:  jansson-devel
BuildRequires:  pygobject2
BuildRequires:  python-simplejson


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
%setup -qn %{name}-%{version}
sed -i -e /\(DESTDIR\)/d %{name}.pc.in


%build
./autogen.sh
%configure --disable-static --disable-compile-demo
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"


%install
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
%{__make} check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS README.markdown
%license COPYING
%{_libdir}/%{name}.so.*
%{_bindir}/searpc-codegen.py
%{python_sitearch}/pysearpc/

%files devel
%license COPYING
%{_includedir}/searpc*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Feb 02 2016 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0.7-1
- Update to 3.0.7

* Fri Dec 04 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-6
- Add optflags

* Fri Sep 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-5
- Fix license

* Fri Sep 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-4
- Fix license
- Fix build requiremets
- Add check

* Sat Apr 11 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-3
- Use release tag instead of commit

* Wed Nov 05 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-2
- Update to latest tag
- Remove merged patch

* Tue Aug 12 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 3.0-1
- Initial version of the package
