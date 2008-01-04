#
# TODO:
# - .desktop file as Source1
#

Summary:	QtChess - chess program with Qt user interface
Summary(pl.UTF-8):	QtChess - szachy z interfejsem użytkownika opartym na Qt
Name:		qtchess
Version:	3.03
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtchess/%{name}%{version}.d.tar
# Source0-md5:	722261e380f701b0c8ba8d0466dffd9d
URL:		http://qtchess.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtChess is the world's least powerful peer-to-peer Chess program.
Written in C++, it has a 2D Qt/OpenGL user interface and utilizes
TCP/IP for communications.

%description -l pl.UTF-8
QtChess to program szachowy peer-to-peer o najmniejszych możliwościach
na świecie. Jest napisany w C++, ma dwuwymiarowy interfejs użytkownika
Qt/OpenGL i wykorzystuje do komunikacji protokół TCP/IP.

%prep
%setup -q -c

%build
cd %{name}3.d
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}3.d/qtchess $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtchess
