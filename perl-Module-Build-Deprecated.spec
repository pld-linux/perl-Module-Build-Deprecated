#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Build-Deprecated
Summary:	Module::Build::Deprecated - A collection of modules removed from Module-Build
Summary(pl.UTF-8):	Module::Build::Deprecated - zbiór modułów usuniętych z Module-Build
Name:		perl-Module-Build-Deprecated
Version:	0.4210
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e6e5f4f27f0ea6990f29f6e10aa65e6
URL:		http://search.cpan.org/dist/Module-Build-Deprecated/
BuildRequires:	perl-Module-Build >= 0.3601
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-YAML >= 0.002
BuildRequires:	perl-Module-Metadata
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-version >= 0.87
%endif
Requires:	perl-Module-Build >= 0.4210
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a number of module that have been removed from
Module-Build: ModuleInfo, Version and YAML.

%description -l pl.UTF-8
Ten moduł zawiera zbiór modułów, które zostały usunięte z dystrybucji
Module-Build: ModuleInfo, Version oraz YAML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/Build/Deprecated.pm
%{perl_vendorlib}/Module/Build/ModuleInfo.pm
%{perl_vendorlib}/Module/Build/Version.pm
%{perl_vendorlib}/Module/Build/YAML.pm
%{_mandir}/man3/Module::Build::Deprecated.3pm*
%{_mandir}/man3/Module::Build::ModuleInfo.3pm*
%{_mandir}/man3/Module::Build::Version.3pm*
%{_mandir}/man3/Module::Build::YAML.3pm*
