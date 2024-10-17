Name: meego-panel-web
Summary: Internet panel
Version: 0.2.0
Release: %mkrel 1
Group: System/Desktop
License: LGPL 2.1
URL: https://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
Source1: meego-panel-web
Patch0: use_default_icon.patch
Patch1: fix-launch-chrome.patch    
Requires: mutter-meego
BuildRequires: libclutter1.0-devel
BuildRequires: libgtk+2-devel
BuildRequires: mx-devel >= 0.99
BuildRequires: meego-panel-devel >= 0.75.4
BuildRequires: libsqlite3-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
Obsoletes: moblin-panel-web < 0.2.0

%description
Meego Internet panel

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_datadir}/mutter-meego/panels
mv %{buildroot}%{_libdir}/meego-panel-web %{buildroot}%{_libdir}/meego-panel-web.bin
install -m 755 %{SOURCE1} %{buildroot}%{_libdir}

%find_lang meego-panel-web


%files -f meego-panel-web.lang
%defattr(-,root,root,-)
%{_datadir}/mutter-meego/panels/*.desktop
%{_libdir}/meego-panel-web
%{_libdir}/meego-panel-web.bin
%{_datadir}/dbus-1/services/com.meego.UX.Shell.Panels.internet.service
%{_datadir}/meego-panel-web

