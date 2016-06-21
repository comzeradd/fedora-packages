%global confdir %{_sysconfdir}/postfix

Name:              postgrey
Version:           1.36
Release:           1%{?dist}
# File headers only state "GNU GPL", but the LICENSE sections state v2 and "any
# later version"
Summary:           Postfix Greylisting Policy Server
License:           GPLv2+
URL:               http://postgrey.schweikert.ch/
Source0:           http://postgrey.schweikert.ch/pub/postgrey-%{version}.tar.gz
Source1:           postgrey.service
Source2:           README-rpm
Source3:           postgrey.sysconfig
Patch0:            postgrey-1.28-group.patch
Patch1:            postgrey-1.34-perl-5.18.patch
BuildArch:         noarch
BuildRequires:     perl-podlators
BuildRequires:     systemd
Requires:          perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
#Requires:          perl(BerkeleyDB)
#Requires:          perl(Fcntl)
#Requires:          perl(Getopt::Long)
#Requires:          perl(IO::Multiplex)
#Requires:          perl(Net::DNS)
#Requires:          perl(Net::Server)
#Requires:          perl(Pod::Usage)
#Requires:          perl(POSIX)
#Requires:          perl(strict)
#Requires:          perl(Sys::Hostname)
#Requires:          perl(Sys::Syslog)
# We require postfix for its directories and gid
Requires:          postfix
Requires(pre):     shadow-utils
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Postgrey is a Postfix policy server implementing greylisting. When a request
for delivery of a mail is received by Postfix via SMTP, the triplet CLIENT_IP /
SENDER / RECIPIENT is built. If it is the first time that this triplet is
seen, or if the triplet was first seen less than 5 minutes, then the mail gets
rejected with a temporary error. Hopefully spammers or viruses will not try
again later, as it is however required per RFC.

%prep
%setup -q
%patch0 -p1 -b .group
%patch1 -p1 -b .perl-5.18
install -pm0644 %{SOURCE2} README-rpm

%build
# We only have perl scripts, so just "build" the man page
pod2man \
    --center="Postgrey Policy Server for Postfix" \
    --section="8" \
    postgrey > postgrey.8

%install
# Configuration files
mkdir -p %{buildroot}%{confdir}
install -pm0644 postgrey_whitelist_{clients,recipients} \
    %{buildroot}%{confdir}/
# Local whitelist file
echo "# Clients that should not be greylisted.  See postgrey(8)." \
    > %{buildroot}%{confdir}/postgrey_whitelist_clients.local

# Main script
install -pDm0755 postgrey %{buildroot}%{_sbindir}/postgrey

# Spool directory
mkdir -p %{buildroot}%{_localstatedir}/spool/postfix/postgrey

# Init script
install -pDm0644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/postgrey.service

# Sysconfig
install -pDm0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/sysconfig/postgrey

# Man page
install -pDm0644 postgrey.8 \
    %{buildroot}%{_mandir}/man8/postgrey.8

# Optional report script
install -pDm0755 contrib/postgreyreport \
    %{buildroot}%{_sbindir}/postgreyreport

%pre
getent group postgrey >/dev/null || groupadd -r postgrey
getent passwd postgrey >/dev/null || \
    useradd -r -g postgrey -d %{_localstatedir}/spool/postfix/postgrey -s /sbin/nologin \
    -c "Postfix Greylisting Service" postgrey
exit 0

%post
%systemd_post postgrey.service

%preun
%systemd_preun postgrey.service

%postun
%systemd_postun postgrey.service

%triggerun -- postgrey < 1.34-3
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply postgrey
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save postgrey >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del postgrey >/dev/null 2>&1 || :
/bin/systemctl try-restart postgrey.service >/dev/null 2>&1 || :

%files
%doc Changes COPYING README README-rpm
%{_unitdir}/postgrey.service
%{_sysconfdir}/sysconfig/postgrey
%config(noreplace) %{confdir}/postgrey_whitelist_clients
%config(noreplace) %{confdir}/postgrey_whitelist_recipients
%config(noreplace) %{confdir}/postgrey_whitelist_clients.local
%{_sbindir}/postgrey
%{_sbindir}/postgreyreport
%{_mandir}/man8/postgrey.8*
%dir %attr(0751,postgrey,postfix) %{_localstatedir}/spool/postfix/postgrey/

%changelog
* Thu Oct 01 2015 Nikos Roussos <comzeradd@fedoraproject.org> - 1.36-1
- Update to 1.36

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-16
- Perl 5.22 rebuild

* Fri Nov 07 2014 Petr Pisar <ppisar@redhat.com> - 1.34-15
- Build-require perl-podlators for pod2man (bug #1161477)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-14
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Christopher Meng <rpm@cicku.me> - 1.34-12
- Correct the syntax of systemd unit to support option with space-separated content.

* Tue Jan 21 2014 Christopher Meng <rpm@cicku.me> - 1.34-11
- Let perl magic determine the dependencies.
- Fix systemd unit typo.

* Tue Jan 14 2014 Christopher Meng <rpm@cicku.me> - 1.34-10
- Fix typo in the SPEC.

* Sun Jan 12 2014 Christopher Meng <rpm@cicku.me> - 1.34-9
- Update systemd service unit to be more powerful.
- SPEC cleanup(BZ#850279).
- Add missing dependencies(BZ#1039355).

* Wed Jan 01 2014 Nils Philippsen <nils@redhat.com> - 1.34-8
- make postgrey work with perl 5.18 (#1039551)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.34-6
- Perl 5.18 rebuild
- Build-require systemd-units

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 20 2012 Jon Ciesla <limburgher@gmail.com> - 1.34-3
- Migrate to systemd, BZ 714430.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun  7 2011 Matthias Saou <http://freshrpms.net/> 1.34-1
- Update to 1.34.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Matthias Saou <http://freshrpms.net/> 1.32-1
- Update to 1.32.
- Update init script to the new style.
- Slightly update README-rpm instructions.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 22 2008 Matthias Saou <http://freshrpms.net/> 1.31-1
- Update to 1.31.

* Mon Aug  6 2007 Matthias Saou <http://freshrpms.net/> 1.30-1
- Update to 1.30.
- Update License field.

* Fri Jun 22 2007 Matthias Saou <http://freshrpms.net/> 1.28-1
- Update to 1.28.
- Update URL to the new homepage.

* Mon Feb 12 2007 Matthias Saou <http://freshrpms.net/> 1.27-4
- Silence %%setup.
- Fix init script mode in the srpm.
- Remove explicit perl(IO::Multiplex) requirement, not needed on FC6 (but
  probably still on RHEL4).
- Add a comment line to the empty local whitelist file.

* Mon Dec  4 2006 Matthias Saou <http://freshrpms.net/> 1.27-3
- Add man page generation (Mike Wohlgemuth).

* Fri Dec  1 2006 Matthias Saou <http://freshrpms.net/> 1.27-2
- Include postgreyreport script.

* Mon Nov  6 2006 Matthias Saou <http://freshrpms.net/> 1.27-1
- Spec file cleanup.

* Wed Jan 18 2006 Levente Farkas <lfarkas@lfarkas.org> 1.24
- some minor changes thanks to Peter Bieringer <pb@bieringer.de>

* Mon Jan 16 2006 Levente Farkas <lfarkas@lfarkas.org> 1.24
- upgrade to 1.24

* Sun Nov 13 2005 Levente Farkas <lfarkas@lfarkas.org> 1.22
- upgrade to 1.22

* Mon Aug 22 2005 Levente Farkas <lfarkas@lfarkas.org> 1.21
- spec file update from Luigi Iotti <luigi@iotti.biz>

* Thu Apr 28 2005 Levente Farkas <lfarkas@lfarkas.org> 1.21
- update to 1.21

* Tue Mar  8 2005 Levente Farkas <lfarkas@lfarkas.org> 1.18
- update to 1.18

* Tue Dec 14 2004 Levente Farkas <lfarkas@lfarkas.org> 1.17
- update to 1.17

* Wed Jul 14 2004 Levente Farkas <lfarkas@lfarkas.org> 1.14
- guard the pre and post scripts

* Wed Jul  7 2004 Levente Farkas <lfarkas@lfarkas.org> 1.13
- initial release 1.13

