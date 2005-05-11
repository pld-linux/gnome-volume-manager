Summary:	The GNOME Volume Manager
Summary(pl):	Zarz±dca woluminów dla GNOME
Name:		gnome-volume-manager
Version:	1.2.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-volume-manager/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	7ec66ed5fab8b2d69fd4a06d2d188b25
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-mount-argument.patch
Patch2:		%{name}-less_verbose.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.23
BuildRequires:	hal-devel >= 0.4.7
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	dbus >= 0.23
Requires:	hal >= 0.4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNOME Volume Manager monitors volume-related events and responds
with user-specified policy. The GNOME Volume Manager can automount
hot-plugged drives, automount inserted removable media, autorun
programs, automatically play audio CDs and video DVDs, and
automatically import photos from a digital camera. The GNOME Volume
Manager does this entirely in user-space and without polling.

%description -l pl
Zarz±dca woluminów dla GNOME monitoruje zdarzenia zwi±zane z
woluminami i reaguje na nie zgodnie z polityk± okre¶lon± przez
u¿ytkownika. Program ten potrafi automatycznie montowaæ urz±dzenia
hotplug oraz no¶niki wymienne, odtwarzaæ p³yty audio, czy DVD, a tak¿e
automatycznie importowaæ zdjêcia z aparatu cyfrowego. Zarz±dca ten
dzia³a w przestrzeni u¿ytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
