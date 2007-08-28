%define	module	Catalyst-Engine-Apache
%define	name	perl-%{module}
%define	modprefix Catalyst

%define version 1.11
%define release %mkrel 1
%define _requires_exceptions perl(A


Summary:	Catalyst Apache Engines
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst)
Requires:	apache-mod_perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package contains mod_perl handlers for Catalyst.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man3/*



