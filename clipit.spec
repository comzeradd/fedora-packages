Name:           clipit
Version:        1.4.1
Release:        5%{?dist}
Summary:        A lightweight, fully featured GTK+ clipboard manager

Group:          User Interface/Desktops
License:        GPLv3+
URL:            http://clipit.rspwn.com/
Source0:        http://downloads.sourceforge.net/gtk%{name}/%{name}-%{version}.tar.gz
# patch fixing German translation inconsistency
# http://sf.net/tracker/?func=detail&aid=3367028&group_id=369179&atid=1538558
Patch0:         clipit-1.4.1-de.po.patch
# pacth fixing wrong gtk header inclusion
# http://sf.net/tracker/?func=detail&aid=3495659&group_id=369179&atid=1538558
# https://live.gnome.org/GnomeGoals/CleanupGTKIncludes
Patch1:         clipit-1.4.1-glib.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gtk2-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: gettext
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
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig


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


%changelog
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
