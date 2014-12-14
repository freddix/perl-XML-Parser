# based on PLD Linux spec git://git.pld-linux.org/packages/.git
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Parser
#
Summary:	XML::Parser Perl module
Name:		perl-XML-Parser
Version:	2.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c9ca46832d8e7578bcda99eba3a47f1
Patch0:		%{name}-paths.patch
BuildRequires:	expat-devel
BuildRequires:	perl-URI
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Parser - A Perl module for parsing XML documents.

%prep
%setup -qn %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	EXPATLIBPATH=%{_libdir} \
	EXPATINCPATH=%{_includedir}
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%check
%{__make} test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/XML/Parser.pm
%{perl_vendorarch}/XML/Parser
%dir %{perl_vendorarch}/auto/XML/Parser
%dir %{perl_vendorarch}/auto/XML/Parser/Expat
%attr(755,root,root) %{perl_vendorarch}/auto/XML/Parser/Expat/Expat.so
%{_mandir}/man3/*

