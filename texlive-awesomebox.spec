Name:		texlive-awesomebox
Version:	57349
Release:	1
Summary:	Draw admonition blocks in your documents, illustrated with FontAwesome icons
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/awesomebox
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/awesomebox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/awesomebox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Awesome Boxes is all about drawing admonition blocks around
text to inform or alert readers about something particular. The
specific aim of this package is to use FontAwesome icons to
ease the illustration of these blocks. The package depends on
fontawesome5, xcolor, array and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/awesomebox
%doc %{_texmfdistdir}/doc/latex/awesomebox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
