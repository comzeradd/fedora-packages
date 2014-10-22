Name:           idjc
Version:        0.8.14
Release:        1%{?dist}
Summary:        DJ application for streaming audio

License:        GPLv2+
URL:            http://idjc.sourceforge.net
Source0:       http://downloads.sourceforge.net/project/idjc/idjc/0.8/%{name}-%{version}.tar.gz
Source1:        %{name}-README.Fedora


BuildRequires:  pygtk2-devel
BuildRequires:  python-mutagen
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  speex-devel
BuildRequires:  flac-devel
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  libshout-idjc-devel
BuildRequires:  libmad-devel
BuildRequires:  lame-devel
BuildRequires:  libmpg123-devel
BuildRequires:  twolame-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  opus-devel
Requires:       python-mutagen
Requires:       pulseaudio-module-jack


%description
Internet DJ Console is a client for streaming live radio shows over the
Internet using Icecast or Shoutcast servers. It has a two panel playlist mode,
with automatic cross-fading. It uses jack as a back-end and it supports all
major free audio codecs.


%prep
%setup -q
cp %{SOURCE1} README.Fedora


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
desktop-file-install --delete-original \
    --remove-category=Application \
    --add-category="AudioVideo" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%{_bindir}/%{name}*
%{python_sitelib}/%{name}*
%{_libdir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*
%lang(fr) %{_mandir}/fr/man1/%{name}*
%{_datadir}/pixmaps/%{name}.png
%doc %{_docdir}/%{name}-%{version}/README.gz
%doc %{_docdir}/%{name}-%{version}/AUTHORS.gz
%doc %{_docdir}/%{name}-%{version}/ChangeLog.gz
%doc %{_docdir}/%{name}-%{version}/NEWS.gz
%doc COPYING README.Fedora doc/*.html doc/*.css doc/*.png


%changelog
* Mon May 19 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 0.8.14-1
- Update to 0.8.14

* Mon Jan 13 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 0.8.13-1
- Update to 0.8.13

* Sat Dec 01 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.8-1
- Update to 0.8.8

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 02 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.7-2
- fix valueerror bug

* Tue Jan 03 2012 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.7-1
- Update to 0.8.7

* Sun Dec 04 2011 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.6-4
- Added README.Fedora for codecs
- Changed category to Multimedia
- Added AudioVideo category to desktop file

* Mon Nov 28 2011 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.6-3
- Added pulseaudio module dependency
- Added html documentation

* Tue Nov 22 2011 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.6-2
- Fix license error

* Thu Nov 17 2011 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.6-1
- Update to 0.8.6

* Sun May 08 2011 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.5-1
- Update to 0.8.5

* Mon Oct 25 2010 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.3-2
- Add patch to fix pythondir bug on x86_64

* Mon Oct 18 2010 Nikos Roussos <comzeradd@fedoraproject.org> 0.8.3-1
- Initial version of the package
