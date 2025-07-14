#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	GUPnP-UI - a collection of GTK+ widgets on top of GUPnP
Summary(pl.UTF-8):	GUPnP-UI - widgety GTK+ dla biblioteki GUPnP
Name:		gupnp-ui
Version:	0.1.1
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-ui/0.1/%{name}-%{version}.tar.gz
# Source0-md5:	5ca6b3f6740d0295066b0b533289aa4c
Patch0:		%{name}-gupnp.patch
URL:		http://gupnp.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gupnp-devel >= 1.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gupnp >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUPnP-UI provides a collection of simple GTK+ widgets on top of GUPnP.

%description -l pl.UTF-8
Biblioteka GUPnP-UI dostarcza zbiór prostych widgetów GTK+ dla
biblioteki GUPnP.

%package devel
Summary:	Header files for GUPnP-UI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GUPnP-UI
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2.0
Requires:	gupnp-devel >= 1.2

%description devel
Header files for GUPnP-UI library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GUPnP-UI.

%package static
Summary:	Static GUPnP-UI library
Summary(pl.UTF-8):	Statyczna biblioteka GUPnP-UI
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GUPnP-UI library.

%description static -l pl.UTF-8
Statyczna biblioteka GUPnP-UI.

%package apidocs
Summary:	GUPnP-UI library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki GUPnP-UI
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for GUPnP-UI library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GUPnP-UI.

%prep
%setup -q
%patch -P0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgupnp-ui-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgupnp-ui-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgupnp-ui-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgupnp-ui-1.0.so
%{_includedir}/gupnp-ui-1.0
%{_pkgconfigdir}/gupnp-ui-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgupnp-ui-1.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-ui
%endif
