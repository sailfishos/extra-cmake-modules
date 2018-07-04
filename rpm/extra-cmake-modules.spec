Name:        extra-cmake-modules
Version:     5.47.0
Release:     1
Summary:     The Extra CMake Modules package
License:     BSD-3-Clause
URL:         https://cgit.kde.org/extra-cmake-modules.git
Source0:     %{name}-%{version}.tar.gz
BuildRequires: cmake
BuildArch: noarch

%description
The Extra CMake Modules package, or ECM, adds to the modules provided by CMake, including ones
used by find_package() to find common software, ones that can be used directly in CMakeLists.txt
files to perform common tasks and toolchain files that must be specified on the commandline by the user.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
cmake . -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{make_install}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING-CMAKE-SCRIPTS README.rst
%{_datarootdir}/ECM/modules/*
%{_datarootdir}/ECM/test-modules/*
%{_datarootdir}/ECM/kde-modules/*
%{_datarootdir}/ECM/find-modules/*
%{_datarootdir}/ECM/toolchain/*
%{_datarootdir}/ECM/cmake/*
