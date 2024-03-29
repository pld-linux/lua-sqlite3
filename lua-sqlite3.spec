# TODO
# - missing runtime dep for parent dirs?
# - fix build problem (/usr/bin/ld: cannot find -llualib - at me ./configure says that
#   checking if we need -llualib... no
#   but at the build server say "yes"
Summary:	Lua-Sqlite3 is a binding of Sqlite3 for Lua
Summary(hu.UTF-8):	Lua-Sqlite3 Sqlite3 kapcsolódási felület Lua-hoz.
Name:		lua-sqlite3
Version:	0.4.1
Release:	2.1
License:	BSD-like
# (existing?/)new group for Lua
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/1611/%{name}-%{version}.tar.bz2
# Source0-md5:	eb14c0b5c4bf8e0052dc2d054386717a
URL:		http://lua.sqlite.org/
BuildRequires:	lua51-devel
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lua-Sqlite3 is a binding of Sqlite3 for Lua. Lua-Sqlite3 provides a
nice and smart view of the database with iterators, dynamic parameter
binding for prepared statements user functions and aggregates and so
on. It is useful when you use awesome3 with liferea or newsbeuter.

%description -l hu.UTF-8
Lua-Sqlite3 egy Sqlite3 kapcsolódási felület Lua-hoz. Hasznos lehet,
ha awesome3-at használsz liferea-val vagy newsbeuter-rel.

%prep
%setup -q

%build
%configure \
	--with-lua-includedir=%{_includedir}/lua51 \
	--with-lua=%{_bindir}/lua51 \
	--with-lua-libdir=%{_libdir}/lua/5.1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_libdir}}/lua/5.1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# TODO: patch makefile instead
mv $RPM_BUILD_ROOT%{_libdir}/lua/{*.so,5.1}
mv $RPM_BUILD_ROOT{%{_libdir}/lua/*.lua,%{_datadir}/lua/5.1}
%{__sed} -i -e 's#\(shared_lib_path =.*\)"#\1/5.1"#' $RPM_BUILD_ROOT%{_datadir}/lua/5.1/libluasqlite3-loader.lua

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README examples/* documentation.html
# XXX missing runtime dep for parent dirs?
%attr(755,root,root) %{_libdir}/lua/5.1/*.so
%{_datadir}/lua/5.1/*.lua
