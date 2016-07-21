Name:		kcolorchooser
Summary:	KDE Color Chooser
Version:	16.04.3
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)

%description
KColorChooser is a simple application to select the color from the screen or
from a pallete.
Features :
   - Select colors from any location on the screen.
   - Select colors from a range of standard palletes available.
   - Color values shown in Hue-Saturation-Value (HSV), Red-Green-Blue (RGB) and
     HTML formats.

%files
%{_bindir}/kcolorchooser
%{_datadir}/applications/kcolorchooser.desktop
%{_datadir}/icons/*/*/*/kcolorchooser*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%ninja

%install
%ninja_install -C build
