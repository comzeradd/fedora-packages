Name:           openclipart
Version:        2.0
Release:        1%{?dist}
Summary:        Open Clip Art Library

Group:          Applications/Publishing
License:        Public Domain
URL:            http://www.openclipart.org/
Source0:        http://www.openclipart.org/downloads/%{version}/openclipart-%{version}-svgonly.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  dos2unix
BuildArch:      noarch

%description
Open Clip Art Gallery contains thousand of SVG vector images that can be
freely used.  SVG files can be opened in various tools including
Inkscape vector graphics editor, OpenOffice.org and Firefox web browser.


%prep
%setup -q -n openclipart-%{version}-svgonly
find . -name '*.svg' -exec dos2unix -k -q '{}' \;


%build


%install
rm -rf $RPM_BUILD_ROOT
# Bundled makefile messes things up horribly,
# (copies unnecessary files including vim backups and doesn't
# handle spaces in names though they are actually present in-tree)
cd clipart
find . -name '*.svg' -exec sh -c '
        DIR="$RPM_BUILD_ROOT/%{_datadir}/clipart/%{name}/$(dirname "{}")";
        install -d "$DIR";
        install -m 644 "{}" "$DIR"' \;


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/clipart
%doc AUTHORS LICENSE ChangeLog NEWS README VERSION


%changelog
* Mon Mar 17 2014 Nikos Roussos <comzeradd@fedoraproject.org> 2.0-1
- Update to 2.0

* Sat Aug 10 2013 Nikos Roussos <comzeradd@fedoraproject.org> 0.18-9
- Fix description typo

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.18-1
- Initial packaging attempt
