%define	module	Catalyst-Engine-Apache
%define	name	perl-%{module}
%define	modprefix Catalyst

%define version 1.07
%define release %mkrel 3

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
BuildRequires:  perl(Module::Build)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
Requires:	apache-mod_perl

%description
This package contains mod_perl handlers for Catalyst.

%define _requires_exceptions perl(A

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%buildroot

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/man3/*



