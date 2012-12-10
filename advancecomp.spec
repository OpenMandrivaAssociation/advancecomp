%define name	advancecomp
%define version	1.15
%define release	%mkrel 6

Summary:	The AdvanceCOMP compression
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Archiving/Compression
URL:		http://advancemame.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	mencoder
BuildRequires:	groff
BuildRequires:  zlib-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
AdvanceCOMP contains recompression utilities for your .zip
archives, .png images, .mng video clips and .gz files.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x

# this does not work
#    --enable-bzip2

%make

make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING HISTORY INSTALL README doc/*.html doc/*.txt
%attr(0755,root,root) %{_bindir}/advzip
%attr(0755,root,root) %{_bindir}/advpng
%attr(0755,root,root) %{_bindir}/advmng
%attr(0755,root,root) %{_bindir}/advdef
%{_mandir}/man1/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.15-6mdv2011.0
+ Revision: 616502
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.15-5mdv2010.0
+ Revision: 423971
- rebuild

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.15-4mdv2010.0
+ Revision: 423863
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.15-3mdv2009.0
+ Revision: 226128
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.15-2mdv2008.1
+ Revision: 135817
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.15-2mdv2007.0
+ Revision: 101583
- Import advancecomp

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 1.15-2mdv2007.0
- rebuild

* Tue Mar 21 2006 Lenny Cartier <lenny@mandriva.com> 1.15-1mdk
- 1.15

* Fri Oct 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.14-2mdk
- Fix BuildRequires
- %%mkrel

* Mon Sep 19 2005 Pascal Terjan <pterjan@mandriva.org> 1.14-1mdk
- 1.14
- fix build on 64 bits (P0 from Fedora)

* Fri Jan 14 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.13-1mdk
- initial mandrake package

