Name:		kcolorchooser
Summary:	KDE Color Chooser
Version:	15.08.1
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
KColorChooser is a simple application to select the color from the screen or
from a pallete.
Features :
   - Select colors from any location on the screen.
   - Select colors from a range of standard palletes available.
   - Color values shown in Hue-Saturation-Value (HSV), Red-Green-Blue (RGB) and
     HTML formats.

%files
%{_kde_bindir}/kcolorchooser
%{_kde_applicationsdir}/kcolorchooser.desktop
%{_kde_iconsdir}/*/*/*/kcolorchooser*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Fri Jul 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Wed Jul 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762455
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758047
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 744530
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739358
- New upstream tarball

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 731856
- New upstream tarball 4.7.80

* Tue Oct 11 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 704179
- Import kcolorchooser
- Create current folder

