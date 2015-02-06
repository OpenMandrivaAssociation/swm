%define	relver	1.2.3

Summary:	A small window manager for X11
Name:		swm
Version:	1.2.5
Release:	14
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.informatik.hu-berlin.de/prog/swm.html
Source0:	http://www.informatik.hu-berlin.de/prog/%{name}-%{relver}-src.tar.bz2
Patch0:		swm-makefile.fix.relocate.patch
Patch1:		swm-1.2.3-link.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)

%description
Swm is a small window manager for X11 designed for very small laptop-screens
with a resolution of 640x400 pixels and above. (Or with PDA-mode 
320x240) SWM is even smaller than a rxvt!

%files
%{_bindir}/*
%{_mandir}/man1/*
%doc TODO README LIESMICH COMPILE_PARAMS AUTHORS README.iPaq COPYING
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/*
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{relver}-src
%patch0 -p0 -b .dir
%patch1 -p0

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

