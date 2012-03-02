Name:           sparkleshare
Version:        0.8.0
Release:        4%{?dist}
Summary:        Easy file sharing based on git repositories

Group:          Applications/Productivity
License:        GPLv3
URL:            http://www.sparkleshare.org/
Source0:        https://github.com/downloads/hbons/SparkleShare/%{name}-%{version}.tar.gz

BuildRequires:  mono-devel
BuildRequires:  ndesk-dbus-devel
BuildRequires:  ndesk-dbus-glib-devel
BuildRequires:  notify-sharp-devel
BuildRequires:  desktop-file-utils
BuildRequires:  intltool 
BuildRequires:  gnome-doc-utils
BuildRequires:  nant
BuildRequires:  webkit-sharp-devel
BuildRequires:  nautilus-python-devel >= 1.1
BuildRequires:  gettext
Requires:       git
Requires:       yelp
Requires:       nautilus-python >= 1.1

ExclusiveArch:  %{mono_arches}


#https://fedoraproject.org/wiki/Packaging:Mono#Empty_debuginfo
%global debug_package %{nil}


%description
Easy file sharing based on git repositories. A special folder is setup and
directories/files placed within are placed in a git-based version control
system and synchronized elsewhere.


%prep
%setup -q


%build
#disable user help because of a bug
#https://github.com/hbons/SparkleShare/issues/557
%configure --prefix=/usr --disable-user-help
GMCS_FLAGS=-codepage:utf8 make


%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/nautilus-python/extensions/%{name}-nautilus3-extension*
%defattr(0644,root,root,0755)
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/icons/hicolor/16x16/apps/folder-%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/folder-%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/folder-%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/folder-%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/folder-%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/folder-%{name}.png
%{_datadir}/icons/hicolor/24x24/status/process-syncing-%{name}-i*.png
%doc AUTHORS LICENSE NEWS



%changelog
* Fri Mar 02 2012 Dan Horák <dan[at]danny.cz> 0.8.0-4
- set ExclusiveArch

* Thu Mar 01 2012 Nikos Roussos <nikos@autoverse.net> 0.8.0-3
- added nautilus-python as dependency

* Tue Feb 14 2012 Nikos Roussos <nikos@autoverse.net> 0.8.0-2
- gettext added as buildrequirement, permissions error fixes

* Tue Feb 01 2012 Nikos Roussos <nikos@autoverse.net> 0.8.0-1
- Update to 0.8.0

* Wed Jun 29 2011 fedora@alexhudson.com - 0.2.4-1
- rebuilt for new upstrema 0.2.4

* Wed Jun 15 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.2-1
- rebuilt for new upstream 0.2.2

* Wed Jun 08 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.1-1
- rebuilt for new upstream 0.2.1

* Tue Jun 07 2011 Alex Hudson - 0.2.0-1
- initial release of 0.2!

* Sat May 21 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.beta2rc2-3
- remove nautilus extension for now; causes segfaults in F15 :(

* Fri May 20 2011 Alex Hudson <fedora@alexhudson.com> - 0.2.beta2rc2-2
- rebuilt to address python errors in F15

* Fri Mar 25 2011 Alex Hudson - 0.2.beta2rc1-1
- Initial build of 0.2rc1

* Mon Nov 22 2010 Alex Hudson - 0.2.beta1-7
- rebuilt

* Sat Nov 20 2010 Alex Hudson - 0.2.beta1-3
- rebuilt

* Thu Sep 02 2010 Alex Hudson - 0.2.alpha2-5
- update from git; now includes end-user help

* Tue Aug 17 2010 Alex Hudson - 0.2.alpha2-4
- now includes man page and new icons

* Mon Aug 16 2010 Alex Hudson - 0.2.alpha2-3
- slightly cleaner wrt. rpmlint

* Sat Aug 07 2010 Alex Hudson - 0.2.alpha1-2
- various fixes from git post-alpha release

* Tue Aug 03 2010 Alex Hudson - 0.2.alpha1-1
- Initial release of the 0.2alpha series of SparkleShare

