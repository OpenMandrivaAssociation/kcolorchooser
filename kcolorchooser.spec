Name:    kcolorchooser
Summary: KDE Color Chooser
Version: 4.8.0
Release: 1
Epoch:   2
Group:   Graphical desktop/KDE
License: GPLv2
URL:     http://www.kde.org
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KColorChooser is a simple application to select the color from the screen or
from a pallete.
Features :
   - Select colors from any location on the screen.
   - Select colors from a range of standard palletes available.
   - Color values shown in Hue-Saturation-Value (HSV), Red-Green-Blue (RGB) and
     HTML formats.

%files
%_kde_bindir/kcolorchooser
%_kde_applicationsdir/kcolorchooser.desktop
%_kde_iconsdir/*/*/*/kcolorchooser*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

