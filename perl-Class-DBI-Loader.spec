%define module	Class-DBI-Loader
%define name	perl-%{module}
%define version 0.33
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Dynamic definition of Class::DBI sub classes
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DM/DMAKI/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	perl-Lingua-EN-Inflect
BuildRequires:	perl-DBI >= 0.89

%description
Class::DBI::Loader automate the definition of Class::DBI sub-classes.
scan table schemas and setup columns, primary key.
class names are defined by table names and namespace option.
Class::DBI::Loader supports MySQL, Postgres and SQLite.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

