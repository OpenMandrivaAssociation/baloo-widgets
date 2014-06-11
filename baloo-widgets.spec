Summary:	Widgets for Baloo
Name:		baloo-widgets
Version:	4.13.2
Release:	1
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

