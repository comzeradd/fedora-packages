%if 0%{?fedora} > 21
%global python3 1
%endif

Name:           git-cola
Version:        2.6
Release:        1%{?dist}
Summary:        A sleek and powerful git GUI

License:        GPLv2+
URL:            http://git-cola.github.io
Source0:        https://github.com/git-cola/git-cola/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  xmlto
%if 0%{?python3}
BuildRequires:  python3-PyQt4-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
%global sphinxbuild sphinx-build-3
# Set the Python version for brp-python-bytecompile (see the Python guidelines).
# We also use this to set the PYTHON makefile variable.
%global __python %{__python3}
Requires:       python3-PyQt4
Requires:       python3-PyQt4-webkit
Requires:       python3-inotify
%else
BuildRequires:  PyQt4-devel
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
# Set the Python version for brp-python-bytecompile (see the Python guidelines).
# We also use this to set the PYTHON makefile variable.
%global __python %{__python2}
Requires:       PyQt4
Requires:       PyQt4-webkit
Requires:       python-inotify
%endif
Requires:       git
Requires:       hicolor-icon-theme


%description
git-cola is a powerful git GUI with a slick and intuitive user interface.


%prep
%setup -q
%if 0%{?python3}
# fix #!/usr/bin/env/python to #!/usr/bin/env/python3 everywhere
find . -type f -exec sh -c "head {} -n 1 | grep ^#\!\ \*/usr/bin/env\ python >/dev/null && sed -i -e sX^#\!\ \*/usr/bin/env\ python\ \*"\\\$"X#\!/usr/bin/env\ python3Xg {}" \;
%endif


%build
%global makeopts PYTHON="%{__python}" %{?sphinxbuild:SPHINXBUILD="%{sphinxbuild}"}
make %{?_smp_mflags} %{makeopts}
make %{makeopts} doc


%install
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} install
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} install-doc
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} install-html
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola-folder-handler.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-dag.desktop


%post
update-desktop-database &> /dev/null || :


%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc COPYING COPYRIGHT README.md
%{_bindir}/cola
%{_bindir}/git-*
%{_datadir}/applications/git*.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_docdir}/%{name}/
%{_mandir}/man1/git*.1*


%changelog
* Fri May 06 2016  Nikos Roussos <comzeradd@fedoraproject.org> - 2.6-1
- Update to 2.6

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 2.3-6
- Requires: PyQt4-webkit

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.3-4
- Drop obsolete (since 2.0.0) dependency on python*-simplejson (#1294541)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 2.3-2
- Remove no longer required AppData file

* Tue Aug 11 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.3-1
- Update to 2.3 (#1231812)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Christopher Meng <rpm@cicku.me> - 2.1.2-1
- Update to 2.1.2

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.0.8-3
- Add an AppData file for the software center

* Mon Dec 15 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.8-2
- Build against Python 3 on Fedora >= 22

* Fri Dec 12 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.8-1
- Update to 2.0.8 (#1136235, also fixes #1171612)
- Use less hackish GitHub Source0 URL
- Add new icon to file list, icon scriptlets, Requires: hicolor-icon-theme

* Sun Aug 03 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.5-1
- Update to 2.0.5 (#1124151)

* Thu Jun 26 2014 Christopher Meng <rpm@cicku.me> - 2.0.4-1
- Update to 2.0.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.3-1
- Update to 2.0.3 (#1101185)
- Drop BR asciidoc, not used anymore (since 2.0.2)

* Wed Apr 23 2014 Christopher Meng <rpm@cicku.me> - 2.0.2-1
- Update to 2.0.2

* Fri Mar 21 2014 Christopher Meng <rpm@cicku.me> - 2.0.1-1
- Update to 2.0.1

* Wed Feb 26 2014 Christopher Meng <rpm@cicku.me> - 2.0.0-1
- Update to 2.0.0

* Sat Feb 15 2014 Christopher Meng <rpm@cicku.me> - 1.9.4-2
- Remove unneeded dependency.

* Fri Feb 07 2014 Christopher Meng <rpm@cicku.me> - 1.9.4-1
- Update to 1.9.4

* Thu Dec 12 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.3-1
- Update to 1.9.3 (#1040157)

* Thu Nov 28 2013 Christopher Meng <rpm@cicku.me> - 1.9.2-1
- Update to 1.9.2 with fix for BZ#1034778.

* Tue Nov 12 2013 Christopher Meng <rpm@cicku.me> - 1.9.1-1
- Update to 1.9.1 with fix for BZ#1028854.

* Wed Sep 25 2013 Christopher Meng <rpm@cicku.me> - 1.8.5-1
- Update to 1.8.5(BZ#1011796) with fix for BZ#886826.

* Thu Sep 05 2013 Christopher Meng <rpm@cicku.me> - 1.8.4-1
- Update to 1.8.4(BZ#1003317) with fix for BZ#1001200/BZ#1001200.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Christopher Meng <rpm@cicku.me> - 1.8.3-1
- Update to 1.8.3.
- Cleanup the spec.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.8.1-1
- Update to 1.8.1 (#885442)

* Wed Sep 26 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.8.0-1
- Update to 1.8.0 (#849593)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.7-1
- Update to 1.7.7 (#819165)

* Mon Mar 19 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.6-1
- Update to 1.7.6 (#804407)

* Mon Feb 20 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.5-1
- Update to 1.7.5 (#789309)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.5-1
- Update to 1.4.3.5 (#732249)

* Sat May 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.4-1
- Update to 1.4.3.4 (#706588)

* Sat Apr 23 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.3-1
- Update to 1.4.3.3 (#699123)

* Thu Apr 14 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.2-1
- Update to 1.4.3.2 (#696563, #694806)

* Sun Mar 06 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3.1-1
- Update to 1.4.3.1 (#682518)
- Drop upstreamed translations patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.4.3-1
- Update to 1.4.3, fixes broken Actions widget
- Drop docpath patch, fixed upstream
- Drop obsolete conditional for Fedora <= 11
- Fix installation of translations

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.4.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Mar 13 2010 Ben Boeckel <MathStuf@gmail.com> - 1.4.1.2-3
- Backport patch for documentation path

* Mon Jan 25 2010 Ben Boeckel <MathStuf@gmail.com> - 1.4.1.2-2
- Fix %%files list

* Sun Jan 24 2010 Ben Boeckel <MathStuf@gmail.com> - 1.4.1.2-1
- Update to 1.4.1.2

* Thu Dec 10 2009 Ben Boeckel <MathStuf@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Tue Nov 17 2009 Ben Boeckel <MathStuf@gmail.com> 1.4.0.5-1
- Update to 1.4.0.5

* Mon Nov 02 2009 Ben Boeckel <MathStuf@gmail.com> 1.4.0.1-1
- Update to 1.4.0.1
- Add patch to not ship simplejson

* Sat Oct 24 2009 Ben Boeckel <MathStuf@gmail.com> 1.4.0-1
- Update to 1.4.0

* Fri Aug 28 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.9.14-1
- Update to 1.3.9.14

* Wed Jul 29 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.8-3
- Try build again for mass rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.8-1
- Update to 1.3.8
- Fix changelog usage of %%
- BR and R on git instead of git-core
- Add conditionals on git-difftool

* Mon Mar 23 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.6-1
- Update to 1.3.6

* Mon Mar 16 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5.42-1
- Update to 1.3.5.42

* Sat Feb 28 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5.28-1
- Added %%post and %%postun
- Use desktop-file-install

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 9 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-4
- Added missing Requires on PyQt4

* Thu Feb 5 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-3
- Added patch for shebang line removal

* Thu Feb 5 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-2
- Add missing BRs

* Sun Feb 1 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.5-1
- Update for 1.3.5

* Thu Jan 8 2009 Ben Boeckel <MathStuf@gmail.com> 1.3.4.4-1
- Initial package
