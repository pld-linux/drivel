Summary:	A LiveJournal client for GNOME
Name:		drivel
Version:	0.9.1
Release:	1
License:	GPL
Group:		Applications/Communication
Url:		http://www.sf.net/projects/drivel
Source0:	http://dl.sourceforge.net/drivel/%{name}-%{version}.tar.bz2
# Source0-md5:	148bc826935b8cd19a035542c5076cbc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+2-devel
BuildRequires:	curl-devel

%description
Drivel is an advanced LiveJournal client for the GNOME desktop. While
maintaining a full set of features, it had been designed with
usability in mind, and presents an elegant user interface.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(644,root,root,755)
%doc README TODO COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
/etc/gconf/schemas/*

%clean
rm -r $RPM_BUILD_ROOT
