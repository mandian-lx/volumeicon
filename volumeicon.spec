Summary:	Lightweight volume control
Name:		volumeicon
Version:	0.4.6
Release:	2
Group:		Graphical desktop/Other
License:	GPLv3
URL:		http://softwarebakery.com/maato/volumeicon.html
Source0:        http://softwarebakery.com/maato/files/volumeicon/%{name}-%{version}.tar.gz
Patch0:		glib.h_include.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)

Obsoletes: %name < %version

%description
Volume Icon aims to be a lightweight volume control that sits in your systray.
Features

* Change volume by scrolling on the systray icon
* Ability to choose which channel to control
* Configurable stepsize (percentage of volume
  increase/decrease per scrollwheel step)
* Several icon themes (with gtk theme as default)
* Configurable external mixer
* Volume Slider


%prep
%setup -q 
%apply_patches

%build
%configure2_5x
       
%make 

%install
%makeinstall_std
mkdir -p %{buildroot}%_sysconfdir/xdg/autostart/
cat > %{buildroot}%_sysconfdir/xdg/autostart/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=volumeicon
Comment=Volume Icon
Exec=%{name}
Terminal=false
Type=Application
Icon=%{_datadir}/%{name}/gui/appicon.svg
Categories=AudioVideo;Audio
EOF

#%find_lang %{name}

%files 
#-f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%_sysconfdir/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}
