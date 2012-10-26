Summary:	Download and Install Windows Libraries on WINE 
Summary(de):	Herunterladen und Installieren von Windows-Bibliotheken für WINE
Name:		winetricks
Version:	20120912
Release:	%mkrel 1
Group:		Emulators
License:	LGPLv2+
URL:		http://wiki.winehq.org/winetricks
Source0:	http://www.kegel.com/wine/winetricks
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
Requires:	wine 
Requires:	wine-gecko
Requires:	cabextract

%description
winetricks is a quick and dirty script to download and install various redistributable 
runtime libraries sometimes needed to run programs in Wine.

You can find winetricks in your menu under 'More Applications -> Emulators'.

See: http://wiki.winehq.org/winetricks for more details.

%description -l de
winetricks ist ein schnelles und schmutziges Skript zum Herunterladen von verschiedenen
wieder verteilbaren Laufzeitbibliotheken, die von manchen Programmen gebraucht werden um
unter Wine zu funktionieren.

Sie finden winetricks im Menü unter 'Weitere Anwendungen -> Emulatoren'.

Besuchen Sie http://wiki.winehq.org/winetricks für weitere Details!


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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

