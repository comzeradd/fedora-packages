Name:           libshout-idjc
Version:        2.3.1
Release:        1%{?dist}
Summary:        Icecast source streaming library modified for IDJC

License:        LGPLv2+
URL:            http://idjc.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/idjc/%{name}/%{name}-%{version}.tar.gz


BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libtheora-devel
BuildRequires:  speex-devel

%description
The libshout is a library for communicating with and sending data to an icecast
server.  It handles the socket connection, the timing of the data, and prevents
most bad data from getting to the icecast server. libshout-idjc is a modified
version of libshout library with extra functionality needed by idjc.

%package        devel
Summary:        static libraries and header files for %{name} development
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

Requires:       libogg-devel
Requires:       libvorbis-devel
Requires:       libtheora-devel
Requires:       speex-devel

%description    devel
The libshout-idjc-devel package contains the header files needed for developing
applications that send data to an icecast server. Install libshout-idjc-devel
if you want to develop applications using libshout-idjc.


%prep
%setup -q


%build
%configure --disable-static
# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm -rf %{buildroot}/%{_docdir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING NEWS README
%{_libdir}/libshout-idjc.so.*


%files devel
%{_libdir}/libshout-idjc.so
%{_libdir}/pkgconfig/shout-idjc.pc
%dir %{_includedir}/shoutidjc/
%{_includedir}/shoutidjc/shout.h


%changelog
* Sat May 11 2013 Nikos Roussos <comzeradd@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Sat Dec 01 2012 Nikos Roussos <comzeradd@fedoraproject.org> - 2.3.0-1
- Initial RPM release for this fork

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2.2-3
- Autorebuild for GCC 4.3

* Fri Dec  7 2007 kwizart < kwizart at gmail.com > - 2.2.2-2
- Fix http://bugzilla.redhat.com/415121
- Add disable-static
- Don't use makeinstall macro
- Update License field

* Thu Sep 07 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2.2-1
- updated to new release

* Fri Mar 17 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2-3
- add Requires: to -devel package

* Fri Mar 17 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2-2
- rebuild to please the extras repository

* Fri Mar 10 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.2-1
- new (incompatible) version, but deps are updated
- various cleanups

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0.9-4
- rebuild on all arches

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.9-3
- Include headers directory entry in -devel package.

* Sat Feb 26 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.9-2
- Remove redundant explicit /sbin/ldconfig dependency.

* Wed Jun 04 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.0.9-0.fdr.1: initial RPM release
