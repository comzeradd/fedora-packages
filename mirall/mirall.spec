Name:           mirall
Version:        1.5.4
Release:        4%{?dist}
License:        GPLv2+
Summary:        The ownCloud Client
Url:            http://owncloud.org/sync-clients/
Source0:        http://download.owncloud.com/desktop/stable/%{name}-%{version}.tar.bz2
Patch0:         %{name}-1.5.3-syslibs.patch

BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qtwebkit-devel
BuildRequires:  neon-devel
BuildRequires:  qtkeychain-devel >= 0.3.0
BuildRequires:  check
BuildRequires:  doxygen
BuildRequires:  sqlite-devel
BuildRequires:  python-sphinx
BuildRequires:  qtlockedfile-devel
BuildRequires:  qtsingleapplication-devel

Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Provides:       owncloud-client = %{version}-%{release}

Obsoletes: mirall < 1.5.2
Obsoletes: owncloud-client < 1.5.2
Obsoletes: owncloud-csync < 1.5.2
Obsoletes: owncloud-csync-plugin-smb < 0.70
Obsoletes: owncloud-csync-plugin-sftp < 0.91
Obsoletes: owncloud-csync-plugin-owncloud < 0.91

%description
Mirall owncloud-client enables you to connect to your private
ownCloud Server. With it you can create folders in your home
directory, and keep the contents of those folders synced with your
ownCloud server. Simply copy a file into the directory and the
ownCloud Client does the rest.

%package common
Summary: common files for mirall and owncloud-client
Obsoletes: owncloud-csync-libs < 1.5.2

%description common
provides common files for mirall and owncloud-client
such as the configurationfile that determines the excluded files
in a sync.

%package devel
Summary: Development files for mirall
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Obsoletes: owncloud-csync-devel < 1.5.2

%description devel
Development headers for use of the mirall library

%package -n owncloud-client
Summary: owncloud Standalone client
Requires: %{name}-common%{?_isa} = %{version}-%{release}

%description -n owncloud-client
The ownCloud desktop client, lets you sync directly to your ownCloud server.

%prep
%setup -q %{name}-%{version}
%patch0 -p1
rm -r src/3rdparty/qtlockedfile src/3rdparty/qtsingleapplication

%build
mkdir build
pushd build
%cmake .. -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"
make %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=%{buildroot}
popd
%find_lang %{name} --with-qt

%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null
    gtk-update-icon-cache -f %{_datadir}/icons/hicolor &> /dev/null || :
fi

%post common -p /sbin/ldconfig

%postun common -p /sbin/ldconfig


%files -f %{name}.lang
%{_bindir}/owncloud
%{_bindir}/owncloudcmd
%{_datadir}/applications/owncloud.desktop
%{_datadir}/icons/hicolor/48x48/apps/owncloud.png
%{_datadir}/icons/hicolor/128x128/apps/owncloud.png
%{_datadir}/icons/hicolor/22x22/apps/owncloud.png
%{_datadir}/icons/hicolor/32x32/apps/owncloud.png
%{_datadir}/icons/hicolor/64x64/apps/owncloud.png

%files common
%{_libdir}/libowncloudsync.so.0
%{_libdir}/libowncloudsync.so.%{version}
%{_libdir}/libocsync.so.*

%doc README.md COPYING
%config  %{_sysconfdir}/ownCloud/sync-exclude.lst

%files devel
%{_libdir}/libowncloudsync.so
%{_includedir}/owncloudsync/
%{_libdir}/libowncloudsync.so
%{_libdir}/libhttpbf.a
%{_libdir}/libocsync.so
%{_includedir}/httpbf.h

%changelog
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Rex Dieter <rdieter@fedoraproject.org> 1.5.4-2
- drop hard-coded Requires: neon, qtkeychain, let rpm autodeps handle it
- drop BR: gcc-c++
- -devel: tighten subpkg dep

* Mon May 05 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4
* Thu Mar 20 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.5.3-3
- Use system qtlockedfile and qtsingleapplication instead of bundled ones
* Wed Mar 19 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.3-2
- Updated Obsoletes for each subpackage
* Sun Mar 16 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.3-1
- Update to latest Upstream version
- Merge owncloud-csync and mirall as upstream has done

* Thu Jan 09 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.0-2
- Add requires owncloud-csync-libs
* Tue Jan 07 2014 Joseph Marrero <jmarrero@fedoraproject.org> - 1.5.0-1
- Update to latest upstream release
* Sun Dec 29 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.4.2-4
- Build with $RPM_OPT_FLAGS.
- Move ldconfig scriptlets to -common.
* Thu Nov 14 2013 <jmarrero@fedoraproject.org> 1.4.2-3
- Add Requires neon as noted by Manuel Faux
- Add backported patch created by Klass Freitag backported by Manuel Faux
* Tue Nov 12 2013 <jmarrero@fedoraproject.org> 1.4.2-2
- Add BuildRequires neon-devel
* Sat Oct 26 2013 <jmarrero@fedoraproject.org> 1.4.2-1
- Update to version 1.4.2
* Fri Oct 04 2013 <jmarrero@fedoraproject.org> 1.4.1-1
- Update to version 1.4.1
* Wed Sep 04 2013 <jmarrero@fedoraproject.org> 1.4.0-2
- Add qtwebkit-devel dependency
* Wed Sep 04 2013 <jmarrero@fedoraproject.org> 1.4.0-1
- Update to version 1.4.0
- Update URL
* Sun Aug 18 2013 <jmarrero@fedoraproject.org> 1.4.0beta2-1
- Update to testing version 1.4.0beta2
* Wed Jun 26 2013 <jmarrero@fedoraproject.org> 1.3.0-1
- Update to version 1.3.0
* Thu May 23 2013 <jmarrero@fedoraproject.org> 1.3.0beta1-1
- Update to testing version 1.3.0beta1
* Tue Apr 23 2013 <jmarrero@fedoraproject.org> 1.2.5-1
- Update to upstream version 1.2.5
* Thu Apr 11 2013 <jmarrero@fedoraproject.org> 1.2.4-1
- Update to uptream version 1.2.4
* Wed Apr 03 2013 <jmarrero@fedoraproject.org> 1.2.3-1
- remove plasma client files as is not officially merged uptream
- Update to 1.2.3 uptream version
* Tue Mar 05 2013 <jmarrero@fedoraproject.org> 1.2.2-2
- plasma client files fix
* Tue Mar 05 2013 <jmarrero@fedoraproject.org> 1.2.2-1
- add new Plasma client package
* Sat Mar 02 2013 <jmarrero@fedoraproject.org> 1.2.1-2
- moved libowncloudsync.so* to common as it is now used by mirall and owncloud-client
- re-added mirall .desktop launcher
* Sat Mar 02 2013 <jmarrero@fedoraproject.org> 1.2.1-1
- Update to 1.2.1
* Sat Jan 26 2013 <jmarrero@fedoraproject.org> 1.2.0-1
- Update to 1.2.0
* Sat Jan 19 2013 <jmarrero@fedoraproject.org> 1.2.0beta2-1
- update to 1.2.0beta2
* Fri Dec 21 2012 <jmarrero@fedoraproject.org> 1.2.0beta1-1
- Update to 1.2.0beta1
* Thu Dec 20 2012 <jmarrero@fedoraproject.org> 1.1.4-1
- Update to 1.1.4
* Tue Dec 04 2012 <jmarrero@fedoraproject.org> 1.1.3-1
- Update to 1.1.3
* Fri Oct 19 2012 <jmarrero@fedoraproject.org> 1.1.1-1
- Update to 1.1.1
* Mon Oct 15 2012 <jmarrero@fedoraproject.org> 1.1.0-2
- fix mirall-common dependency problem
* Sun Oct 14 2012 <jmarrero@fedoraproject.org> 1.1.0-1
- Version Upgrade to 1.1.0
- Removed the need to look for occsync now mirall looks for ocsync the new name of owncloud-csync
* Mon Aug 20 2012 <jmarrero@fedoraproject.org> 1.0.5-4
- removed unesesary cmake flags
* Fri Aug 17 2012 <jmarrero@fedoraproject.org> 1.0.5-3
- added icon scriplets for owncloud-client icons
- moved %%doc to mirall-common
- Added cmake  dcSYNC_INCLUDE_PATH:PATH=_includedir}/occsync and dc SYNC_LIBRARY:PATH=_libdir}/liboccsync.so to have mirall look for occsync instead of csync
- Removed uneeded dep
- Changelog corrections and clean up
* Thu Aug 16 2012 <jmarrero@fedoraproject.org> 1.0.5-2
- Divided mirall into mirall-common, mirall and owncloud-client
- Added dcMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed
- moved exclude.lst back to /etc/, the apps look for it there
- fixed icons descriptions
- added refresh icon cache
- updated csync dep to owncloud-csync
* Sat Aug 11 2012 <jmarrero@fedoraproject.org> 1.0.5-1
- Update to 1.0.5
- drop defattr
- remove not-needed dependencies
- changelog cleanup
- moved exclude.lst to /etc/mirall/
- fixed source01 and source 02 (icons)
* Sat Aug 11 2012 <jmarrero@fedoraproject.org> 1.0.4-2
- added mirall icon and smp flags plus code cleanup
* Sat Aug 11 2012 <jmarrero@fedoraproject.org> 1.0.4-1
- Initial try
