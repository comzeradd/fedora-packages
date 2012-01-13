Name:           idjc
Version:        0.8.6
Release:        5%{?dist}
Summary:        DJ application for streaming audio

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://idjc.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/idjc/idjc/0.8/%{name}-%{version}.tar.gz
Source1:        %{name}-README.Fedora
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pygtk2-devel
BuildRequires:  python-mutagen
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  speex-devel
BuildRequires:  flac-devel
BuildRequires:  desktop-file-utils
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
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
desktop-file-install --delete-original \
    --remove-category=Application \
    --add-category="AudioVideo" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}*
%{python_sitelib}/%{name}*
%attr(755,root,root) %{python_sitelib}/%{name}/mutagentagger.py
%{_datadir}/applications/%{name}.desktop
%{_prefix}/libexec/%{name}*
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}.png
%doc COPYING README AUTHORS ChangeLog NEWS README.Fedora doc/*.html doc/*.css doc/*.png


%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Nikos Roussos <nikos@autoverse.net> 0.8.6-4
- Added README.Fedora for codecs
- Changed category to Multimedia
- Added AudioVideo category to desktop file

* Mon Nov 28 2011 Nikos Roussos <nikos@autoverse.net> 0.8.6-3
- Added pulseaudio module dependency
- Added html documentation

* Tue Nov 22 2011 Nikos Roussos <nikos@autoverse.net> 0.8.6-2
- Fix license error

* Thu Nov 17 2011 Nikos Roussos <nikos@autoverse.net> 0.8.6-1
- Update to 0.8.6

* Mon May 08 2011 Nikos Roussos <nikos@autoverse.net> 0.8.5-1
- Update to 0.8.5

* Mon Oct 25 2010 Nikos Roussos <nikos@autoverse.net> 0.8.3-2
- Add patch to fix pythondir bug on x86_64

* Mon Oct 18 2010 Nikos Roussos <nikos@autoverse.net> 0.8.3-1
- Initial version of the package
