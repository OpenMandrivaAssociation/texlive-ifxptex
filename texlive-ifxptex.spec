%global tl_name ifxptex
%global tl_revision 46153

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Detect pTeX and its derivatives
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/ifxptex
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifxptex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ifxptex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands for detecting pTeX and its derivatives
(e-pTeX, upTeX, e-upTeX, and ApTeX). Both LaTeX and plain TeX are
supported.

