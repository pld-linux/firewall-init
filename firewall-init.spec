Summary:	Firewall SysV-init style start-up script
Summary(pl):	Skrypt startowy firewalla
Name:		firewall-init
Version:	2.99.0
Release:	1
License:	GPL
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Source0:	ftp://ftp.pld.org.pl/software/firewall-init/%{name}-%{version}.tar.gz
Requires:	iptables
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall-init is meant to provide an easy to use interface to start
and stopping the kernel IP packet filter through iptables(8).

%description -l pl
Dzi�ki firewall-init uzyskuje si� �atwy interfejs do startowania i
stopowania filtr�w IP j�dra poprzez iptables(8).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%post
/sbin/chkconfig --add firewall

%postun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del firewall
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(640,root,root,750)
%doc README.gz
%verify(not size mtime md5) %config(noreplace) /etc/sysconfig/firewall
%verify(not size mtime md5) %config(noreplace) /etc/sysconfig/firewall.d/*
%attr(754,root,root) /etc/rc.d/init.d/firewall
%dir /etc/sysconfig/firewall.d
