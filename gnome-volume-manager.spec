Summary:	The GNOME Volume Manager
Summary(pl):	Zarz�dca wolumin�w dla GNOME
Name:		gnome-volume-manager
Version:	1.1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-volume-manager/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	9e92970db015fe8f259f19fef250294f
Source1:	%{name}-magicdev-wrapper
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.23
BuildRequires:	hal-devel >= 0.4.7
BuildRequires:	intltool >= 0.28
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
Requires(post):	GConf2
Requires:	dbus >= 0.23
Requires:	hal >= 0.4.7
Obsoletes:	magicdev
Provides:	magicdev
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNOME Volume Manager monitors volume-related events and responds
with user-specified policy. The GNOME Volume Manager can automount
hot-plugged drives, automount inserted removable media, autorun
programs, automatically play audio CDs and video DVDs, and
automatically import photos from a digital camera. The GNOME Volume
Manager does this entirely in user-space and without polling.

%description -l pl
Zarz�dca wolumin�w dla GNOME monitoruje zdarzenia zwi�zane z
woluminami i reaguje na nie zgodnie z polityk� okre�lon� przez
u�ytkownika. Program ten potrafi automatycznie montowa� urz�dzenia
hotplug oraz no�niki wymienne, odtwarza� p�yty audio, czy DVD, a tak�e
automatycznie importowa� zdj�cia z aparatu cyfrowego. Zarz�dca ten
dzia�a w przestrzeni u�ytkownika.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
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

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/magicdev

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
