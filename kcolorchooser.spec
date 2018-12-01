Name:		kcolorchooser
Summary:	KDE Color Chooser
Version:	 18.11.90
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%files -f %{name}.lang
%{_bindir}/kcolorchooser
%{_datadir}/applications/org.kde.kcolorchooser.desktop
%{_datadir}/icons/*/*/*/kcolorchooser*

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
