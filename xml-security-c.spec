Name:		xml-security-c
Version:	1.5.1
Release:	%mkrel 4
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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-4mdv2011.0
+ Revision: 615681
- the mass rebuild of 2010.1 packages

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 1.5.1-3mdv2010.1
+ Revision: 533624
- rebuild

* Tue Feb 02 2010 Funda Wang <fwang@mandriva.org> 1.5.1-2mdv2010.1
+ Revision: 499659
- rebuild

* Wed Dec 16 2009 Sander Lepik <sander85@mandriva.org> 1.5.1-1mdv2010.1
+ Revision: 479581
- spec corrected
- import xml-security-c


* Fri Nov 20 2009 Sander Lepik <sander.lepik@eesti.ee> - 1.5.1
- Initial release for Mandriva

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.5.1-2
- rebuilt with new openssl

* Tue Jul 28 2009 Antti Andreimann <Antti.Andreimann@mail.ee> 1.5.1-1
- New upstream relase (#513078)
- Fixes CVE-2009-0217 (#511915)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Antti Andreimann <Antti.Andreimann@mail.ee> - 1.5.0-1
- New upstream release

* Tue Apr 28 2009 Antti Andreimann <Antti.Andreimann@mail.ee> - 1.4.0-2
- Execute sed magic against configure instead of configure.ac to 
  avoid calling autotools
- Removed build dependency on autotools.
- Do not ship test binaries (not needed for end-users)
- Added proper dependencies for devel sub-package
- Added CPPROG="cp -p" to preserve header file timestamps.

* Mon Mar 30 2009 Antti Andreimann <Antti.Andreimann@mail.ee> - 1.4.0-1
- Initial RPM release.

