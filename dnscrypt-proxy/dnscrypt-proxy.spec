%global _hardened_build 1

Name:       dnscrypt-proxy
Version:    1.6.1
Release:    3%{?dist}
Summary:    DNSCrypt client

Group:      System Environment/Daemons
License:    MIT
URL:        https://dnscrypt.org/
Source0:    https://github.com/jedisct1/%{name}/archive/%{version}.tar.gz
Patch0:     dnscrypt-proxy-1.6.1-libtool-obsolete-macro.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  gettext-devel
BuildRequires:  libevent-devel
BuildRequires:  libsodium-devel


%description
DNSCrypt is a protocol that authenticates communications between a DNS
client and a DNS resolver. It prevents DNS spoofing. It uses cryptographic
signatures to verify that responses originate from the chosen DNS resolver
and haven't been tampered with.


%prep
%setup -n %{name}-%{version} -q
%patch0 -p1


%build
./autogen.sh
%configure --prefix=/usr --disable-static
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/hostip
%{_sbindir}/%{name}
%{_usr}/share/%{name}
%{_mandir}/man8/%{name}*
%{_mandir}/man8/hostip*


%changelog
* Mon Jun 06 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.1-3
- Fix license

* Mon Jun 06 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.1-2
- Add hardened flag
- Fix obsolete m4 macro

* Fri Apr 22 2016 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.1-1
- Update to 1.6.1

* Sat Oct 24 2015 Nikos Roussos <comzeradd@fedoraproject.org> 1.6.0-1
- Initial package
