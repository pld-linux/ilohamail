Summary:	Easy-to-use Webmail
Name:		ilohamail
Version:	0.8.10
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/ilohamail/IlohaMail-%{version}.tar.gz
# Source0-md5:	60d776d5c326d2a5a675b044c7f5d345
Requires:	php
Requires:	php-gettext
Requires:	php-pcre
Requires:	php-imap
Requires:	webserver
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prefix:		/home/services/httpd/html

%define		_ilohamaildir	/home/services/httpd/html/%{name}

%description
IlohaMail is an easy-to-use, multilingual mail system

%prep
%setup -q -n IlohaMail-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ilohamaildir}

cp -a IlohaMail/* $RPM_BUILD_ROOT%{_ilohamaildir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO Manual/* THEMES  UPGRADING RELEASE_NOTES 
%dir %{_ilohamaildir}
%dir %{_ilohamaildir}/conf
%config(noreplace) %verify(not size mtime md5) %{_ilohamaildir}/conf/*
%attr(755,http,http) %{_ilohamaildir}/data
%{_ilohamaildir}/include
%{_ilohamaildir}/index.html
%{_ilohamaildir}/lang
%{_ilohamaildir}/source
