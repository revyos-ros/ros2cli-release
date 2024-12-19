%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-ros2param
Version:        0.32.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2param package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-rcl-interfaces
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-ros2cli
Requires:       ros-jazzy-ros2node
Requires:       ros-jazzy-ros2service
Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-timeout
BuildRequires:  ros-jazzy-ament-copyright
BuildRequires:  ros-jazzy-ament-flake8
BuildRequires:  ros-jazzy-ament-pep257
BuildRequires:  ros-jazzy-ament-xmllint
BuildRequires:  ros-jazzy-launch
BuildRequires:  ros-jazzy-launch-ros
BuildRequires:  ros-jazzy-launch-testing
BuildRequires:  ros-jazzy-launch-testing-ros
%endif

%description
The param command for ROS 2 command line tools.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Thu Dec 19 2024 Audrow Nash <audrow@openrobotics.org> - 0.32.2-1
- Autogenerated by Bloom

* Tue Jun 18 2024 Audrow Nash <audrow@openrobotics.org> - 0.32.1-2
- Autogenerated by Bloom

* Sat Jun 15 2024 Audrow Nash <audrow@openrobotics.org> - 0.32.1-1
- Autogenerated by Bloom

* Fri Apr 19 2024 Audrow Nash <audrow@openrobotics.org> - 0.32.0-2
- Autogenerated by Bloom

* Tue Apr 16 2024 Audrow Nash <audrow@openrobotics.org> - 0.32.0-1
- Autogenerated by Bloom

* Thu Mar 28 2024 Audrow Nash <audrow@openrobotics.org> - 0.31.2-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Audrow Nash <audrow@openrobotics.org> - 0.31.1-2
- Autogenerated by Bloom

