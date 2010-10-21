Summary:	The GNOME Volume Manager
Summary(pl.UTF-8):	Zarządca woluminów dla GNOME
Name:		gnome-volume-manager
Version:	2.24.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-volume-manager/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	ef99c49214a2e265b127470b1da97392
Patch0:		%{name}-defaults.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	dbus >= 0.91
Requires:	dbus(org.freedesktop.Notifications)
Requires:	eject
Requires:	gnome-mount
Requires:	hal >= 0.5.10
Requires:	libgnomeui >= 2.24.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

%build
%{__glib_gettextize}
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
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

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
%attr(755,root,root) %{_bindir}/gnome-volume-properties
%attr(755,root,root) %{_libdir}/gnome-volume-manager
%{_sysconfdir}/xdg/autostart/gnome-volume-manager.desktop
%{_datadir}/%{name}
%{_desktopdir}/gnome-volume-properties.desktop
%{_sysconfdir}/gconf/schemas/gnome-volume-manager.schemas
