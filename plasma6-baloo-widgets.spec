#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define baloowidgets_major 6
%define libbaloowidgets %mklibname KF6BalooWidgets

Summary:	Widgets for Baloo
Name:		plasma6-baloo-widgets
Version:	24.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/baloo-widgets/-/archive/%{gitbranch}/baloo-widgets-%{gitbranchd}.tar.bz2#/baloo-widgets-%{git}.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/baloo-widgets-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(KF6Baloo)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
Requires:	%{libbaloowidgets} = %{EVRD}

%description
Widgets for Baloo.

%files -f %{name}.lang
%{_bindir}/baloo_filemetadata_temp_extractor
%{_libdir}/qt6/plugins/kf6/kfileitemaction/tagsfileitemaction.so
%{_libdir}/qt6/plugins/kf6/propertiesdialog/baloofilepropertiesplugin.so
%{_datadir}/qlogging-categories6/baloo-widgets.categories

#--------------------------------------------------------------------
%package -n %{libbaloowidgets}
Summary:	Shared library for Baloo Widgets
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libbaloowidgets}
Shared library for Baloo Widgets.

%files -n %{libbaloowidgets}
%{_libdir}/libKF6BalooWidgets.so.%{baloowidgets_major}*
%{_libdir}/libKF6BalooWidgets.so.%(echo %{version} |cut -d. -f1)*

#--------------------------------------------------------------------

%define devbaloowidgets %mklibname KF6BalooWidgets -d

%package -n %{devbaloowidgets}
Summary:	Devel stuff for Baloo Wigets
Group:		Development/KDE and Qt
Requires:	%{libbaloowidgets} = %{EVRD}
Requires:	cmake(KF6Baloo)
Provides:	%{name}-devel = %{EVRD}

%description -n %{devbaloowidgets}
This package contains header files needed if you wish to build applications
based on Baloo Widgets.

%files -n %{devbaloowidgets}
%{_includedir}/KF6/BalooWidgets
%{_libdir}/cmake/KF6BalooWidgets
%{_libdir}/libKF6BalooWidgets.so

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n baloo-widgets-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang baloowidgets5
cat *.lang >%{name}.lang
