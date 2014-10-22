Name:           skyviewer
Version:        1.0.1
Release:        1%{?dist}
Summary:        Program to display HEALPix-based skymaps in FITS files

Group:          Amusements/Graphics
License:        Public Domain
URL:            http://lambda.gsfc.nasa.gov/toolbox/tb_skyviewer_ov.cfm
Source0:        http://lambda.gsfc.nasa.gov/toolbox/skyviewer/%{name}-%{version}.tar.gz
Source1:        skyviewer.desktop
Patch0:         skyviewer-1.0.1-libGLU.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cfitsio-devel
BuildRequires:  chealpix-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libQGLViewer-devel
BuildRequires:  qt4-devel
BuildRequires:  mesa-libGLU-devel

%description
SkyViewer is an OpenGL based program to display HEALPix-based skymaps,
saved in FITS format files. The loaded skymaps can be viewed either on a 3D
sphere or as a Mollweide projection. In either case, realtime panning and
zooming are supported, along with rotations for the 3D sphere view,
assuming you have a strong enough graphics card.


%prep
%setup -q
%patch0 -p1 -b .GLU


%build
%{_qt4_qmake} INCLUDE_DIR=%{_includedir} \
        LIB_DIR=%{_libdir} \
        INCPATH=%{_includedir}/cfitsio
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

# Binary
install -d $RPM_BUILD_ROOT%{_bindir}
install -pm 0755 skyviewer $RPM_BUILD_ROOT%{_bindir}

# Icon
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -pm 0644 images/spherical.png \
        $RPM_BUILD_ROOT%{_datadir}/pixmaps/skyviewer.png

# Desktop entry
desktop-file-install --vendor='' %{SOURCE1} \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications


%clean
rm -rf $RPM_BUILD_ROOT


%pre
/usr/bin/update-desktop-database >/dev/null 2>&1 || :


%post
/usr/bin/update-desktop-database >/dev/null 2>&1 || :


%files
%defattr(-,root,root,-)
%{_bindir}/skyviewer
%{_datadir}/pixmaps/skyviewer.png
%{_datadir}/applications/skyviewer.desktop
%doc test_iqu.fits README.txt License.txt general.txt notes-ngp.txt


%changelog
* Fri Jul 04 2014 Nikos Roussos <comzeradd@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Orion Poplawski <orion@cora.nwra.com> - 1.0.0-14
- Rebuild for cfitsio 3.360

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.0-12
- rebuild for new cfitsio
- fix ftbfs, link to libGLU

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.0-7
- Rebuild for libQGLViewer-2.3.9.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 09 2010 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-5
- Rebuild

* Tue Apr 27 2010 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-4
- Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-2
- Update license
- Fix RBs (Jussi Lehtola)
- Add documentation

* Wed Mar 25 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 1.0.0-1
- Initial packaging
