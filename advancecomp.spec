%define name	advancecomp
%define version	1.15
%define release	%mkrel 2

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


