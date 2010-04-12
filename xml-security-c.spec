Name:		xml-security-c
Version:	1.5.1
Release:	%mkrel 3
Summary:	C++ Implementation of W3C security standards for XML

Group:		System/Libraries
License:	ASL 2.0
URL:		http://santuario.apache.org/c/
Source:		http://santuario.apache.org/dist/c-library/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

# xalan-c-devel
BuildRequires:	xerces-c-devel 
BuildRequires:	openssl-devel

%description
The xml-security-c library is a C++ implementation of the XML Digital Signature
specification. The library makes use of the Apache XML project's Xerces-C XML
Parser and Xalan-C XSLT processor. The latter is used for processing XPath and
XSLT transforms.

# xalan-c-devel
%package	devel
Summary:	Development files for xml-security-c
Group:		System/Libraries
Requires:	%{name} = %{version}
Requires:	xerces-c-devel
Requires:	openssl-devel
# There are a number of headers that can use NSS if HAVE_NSS is set to 1
# Current build does not set it (configure does not even check for NSS)
# so we do not include this dependency for now.
# Requires:	nss-devel

%description	devel
This package provides development files for xml-security-c, a C++ library for
XML Digital Signatures.


%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%check
# Verify that what was compiled actually works.
./bin/xtest

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# We do not ship .la files.
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Do not ship library test utilities. These are only needed for
# xml-security-c developers and they should have the whole source anyway.
rm -rf $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libxml-security-c.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/xsec
%{_libdir}/libxml-security-c.so
