%define major 20
%define libname %mklibname xml-security-c %{major}
%define develname %mklibname xml-security-c -d


Name:		xml-security-c
Version:	2.0.4
Release:	2
Summary:	C++ Implementation of W3C security standards for XML

Group:		System/Libraries
License:	ASL 2.0
URL:		http://santuario.apache.org/cindex.html
Source0:	https://downloads.apache.org/santuario/c-library/xml-security-c-%{version}.tar.bz2

# xalan-c-devel
BuildRequires:	pkgconfig(xerces-c)
BuildRequires:	pkgconfig(openssl)

%description
The xml-security-c library is a C++ implementation of the XML Digital Signature
specification. The library makes use of the Apache XML project's Xerces-C XML
Parser and Xalan-C XSLT processor. The latter is used for processing XPath and
XSLT transforms.

%package -n	%{libname}
Summary:	C++ Implementation of W3C security standards for XML
Group:		System/Libraries

%description -n %{libname}
The xml-security-c library is a C++ implementation of the XML Digital Signature
specification. The library makes use of the Apache XML project's Xerces-C XML
Parser and Xalan-C XSLT processor. The latter is used for processing XPath and
XSLT transforms.

# xalan-c-devel
%package -n	%{develname}
Summary:	Development files for xml-security-c
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	xml-security-c-devel
Requires:	pkgconfig(xerces-c)
Requires:	pkgconfig(openssl)
# There are a number of headers that can use NSS if HAVE_NSS is set to 1
# Current build does not set it (configure does not even check for NSS)
# so we do not include this dependency for now.
# Requires:	nss-devel

%description -n %{develname}
This package provides development files for xml-security-c, a C++ library for
XML Digital Signatures.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install

# Do not ship library test utilities. These are only needed for
# xml-security-c developers and they should have the whole source anyway.
rm -rf %{buildroot}%{_bindir}

%files -n %{libname}
%{_libdir}/libxml-security-c.so.%{major}*

%files -n %{develname}
%{_includedir}/xsec
%{_libdir}/libxml-security-c.so
%{_libdir}/pkgconfig/xml-security-c.pc
