Name:       ninja-ide
Version:    2.1.1
Release:    1
Summary:    Ninja IDE for Python development

Group:      Development/Tools
License:    GPLv3
URL:        http://www.ninja-ide.org/
Source0:    https://github.com/downloads/%{name}/%{name}/%{name}-v%{version}.zip
Source1:    %{name}.desktop

BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  PyQt4-devel
Requires:       PyQt4
Requires:       python-inotify
BuildArch:      noarch


%description
NINJA-IDE (from the recursive acronym: "Ninja-IDE Is Not Just Another IDE"),
is a cross-platform integrated development environment (IDE). NINJA-IDE runs
on Linux/X11, Mac OS X and Windows desktop operating systems, and allows
developers to create applications for several purposes using all the tools and
utilities of NINJA-IDE, making the task of writing software easier and more
enjoyable.


%prep
%setup -q -n %{name}


%build
%{__python} setup.py build


%install
install -Dm 755 icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}


%files
%defattr(-,root,root,-)
%{python_sitelib}/ninja_ide/
%{python_sitelib}/ninja_tests/
%{python_sitelib}/NINJA_IDE-2.1.1-py2.7.egg-info/
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc COPYING README.md

%changelog
* Mon Oct 08 2012 Nikos Roussos <nikos@roussos.cc> 2.1.1-1
- Initial package for Fedora
