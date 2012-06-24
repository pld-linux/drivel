Summary:	A LiveJournal client for GNOME
Summary(pl):	Klient LiveJournala dla GNOME
Name:		drivel
Version:	0.9.1
Release:	1
License:	GPL
Group:		Applications/Communication
Source0:	http://dl.sourceforge.net/drivel/%{name}-%{version}.tar.bz2
# Source0-md5:	148bc826935b8cd19a035542c5076cbc
URL:		http://www.sf.net/projects/drivel/
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Drivel is an advanced LiveJournal client for the GNOME desktop. While
maintaining a full set of features, it had been designed with
usability in mind, and presents an elegant user interface.

%description -l pl
Drivel to zaawansowany klient LiveJournala dla �rodowiska GNOME. Przy
zachowaniu pe�nego zbioru mo�liwo�ci, zosta� on zaprojektowany z my�l�
o u�ywalno�ci. Prezentuje elegancki interfejs u�ytkownika.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
%{_sysconfdir}/gconf/schemas/*

%clean
rm -r $RPM_BUILD_ROOT
