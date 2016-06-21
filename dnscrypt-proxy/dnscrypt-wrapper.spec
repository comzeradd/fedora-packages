Name:       dnscrypt-wrapper
Version:    0.2
Release:    1%{?dist}
Summary:    DNSCrypt server

Group:      System Environment/Daemons
License:    GPLv2
URL:        http://dnscrypt.org/
Source0:    https://github.com/Cofyc/%{name}/archive/v%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  libevent-devel
BuildRequires:  libsodium-devel


%description
DNSCrypt is a protocol that authenticates communications between a DNS
client and a DNS resolver. It prevents DNS spoofing. It uses cryptographic
signatures to verify that responses originate from the chosen DNS resolver
and haven't been tampered with.


%prep
%setup -n %{name}-%{version} -q


%build
make configure
%configure --prefix=/usr
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_sbindir}
install -d -m 755  %{buildroot}/%{_sbindir}
install -p dnscrypt-wrapper %{buildroot}/%{_sbindir}


%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}


%changelog
* Sat Oct 24 2015 Nikos Roussos <comzeradd@fedoraproject.org>
- Update to 0.2

* Fri Oct 23 2015 Evaggelos Balaskas <Evaggelos _AT_ Balaskas _DOT_ GR>
- Initial package

