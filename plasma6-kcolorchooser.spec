#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		plasma6-kcolorchooser
Summary:	KDE Color Chooser
Version:	24.12.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/kcolorchooser/-/archive/%{gitbranch}/kcolorchooser-%{gitbranchd}.tar.bz2#/kcolorchooser-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kcolorchooser-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)

%description
KColorChooser is a simple application to select the color from the screen or
from a pallete.
Features :
   - Select colors from any location on the screen.
   - Select colors from a range of standard palletes available.
   - Color values shown in Hue-Saturation-Value (HSV), Red-Green-Blue (RGB) and
     HTML formats.

%files -f kcolorchooser.lang
%{_bindir}/kcolorchooser
%{_datadir}/applications/org.kde.kcolorchooser.desktop
%{_datadir}/icons/*/*/*/kcolorchooser*
%{_datadir}/metainfo/org.kde.kcolorchooser.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kcolorchooser-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcolorchooser --with-html
