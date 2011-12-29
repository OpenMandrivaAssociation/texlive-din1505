# revision 19441
# category Package
# catalog-ctan /biblio/bibtex/contrib/german/din1505
# catalog-date 2008-11-25 15:33:33 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-din1505
Version:	20081125
Release:	1
Summary:	Bibliography styles for German texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/german/din1505
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/din1505.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/din1505.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of bibliography styles that conformt to DIN 1505, and
match the original BibTeX standard set (plain, unsrt, alpha and
abbrv), together with a style natdin to work with natbib.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/din1505/abbrvdin.bst
%{_texmfdistdir}/bibtex/bst/din1505/alphadin.bst
%{_texmfdistdir}/bibtex/bst/din1505/natdin.bst
%{_texmfdistdir}/bibtex/bst/din1505/plaindin.bst
%{_texmfdistdir}/bibtex/bst/din1505/unsrtdin.bst
%doc %{_texmfdistdir}/doc/latex/din1505/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/din1505/leitbild.bib
%doc %{_texmfdistdir}/doc/latex/din1505/natbib.cfg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
