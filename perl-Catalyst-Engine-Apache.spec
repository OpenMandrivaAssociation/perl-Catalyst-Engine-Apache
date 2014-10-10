%define	upstream_name	 Catalyst-Engine-Apache
%define upstream_version 1.16

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(A(.*)\\)'
%else
%define _requires_exceptions perl(A
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Catalyst Apache Engines
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildArch:	noarch
Requires:	apache-mod_perl

%description
This package contains mod_perl handlers for Catalyst.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.160.0-2mdv2011.0
+ Revision: 680719
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 595081
- update to new version 1.16

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 401785
- rebuild using %%perl_convert_version
- fixed license field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.12-3mdv2009.0
+ Revision: 255509
- rebuild

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2008.1
+ Revision: 173892
- update to new version 1.12

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2008.0
+ Revision: 72802
- new version

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.09-1mdv2008.0
+ Revision: 19291
-New version


* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:39:58 (54283)
- Rebuild, spec file cleanup

* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:35:44 (54279)
- import perl-Catalyst-Engine-Apache-1.07-2mdk

* Thu May 04 2006 Scott Karns <scottk@mandriva.org> 1.07-2mdk
- Adjusted BuildRequires

* Fri Mar 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.07-1mdk
- 1.07

* Tue Feb 14 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.06-1mdk
- 1.06

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.05-1mdk
- 1.05

* Tue Dec 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.03-1mdk
- 1.03
- Adjust requires and build-requires

* Sat Dec 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.00-1mdk
- Initial MDV package

