Name:           openclipart
Version:        0.18
Release:        6%{?dist}
Summary:        Open Clip Art Library

License:        Public Domain
URL:            http://www.openclipart.org/
Source0:        http://www.openclipart.org/downloads/%{version}/openclipart-%{version}-svgonly.tar.bz2

BuildRequires:  dos2unix
BuildArch:      noarch

%description
Open Clip Art Gallery contains thousand of SVG vector images that can be
freely used.  SVG files can be opened in various tools including
Inkscape vector graphics editor, OpenOffice.org and Firefox web nrowser.


%prep
%setup -q -n openclipart-%{version}-svgonly
find . -name '*.svg' -exec dos2unix -k -q '{}' \;


%build


%install
# Bundled makefile messes things up horribly,
# (copies unnecessary files including vim backups and doesn't
# handle spaces in names though they are actually present in-tree)
cd clipart
find . -name '*.svg' -exec sh -c '
        DIR="$RPM_BUILD_ROOT/%{_datadir}/clipart/%{name}/$(dirname "{}")";
        install -d "$DIR";
        install -m 644 "{}" "$DIR"' \;


%files
%{_datadir}/clipart
%doc AUTHORS LICENSE ChangeLog NEWS README VERSION


%changelog
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
