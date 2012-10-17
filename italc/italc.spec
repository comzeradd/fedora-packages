Name:       italc
Version:    2.0.0
Release:    1%{?dist}
Summary:    Intelligent teaching and learning with computers

License:    GPLv2+
URL:        http://italc.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:    italc.desktop
#both patches below fix wrong fsf address
#https://sourceforge.net/tracker/?func=detail&aid=3343759&group_id=132465&atid=724375
Patch0:      italc-2.0.0-copyingfsf.patch
Patch1:      italc-2.0.0-readmefsf.patch

BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRequires:  libXtst-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  desktop-file-utils
Requires:       xorg-x11-xinit

%description
iTALC is a useful and powerful didactic tool which lets you view and
control computers in your labs and interact with students in a modern
way. It supports Linux and Windows NT/2000/XP and it even can be used
transparently in mixed environments.

%package    client
Summary:    software for iTALC-clients
Group:      Applications/Networking
Requires:   italc = %{version}

%description client
This package contains the software, needed by iTALC-clients.

%package master
Summary:    iTALC master software
Group:      Applications/Networking
Requires:   italc = %{version}
Requires:   italc-client = %{version}

%description master
This package contains the actual master-software for accessing clients.

%prep
%setup -q
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig


%build
mkdir build
pushd build
%cmake ..
make %{?_smp_mflags}
popd


%install
make -C build install DESTDIR=%{buildroot}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}
install -Dm644 ima/data/italc.png %buildroot/%{_datadir}/icons/italc.png
install -Dm644 ima/data/italc.png %buildroot/%{_datadir}/pixmaps/italc.xpm


%files
%doc COPYING README AUTHORS ChangeLog

%files client
%{_bindir}/ica
%{_bindir}/italc_auth_helper
%{_libdir}/libItalcCore.so

%files master
%{_bindir}/italc
%{_bindir}/imc
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Wed Mar 28 2012 Nikos Roussos <comzeradd@fedoraproject.org> - 2.0.0-1
- Update to version 2

* Tue Jun 28 2011 Nikos Roussos <comzeradd@fedoraproject.org> - 1.0.13-1
- Initial build

