Summary:	Download and Install Windows Libraries on WINE 
Name:		winetricks
Version:	20240105
Release:	1
Group:		Emulators
License:	LGPLv2+
URL:		https://wiki.winehq.org/winetricks
Source0:	http://winetricks.org/winetricks
%ifarch x86_64
Requires:   wine64
Requires:   wine64-gecko
%else
Requires:   wine 
Requires:   wine-gecko
%endif
Requires:   cabextract

# No debug, but not noarch to have different reqs in different archs
%define debug_package %{nil}

%description
winetricks is a quick and dirty script to download and install various
redistributable runtime libraries sometimes needed to run programs in Wine.

You can find winetricks in your menu under 'More Applications -> Emulators'.

See: http://wiki.winehq.org/winetricks for more details.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=%{name}
Comment=Download and Install Windows Libraries on WINE
Comment[de]=Herunterladen und Installieren von Windows-Bibliotheken für WINE
StartupNotify=true
Terminal=false
Type=Application
Icon=wine
Exec=%{name}
Categories=X-MandrivaLinux-MoreApplications-Emulators
EOF

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
