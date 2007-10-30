Summary:	String library with very low memory overhead
Summary(pl.UTF-8):	Biblioteka operacji na łańcuchach o małym narzucie pamięciowym
Name:		ustr
Version:	1.0.2
Release:	0.1
License:	LGPL v2+ or BSD or MIT
Group:		Libraries
Source0:	http://www.and.org/ustr/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	031846d6e6f86530752bcab9b2eed9e7
URL:		http://www.and.org/ustr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Micro string library, very low overhead from plain strdup() (Ave. 44%%
for 0-20B strings). Very easy to use in existing C code.

%description -l pl.UTF-8
Malutka biblioteka operacji na łańcuchach znaków, mająca bardzo mały
narzut pamięciowy w stosunku do zwykłego strdup() (średnio 44%% dla
łańcuchów 0-20B). Bardzo łatwa w użyciu w istniejącym kodzie w C.

%package devel
Summary:	Header files for ustr library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ustr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ustr library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ustr.

%package static
Summary:	Static ustr library
Summary(pl.UTF-8):	Statyczna biblioteka ustr
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ustr library.

%description static -l pl.UTF-8
Statyczna biblioteka ustr.

%prep
%setup -q

%build
%{__make} all-shared \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIB_SHARED='$(OPT_LIB_SHARED)' \
	LIB_STATIC='$(OPT_LIB_STATIC)' \
	HIDE=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	LIB_SHARED='$(OPT_LIB_SHARED)' \
	LIB_STATIC='$(OPT_LIB_STATIC)' \
	LDCONFIG=true

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE LICENSE_BSD LICENSE_MIT NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libustr-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libustr-1.0.so.1

%files devel
%defattr(644,root,root,755)
%doc Documentation/*.html 'Documentation/strdup vs. ustr.gnumeric'
%attr(755,root,root) %{_bindir}/ustr-import
%attr(755,root,root) %{_libdir}/libustr.so
%{_includedir}/ustr*.h
%{_datadir}/ustr-%{version}
%{_pkgconfigdir}/ustr.pc
%{_mandir}/man1/ustr-import.1*
%{_mandir}/man3/ustr*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libustr.a
