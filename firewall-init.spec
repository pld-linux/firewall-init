Summary:	Firewall SysV-init style start-up script
Summary(pl):	Skrypt startowy firewalla
Name:		firewall-init
Version:	2.99.6
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://ep09.pld-linux.org/~mmazur/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	2d2714634b48e79cccfe95e5163b4cde
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	iptables >= 1.2.2-2
Obsoletes:	iptables-init
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall-init is meant to provide an easy to use interface for starting
and stopping the kernel IP packet filter through iptables(8).

%description -l pl
Dziêki firewall-init uzyskuje siê ³atwy interfejs do startowania i
stopowania filtrów IP j±dra poprzez iptables(8).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%%pre
#if [ `rpm -q --queryformat='%{VERSION}' firewall-init` < '2.5' ]; then
#	echo "You need to manually convert your rules to iptables or install"
#	echo "firewall-init-ipchains"
#	exit 1
#fi

%post
/sbin/chkconfig --add firewall
/sbin/chkconfig --add firewall-pre

%postun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del firewall
	/sbin/chkconfig --del firewall-pre
fi

%files
%defattr(644,root,root,755)
%doc README
%defattr(640,root,root,750)
%verify(not size mtime md5) %config(noreplace) /etc/sysconfig/firewall
%verify(not size mtime md5) %config(noreplace) /etc/sysconfig/firewall.d/ip*
%verify(not size mtime md5) %config(noreplace) /etc/sysconfig/firewall.d/functions.rules
/etc/sysconfig/firewall.d/functions
%attr(754,root,root) /etc/rc.d/init.d/firewall*
%dir /etc/sysconfig/firewall.d
