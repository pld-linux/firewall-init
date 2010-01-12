Summary:	Firewall SysV-init style start-up script
Summary(pl.UTF-8):	Skrypt startowy firewalla
Name:		firewall-init
Version:	2.99.11
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	ftp://ftp.pld-linux.org/software/firewall-init/%{name}-%{version}.tar.bz2
# Source0-md5:	8a57d9efb9df6f46b4665c55d0a9450f
BuildRequires:	rpmbuild(macros) >= 1.194
Requires(post,preun):	/sbin/chkconfig
Requires:	coreutils
Requires:	iptables >= 1.2.2-2
Requires:	rc-scripts
Obsoletes:	iptables-init
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall-init is meant to provide an easy to use interface for
starting and stopping the kernel IP packet filter through iptables(8).

%description -l pl.UTF-8
Dzięki firewall-init uzyskuje się łatwy interfejs do startowania i
stopowania filtrów IP jądra poprzez iptables(8).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 2.5
%banner -e %{name} <<'EOF'
You need to manually convert your rules to iptables or install
firewall-init-ipchains
EOF

%post
/sbin/chkconfig --add firewall
/sbin/chkconfig --add firewall-pre

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del firewall
	/sbin/chkconfig --del firewall-pre
fi

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%defattr(640,root,root,750)
%verify(not md5 mtime size) %config(noreplace) /etc/sysconfig/firewall
%verify(not md5 mtime size) %config(noreplace) /etc/sysconfig/firewall.d/ip*
%verify(not md5 mtime size) %config(noreplace) /etc/sysconfig/firewall.d/functions.rules
/etc/sysconfig/firewall.d/functions
%attr(754,root,root) /etc/rc.d/init.d/firewall*
%dir /etc/sysconfig/firewall.d
