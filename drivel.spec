Summary:	A LiveJournal client for GNOME
Summary(pl):	Klient LiveJournala dla GNOME
Name:		drivel
Version:	1.2.3
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/drivel/%{name}-%{version}.tar.bz2
# Source0-md5:	628909334696dd44dc6a60ece5445ae8
Patch0:		%{name}-desktop.patch
URL:		http://www.dropline.net/drivel/
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel
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

# also for desktop translation
mv -f po/{no,nb}.po

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
%{_datadir}/drivel/glade/drivel.glade
