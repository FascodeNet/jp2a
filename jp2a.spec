%global srcurl  https://github.com/cslarsen/%{name}

Name:           jp2a
Version:        1.0.7
Release:        7%{?dist}
Summary:        Small utility that converts JPG images to ASCII (text) using libjpeg

License:        GPLv2+
URL:            https://csl.name/%{name}
Source0:        https://github.com/FascodeNet/jp2a_cmake/archive/refs/tags/cmake-2021-03-24.tar.gz

BuildRequires:  clang libjpeg-turbo-devel cmake ninja-build
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
%global debug_package %{nil}

%description
jp2a is a simple JPEG to ASCII converter. jp2a is very flexible.
It can use ANSI colors and html in output.
jp2a can also download and convert images from Internet via command line.


%prep
rm -rf %{buildroot}

%setup -n jp2a_cmake-cmake-2021-03-24

%build
%install
mkdir -p build
cd build
cmake -G Ninja -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ ..
ninja -j4
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
cp ./src/jp2a ${RPM_BUILD_ROOT}/usr/bin/



%files
/usr/bin/jp2a


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jun 17 2017 Raphael Groner <projects.rg@smart.ms> - 1.0.7-1
- initial
