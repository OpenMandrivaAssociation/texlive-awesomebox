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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Awesome Boxes is all about drawing admonition blocks around text to
inform or alert readers about something particular. The specific aim of
this package is to use FontAwesome icons to ease the illustration of
these blocks. The package depends on fontawesome5, xcolor, array and
xparse.

