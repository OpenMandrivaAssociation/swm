%define	relver	1.2.3

Name:		swm
Version:	1.2.5
Release:	11
License:	GPL
URL:		http://www.informatik.hu-berlin.de/prog/swm.html
Source0:	http://www.informatik.hu-berlin.de/prog/%{name}-%{relver}-src.tar.bz2
Patch0:		swm-makefile.fix.relocate.patch
Patch1:		swm-1.2.3-link.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
Group:		Graphical desktop/Other
Summary:	A small window manager for X11

%description 
Swm is a small window manager for X11 designed for very small laptop-screens
with a resolution of 640x400 pixels and above. (Or with PDA-mode 
320x240) SWM is even smaller than a rxvt!

%prep
%setup -q -n %{name}-%{relver}-src
%patch0 -p0 -b .dir
%patch1 -p0

%build
%make CFLAGS="%optflags" CC="gcc %ldflags"

%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

make PREFIX=%{buildroot}%{_prefix} install

#install -D -m 644 PATCHES/* %{buildroot}%{_docdir}/%{name}-%{ver}/PATCHES

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat << EOF > %{buildroot}%{_sysconfdir}/X11/wmsession.d/12swm
NAME=Swm
DESC=Swm Window manager
EXEC=%{_bindir}/startswm
SCRIPT:
exec %{_bindir}/startswm
EOF


%files
%{_bindir}/*
%{_mandir}/man1/*
%doc TODO README LIESMICH COMPILE_PARAMS AUTHORS README.iPaq COPYING
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/*
%{_datadir}/%{name}


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.2.5-10mdv2011.0
+ Revision: 634642
- bunzip2 the patch
- fix linkage
- turn to regular prefix

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.2.5-9mdv2010.0
+ Revision: 434250
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.2.5-8mdv2009.0
+ Revision: 261308
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.2.5-7mdv2009.0
+ Revision: 253946
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 12 2007 Thierry Vignaud <tv@mandriva.org> 1.2.5-5mdv2008.1
+ Revision: 118961
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import swm


* Thu Feb 26 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.5-5mdk
- own %%datadir/swm

* Sat Sep 06 2003 Marcel Pol <mpol@gmx.net> 1.2.5-4mdk
- buildrequires

* Sun Jul 13 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.5-3mdk
- cosmetics
- rebuild
- quiet setup
- use $RPM_OPT_FLAGS

* Wed Oct 17 2001 Daouda LO <daouda@mandrakesoft.com> 1.2.5-2mdk
- s/Copyright/License
- right permissions on file 

* Sun Sep  2 2001 Daouda LO <daouda@mandrakesoft.com> 1.2.5-1mdk
- release 1.2.5

* Wed Apr 11 2001  Daouda Lo <daouda@mandrakesoft.com> 1.2.4-2mdk
- add Wmsession . 

* Wed Apr 11 2001  Daouda Lo <daouda@mandrakesoft.com> 1.2.4-1mdk
- release ( bug fixes )

*Thu Feb 01 2001 Daouda Lo <daouda@mandrakesoft.com> 1.2.2-1mdk
- first mdk release  
