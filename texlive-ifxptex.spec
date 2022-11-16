Name:		texlive-ifxptex
Version:	46153
Release:	1
Summary:	Detect pTeX and its derivatives
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifxptex
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifxptex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifxptex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for detecting pTeX and its
derivatives (e-pTeX, upTeX, e-upTeX, and ApTeX). Both LaTeX and
plain TeX are supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/ifxptex
%doc %{_texmfdistdir}/doc/generic/ifxptex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
