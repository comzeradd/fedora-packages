Name:           skyviewer
Version:        1.0.0
Release:        6%{?dist}
Summary:        Program to display HEALPix-based skymaps in FITS files

Group:          Amusements/Graphics
License:        Public Domain
URL:            http://lambda.gsfc.nasa.gov/toolbox/tb_skyviewer_ov.cfm
Source0:        http://lambda.gsfc.nasa.gov/toolbox/skyviewer/%{name}-%{version}.tar.gz
Source1:        skyviewer.desktop
# Will be included in the next release
Source2:        skyviewer-license.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cfitsio-devel
BuildRequires:  chealpix-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libQGLViewer-devel
BuildRequires:  qt4-devel

%description
SkyViewer is an OpenGL based program to display HEALPix-based skymaps,
saved in FITS format files. The loaded skymaps can be viewed either on a 3D
sphere or as a Mollweide projection. In either case, realtime panning and
zooming are supported, along with rotations for the 3D sphere view,
assuming you have a strong enough graphics card.


%prep
%setup -q
install -pm 0644 %{SOURCE2} LICENSE


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
%doc test_iqu.fits README.txt LICENSE general.txt notes-ngp.txt


%changelog
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
