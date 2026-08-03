# Tarball is swm-1.3.4c-src.tgz; top-level directory is swm-1.3.4
%define	srcdir	1.3.4

Summary:	A small window manager for X11
Name:		swm
Version:	1.3.4c
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://swm.sourceforge.net/
Source0:	https://swm.sourceforge.net/%{name}-%{version}-src.tgz
Patch0:		swm-makefile.fix.relocate.patch
Patch1:		swm-1.2.3-link.patch
BuildRequires:	make
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)

%description
Swm is a small window manager for X11 designed for very small laptop-screens
with a resolution of 640x400 pixels and above. (Or with PDA-mode 
320x240) SWM is even smaller than a rxvt!

%files
%{_bindir}/*
%{_mandir}/man1/*
%doc doc/*
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/*
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{srcdir}
%patch -P0 -p0 -b .dir
%patch -P1 -p0

%build
%make CFLAGS="%{optflags}" CC="gcc %{ldflags}"

%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

make PREFIX=%{buildroot}%{_prefix} install

mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat << EOF > %{buildroot}%{_sysconfdir}/X11/wmsession.d/12swm
NAME=Swm
DESC=Swm Window manager
EXEC=%{_bindir}/startswm
SCRIPT:
exec %{_bindir}/startswm
EOF

