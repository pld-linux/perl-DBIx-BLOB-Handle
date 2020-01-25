#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	DBIx
%define		pnam	BLOB-Handle
Summary:	DBIx::BLOB::Handle - read database large object binaries from file handles
Summary(pl.UTF-8):	DBIx::BLOB::Handle - czytanie obiektów BLOB z uchwytów plików
Name:		perl-DBIx-BLOB-Handle
Version:	0.2
Release:	6
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e23fbc1e9ca23295847cb94780262757
URL:		http://search.cpan.org/dist/DBIx-BLOB-Handle/
BuildRequires:	perl-DBI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBI has a blob_copy_to_file method which takes a file handle argument
and copies a database large object binary (LOB) to this file handle.
However, the method is undocumented and faulty. Constructing a similar
method yourself is pretty simple but what if you wished to read the
data and perform operations on it? You could use the DBI's blob_read
method yourself to process chunks of data from the LOB or even dump
its contents into a scalar, but maybe it would be nice to read the
data line by line or piece by piece from a familiar old filehandle?!

%description -l pl.UTF-8
DBI ma metodę blob_copy_to_file, która przyjmuje parametr będący
uchwytem pliku i kopiuje duże obiekty bazodanowe (LOB) do tego
uchwytu. Mimo to, ta metoda jest nieudokumentowana i zawiera błędy.
Stworzenie podobnej metody jest proste, ale co jeśli trzeba czytać
dane i przeprowadzać na nich operacje? Można użyć metody blob_read z
DBI do przetwarzania fragmentów danych z obiektu LOB albo nawet
zrzucać zawartość do zmiennej, ale może przyjemniej jest czytać dane
linia po linii lub kawałek po kawałku z normalnego uchwytu pliku?

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/DBIx/BLOB
%{perl_vendorlib}/DBIx/BLOB/*.pm
%{_mandir}/man3/*
