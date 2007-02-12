Summary:	The GNOME Volume Manager
Summary(pl.UTF-8):   Zarządca woluminów dla GNOME
Name:		gnome-volume-manager
Version:	2.17.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-volume-manager/2.17/%{name}-%{version}.tar.bz2
# Source0-md5:	104cec26e721e0bba69debd392367195
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-defaults.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	dbus >= 0.91
Requires:	eject
Requires:	gnome-mount
Requires:	hal >= 0.5.7.1
Requires:	libgnomeui >= 2.15.91
Requires:	notification-daemon >= 0.3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNOME Volume Manager monitors volume-related events and responds
with user-specified policy. The GNOME Volume Manager can automount
hot-plugged drives, automount inserted removable media, autorun
programs, automatically play audio CDs and video DVDs, and
automatically import photos from a digital camera. The GNOME Volume
Manager does this entirely in user-space and without polling.

%description -l pl.UTF-8
Zarządca woluminów dla GNOME monitoruje zdarzenia związane z
woluminami i reaguje na nie zgodnie z polityką określoną przez
użytkownika. Program ten potrafi automatycznie montować urządzenia
hotplug oraz nośniki wymienne, odtwarzać płyty audio, czy DVD, a także
automatycznie importować zdjęcia z aparatu cyfrowego. Zarządca ten
działa w przestrzeni użytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--with-console-auth-dir=%{_localstatedir}/lock/console/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	autostartdir=%{_datadir}/gnome/autostart

#rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-volume-manager.schemas

%preun
%gconf_schema_uninstall gnome-volume-manager.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome/autostart/*.desktop
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_sysconfdir}/gconf/schemas/gnome-volume-manager.schemas
