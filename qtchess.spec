
Summary:	QtChess
Summary(pl.UTF-8):	Szachy napisane w Qt
Name:		qtchess
Version:	2.05
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtchess/%{name}%{version}.d.tar
# Source0-md5:	0aed29e2c8eb4c24f4a16861962b5228
URL:		http://qtchess.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtChess is the world's least powerful peer-to-peer Chess program.
Written in C++, it has a 2-D Qt/OpenGL user interface and utilizes
TCP/IP for communications.

#%description -l pl.UTF-8

%prep
%setup -q -n scsi/backup/backup.d/%{name}2.d/

%build
export QTDIR=%{_prefix}
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install qtchess $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtchess
