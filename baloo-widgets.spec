%define baloowidgets_major 5
%define libbaloowidgets %mklibname KF5BalooWidgets %{baloowidgets_major}

Summary:	Widgets for Baloo
Name:		baloo-widgets
Version:	17.07.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:        http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(Qt5Test)
Requires:	%{libbaloowidgets} = %{EVRD}

%description
Widgets for Baloo.

%files -f %{name}.lang
%{_bindir}/baloo_filemetadata_temp_extractor

#--------------------------------------------------------------------
%package -n %{libbaloowidgets}
Summary:	Shared library for Baloo Widgets
Group:		System/Libraries
Obsoletes:	%{mklibname baloowidgets 4}
Requires:	%{name} = %{EVRD}

%description -n %{libbaloowidgets}
Shared library for Baloo Widgets.

%files -n %{libbaloowidgets}
%{_libdir}/libKF5BalooWidgets.so.%{baloowidgets_major}*

#--------------------------------------------------------------------

%define devbaloowidgets %mklibname baloo-widgets -d

%package -n %{devbaloowidgets}
Summary:	Devel stuff for Baloo Wigets
Group:		Development/KDE and Qt
Requires:	%{libbaloowidgets} = %{EVRD}
Requires:	baloo5-devel
Provides:	%{name}-devel = %{EVRD}

%description -n %{devbaloowidgets}
This package contains header files needed if you wish to build applications
based on Baloo Widgets.

%files -n %{devbaloowidgets}
%{_includedir}/KF5/BalooWidgets
%{_libdir}/cmake/KF5BalooWidgets
%{_libdir}/libKF5BalooWidgets.so

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang baloo_naturalqueryparser
%find_lang baloowidgets5
cat *.lang >%{name}.lang
