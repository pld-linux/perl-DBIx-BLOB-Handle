#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	BLOB-Handle
Summary:	DBIx::BLOB::Handle - Read Database Large Object Binaries from file handles
#Summary(pl):	
Name:		perl-DBIx-BLOB-Handle
Version:	0.2
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBI has a blob_copy_to_file method which takes a file handle argument and
copies a database large object binary (LOB) to this file handle. However,
the method is undocumented and faulty. Constructing a similar method
yourself is pretty simple but what if you wished to read the data
and perform operations on it? You could use the DBI's blob_read method
yourself to process chunks of data from the LOB or even dump its contents
into a scalar, but maybe it would be nice to read the data line by line
or piece by piece from a familiar old filehandle?!

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/DBIx/BLOB/*.pm
%{_mandir}/man3/*
