Name:           ros-kinetic-cmake-modules
Version:        0.4.1
Release:        0%{?dist}
Summary:        ROS cmake_modules package
Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  ros-kinetic-catkin
BuildRequires:  gcc-c++

%description
A common repository for CMake Modules which are not distributed with CMake but
are commonly used by ROS packages.

%prep
%setup -q
cp %{SOURCE1001} .

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="$CMAKE_PREFIX_PATH" \
        -DCMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
pushd build
make install DESTDIR=%{buildroot}
popd

%files -f build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%changelog
* Thu Mar 30 2017 Zhang Xingtao <xingtao.zhang@yahoo.com> - 0.4.1
* Fri May 09 2014 William Woodall <william@osrfoundation.org> - 0.2.1-0
- Autogenerated by Bloom

