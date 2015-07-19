Summary:	Widgets for Baloo
Name:		baloo-widgets
Version:	4.14.3
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	baloo-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kfilemetadata-devel
BuildRequires:	pkgconfig(akonadi)

%description
Widgets for Baloo.

#--------------------------------------------------------------------

%define baloowidgets_major 4
%define libbaloowidgets %mklibname baloowidgets %{baloowidgets_major}

%package -n %{libbaloowidgets}
Summary:	Shared library for Baloo Widgets
Group:		System/Libraries

%description -n %{libbaloowidgets}
Shared library for Baloo Widgets.

%files -n %{libbaloowidgets}
%{_kde_libdir}/libbaloowidgets.so.%{baloowidgets_major}*

#--------------------------------------------------------------------

%define devbaloowidgets %mklibname baloo-widgets -d

%package -n %{devbaloowidgets}
Summary:	Devel stuff for Baloo Wigets
Group:		Development/KDE and Qt
Requires:	%{libbaloowidgets} = %{EVRD}
Requires:	baloo-devel
Provides:	%{name}-devel = %{EVRD}

%description -n %{devbaloowidgets}
This package contains header files needed if you wish to build applications
based on Baloo Widgets.

%files -n %{devbaloowidgets}
%{_kde_includedir}/baloo/*
%{_kde_libdir}/cmake/BalooWidgets
%{_kde_libdir}/libbaloowidgets.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- Initial Rosa package
