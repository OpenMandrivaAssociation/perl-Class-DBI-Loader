%define upstream_name	 Class-DBI-Loader
%define upstream_version 0.34

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Dynamic definition of Class::DBI sub classes
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(DBI)
BuildArch:	noarch

%description
Class::DBI::Loader automate the definition of Class::DBI sub-classes.
scan table schemas and setup columns, primary key.
class names are defined by table names and namespace option.
Class::DBI::Loader supports MySQL, Postgres and SQLite.

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
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.340.0-2mdv2011.0
+ Revision: 680791
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 401706
- rebuild using %%perl_convert_version
- fixed license field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.34-3mdv2009.0
+ Revision: 255948
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.34-1mdv2008.1
+ Revision: 136683
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.34-1mdv2008.0
+ Revision: 19789
- 0.34


* Thu Jul 06 2006 Arnaud de Lorbeau <adelorbeau@seanodes.com> 0.33-2mdv2007.0
- Add buildrequires

* Fri Jun 30 2006 Arnaud de Lorbeau <adelorbeau@seanodes.com> 0.33-1mdv2007.0
- 0.33

