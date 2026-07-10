%global tl_name awesomebox
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Draw admonition blocks in your documents, illustrated with FontAwesome icons
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/awesomebox
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/awesomebox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/awesomebox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Awesome Boxes is all about drawing admonition blocks around text to
inform or alert readers about something particular. The specific aim of
this package is to use FontAwesome icons to ease the illustration of
these blocks. The package depends on fontawesome5, xcolor, array and
xparse.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/awesomebox
%dir %{_datadir}/texmf-dist/tex/latex/awesomebox
%doc %{_datadir}/texmf-dist/doc/latex/awesomebox/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/awesomebox/README.md
%doc %{_datadir}/texmf-dist/doc/latex/awesomebox/awesomebox.pdf
%doc %{_datadir}/texmf-dist/doc/latex/awesomebox/awesomebox.tex
%{_datadir}/texmf-dist/tex/latex/awesomebox/awesomebox.sty
