Summary:	The AdvanceCOMP compression
Name:		advancecomp
Version:	2.5
Release:	1
License:	GPL
Group:		Archiving/Compression
URL:		http://advancemame.sourceforge.net
Source0:	https://github.com/amadvance/advancecomp/releases/download/v%{version}/advancecomp-%{version}.tar.gz
BuildRequires:	mencoder
BuildRequires:	groff
BuildRequires:  zlib-devel

%description
AdvanceCOMP contains recompression utilities for your .zip
archives, .png images, .mng video clips and .gz files.

%prep
%autosetup -p1
%configure

%build
%make_build

%check
make check

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING HISTORY INSTALL README doc/*.txt
%attr(0755,root,root) %{_bindir}/advzip
%attr(0755,root,root) %{_bindir}/advpng
%attr(0755,root,root) %{_bindir}/advmng
%attr(0755,root,root) %{_bindir}/advdef
%{_mandir}/man1/*
