Name:       ninja-ide
Version:    2.1.1
Release:    3%{?dist}
Summary:    Ninja IDE for Python development

Group:      Development/Tools
License:    GPLv3
URL:        http://www.ninja-ide.org/
Source0:    https://github.com/downloads/%{name}/%{name}/%{name}-v%{version}.zip
Source1:    %{name}.desktop
Source2:    %{name}.1.gz

BuildRequires:  desktop-file-utils
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-inotify
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
mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}.1.gz
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
find %{buildroot} -name 'pep8mod.py' | xargs chmod 0755


%check
%{__python} setup.py test


%files
%doc COPYING README.md
%{python_sitelib}/ninja_ide/
%{python_sitelib}/ninja_tests/
%{python_sitelib}/NINJA_IDE-2.1.1-py2.7.egg-info/
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz


%changelog
* Wed Oct 10 2012 Nikos Roussos <nikos@roussos.cc> 2.1.1-3
- Fix perm error on a py script

* Tue Oct 09 2012 Nikos Roussos <nikos@roussos.cc> 2.1.1-2
- Minor fixes and man page inclusion

* Mon Oct 08 2012 Nikos Roussos <nikos@roussos.cc> 2.1.1-1
- Initial package for Fedora
