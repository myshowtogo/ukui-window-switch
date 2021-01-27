%define debug_package %{nil}
Name:           ukui-window-switch
Version:        3.0.1
Release:        2
Summary:        Front of the window switch
License:        GPL-2+ BSD-2-clause BSD-3-clause and GPL-2+ 
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel
BuildRequires: libblkid-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libwnck3-devel
BuildRequires: gtk3-devel
BuildRequires: gsettings-qt-devel
BuildRequires: gsettings-qt

Requires: ukwm >= 1.1.0

%description
 Front of the window switcher in UKUI desktop environment.
 Provides the display function(Display window thumbnails and application
 icons) when the window is switching (press Alt+Tab key).

%prep
%setup -q

%build
qmake-qt5 
make

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/ukui/ukui-window-switch/
%{_bindir}/ukui-window-switch
%{_datadir}/dbus-1/
%{_datadir}/ukui-window-switch/

%changelog
* Wed Jan 27 2021 lvhan <lvhan@kylinos.cn> - 3.0.1-2
- update to upstream version 3.0.0-3

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 3.0.1-1
- update to upstream version 3.0.0-1+1103

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 2.0.2-1
- Init package for openEuler
