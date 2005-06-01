Summary:	A LiveJournal client for GNOME
Summary(pl):	Klient LiveJournala dla GNOME
Name:		drivel
Version:	1.3.90
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/drivel/%{name}-%{version}.tar.bz2
# Source0-md5:	c03231f6dbcf93baed2cff354a2956a8
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-ipv6proxy.patch
URL:		http://www.dropline.net/drivel/
BuildRequires:	curl-devel
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	gtksourceview-devel >= 1.0.0
BuildRequires:	gtkspell-devel >= 1:2.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rhythmbox
BuildRequires:	scrollkeeper >= 0.3.5
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Drivel is an advanced LiveJournal client for the GNOME desktop. While
maintaining a full set of features, it had been designed with
usability in mind, and presents an elegant user interface.

%description -l pl
Drivel to zaawansowany klient LiveJournala dla ¶rodowiska GNOME. Przy
zachowaniu pe³nego zbioru mo¿liwo¶ci, zosta³ on zaprojektowany z my¶l±
o u¿ywalno¶ci. Prezentuje elegancki interfejs u¿ytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure \
	--disable-schemas-install
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -r $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_sysconfdir}/gconf/schemas/*
%dir %{_datadir}/drivel
%dir %{_datadir}/drivel/glade
%dir %{_datadir}/drivel/languages
%{_datadir}/drivel/languages/livejournal.lang
%{_datadir}/drivel/glade/drivel.glade
%{_datadir}/application-registry/drivel.applications
%{_iconsdir}/gnome/48x48/mimetypes/gnome-mime-application-x-drivel.png
%{_datadir}/mime-info/drivel.*
%{_datadir}/mime/packages/drivel.xml
%{_datadir}/omf/drivel/drivel-C.omf
