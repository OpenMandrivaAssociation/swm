%define	ver	1.2.5
%define	relver	1.2.3
%define	rel	%mkrel 10
%define	name	swm

Name:		%{name}
Version:	%{ver}
Release:	%{rel}
License:	GPL
URL:		http://www.informatik.hu-berlin.de/prog/swm.html
Source0:	http://www.informatik.hu-berlin.de/prog/%{name}-%{relver}-src.tar.bz2
Patch0:		swm-makefile.fix.relocate.patch
Patch1:		swm-1.2.3-link.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

make PREFIX=$RPM_BUILD_ROOT%{_prefix} install

#install -D -m 644 PATCHES/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{ver}/PATCHES

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d
cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d/12swm
NAME=Swm
DESC=Swm Window manager
EXEC=%{_bindir}/startswm
SCRIPT:
exec %{_bindir}/startswm
EOF

%clean 
rm -rf $RPM_BUIlD_ROOT

%post
%{make_session}

%postun
%{make_session}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%doc TODO README LIESMICH COMPILE_PARAMS AUTHORS README.iPaq COPYING
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/*
%{_datadir}/%{name}
