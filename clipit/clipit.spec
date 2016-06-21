Name:           clipit
Version:        1.4.2
Release:        9%{?dist}
Summary:        A lightweight, fully featured GTK+ clipboard manager

Group:          User Interface/Desktops
License:        GPLv3+
URL:            http://clipit.rspwn.com/
Source0:        http://downloads.sourceforge.net/gtk%{name}/%{name}-%{version}.tar.gz
# clipit doesn't autostart in MATE
# Fixed upstream but not yet merged
Source1:        %{name}.appdata.xml
Patch0:         %{name}-%{version}-mate.patch
Patch1:         %{name}-%{version}-epel.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtk2-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libappstream-glib
Requires: xdotool

%description
ClipIt is a lightweight, fully featured GTK+ clipboard manager. It was forked
from Parcellite, adding additional features and bug-fixes to the project.
ClipIts main features are:
* Save a history of your last copied items
* Search through the history
* Global hot-keys for most used functions
* Execute actions with clipboard items
* Exclude specific items from history


%prep
%setup -q
%if 0%{?fedora}
%patch0 -p1 -b .orig
%else
%patch1 -p1 -b .orig
%endif

%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-install --delete-original \
    --remove-category=Application \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --delete-original \
    --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
    %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
mkdir -p %{buildroot}%{_datadir}/appdata/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%check
appstream-util validate-relax %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%clean
rm -rf %{buildroot}


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
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/icons/hicolor/scalable/apps/%{name}-trayicon.svg
%{_datadir}/applications/%{name}.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Mon Dec 15 2014 Nikos Roussos <nikos@autoverse.net> 1.4.2-9
- Fix appdata syntax

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Nikos Roussos <nikos@autoverse.net> 1.4.2-6
- Add EPEL support

* Thu Sep 12 2013 Nikos Roussos <nikos@autoverse.net> 1.4.2-5
- Fix MATE autostart. Add appdata

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Nikos Roussos <nikos@autoverse.net> 1.4.2-1
- Update to 1.4.2

* Wed Feb 29 2012 Nikos Roussos <nikos@autoverse.net> 1.4.1-5
- Fix gtk+ inclusion bug, see patch1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Nikos Roussos <nikos@autoverse.net> 1.4.1-3
- Fixed dependency missing, de translation bug, desktop icon bug

* Fri Jul 01 2011 Nikos Roussos <nikos@autoverse.net> 1.4.1-2
- Fixed config warning and more spec errors

* Wed Jun 01 2011 Nikos Roussos <nikos@autoverse.net> 1.4.1-1
- Initial Fedora RPM
