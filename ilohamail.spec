Summary:	IlohaMail - light-weight yet full featured, easy-to-use webmail
Summary(pl.UTF-8):	IlohaMail - lekki ale w pełni funkcjonalny, łatwy w użyciu webmail
Name:		ilohamail
Version:	0.8.13
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/ilohamail/IlohaMail-%{version}.tar.gz
# Source0-md5:	491f1a7e9ab3a5e34c006c9693ef6406
URL:		http://ilohamail.sourceforge.net/
Requires:	php(gettext)
Requires:	php(imap)
Requires:	php(pcre)
Requires:	webserver
Requires:	webserver(php)
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ilohamaildir	/home/services/httpd/html/%{name}

%description
IlohaMail (pronounced: e-lo-ha-mail) is a light weight yet full
featured multilingual webmail program that is easy to use and install.
It runs on a stock build of PHP, and does not require databases
(although database support is available) or the IMAP library (it is
powered by a custom IMAP/POP3 library).

%description -l pl.UTF-8
IlohaMail to lekki ale w pełni funkcjonalny, wielojęzyczny, łatwy w
użyciu i instalacji program webmail. Działa na samym PHP, nie wymaga
baz danych (chociaż dostępna jest ich obsługa) ani biblioteki IMAP
(działa w oparciu o własną bibliotekę IMAP/POP3).

%prep
%setup -q -n IlohaMail-%{version}

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
%config(noreplace) %verify(not md5 mtime size) %{_ilohamaildir}/conf/*
%attr(755,http,http) %{_ilohamaildir}/data
%{_ilohamaildir}/include
%{_ilohamaildir}/index.html
%{_ilohamaildir}/lang
%{_ilohamaildir}/source
