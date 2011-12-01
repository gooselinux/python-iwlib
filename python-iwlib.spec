%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_ver: %define python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}

Summary: Wireless settings python bindings
Name: python-iwlib
Version: 0.1
Release: 1.2%{?dist}
URL: http://git.fedorahosted.org/git/python-iwlib.git
Source: http://fedorahosted.org/released/python-iwlib/%{name}-%{version}.tar.bz2
License: GPLv2
Group: System Environment/Libraries
BuildRequires: python-devel
BuildRequires: wireless-tools-devel
Requires: wireless-tools >= 28-0.pre8.5
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Python bindings for the iwlib kernel interface,
that provides functions to examine the wireless network devices
installed on the system.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
chmod 755 %{buildroot}%{python_sitearch}/iwlib.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{python_sitearch}/iwlib.so
%if "%{python_ver}" >= "2.5"
%{python_sitearch}/*.egg-info
%endif

%changelog
* Fri Jan 15 2010 Harald Hoyer <harald@redhat.com> 0.1-1.2
- built for s390/s390x (system-config-network needs it)
- Related: rhbz#543948

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.1-1.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Jiri Popelka <jpopelka@redhat.com> - 0.1-1
- Get iwlib code from rhpl 0.222-1
