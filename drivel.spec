Summary:	A LiveJournal client for GNOME
Summary(pl.UTF-8):	Klient LiveJournala dla GNOME
Name:		drivel
Version:	2.0.2
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/drivel/%{name}-%{version}.tar.bz2
# Source0-md5:	b77d376946ab32f0f8992c5e0baf1f51
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-debug.patch
URL:		http://www.dropline.net/drivel/
BuildRequires:	automake
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

%description -l pl.UTF-8
Drivel to zaawansowany klient LiveJournala dla środowiska GNOME. Przy
zachowaniu pełnego zbioru możliwości, został on zaprojektowany z myślą
o używalności. Prezentuje elegancki interfejs użytkownika.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

%build
install /usr/share/automake/config.* .
%configure \
	--disable-schemas-install
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicated with nb
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no
rm -rf $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

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
%{_desktopdir}/*.desktop
%{_sysconfdir}/gconf/schemas/*
%dir %{_datadir}/drivel
%dir %{_datadir}/drivel/glade
%dir %{_datadir}/drivel/languages
%{_datadir}/drivel/languages/livejournal.lang
%{_datadir}/drivel/glade/drivel.glade
%{_iconsdir}/gnome/48x48/mimetypes/gnome-mime-application-x-drivel.png
%{_datadir}/mime/packages/drivel.xml
%{_omf_dest_dir}/drivel
