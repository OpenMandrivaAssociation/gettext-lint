Name: gettext-lint
Summary: Gettext linting tools
Version: 0.4
Release: %mkrel 4
License: GPL
URL: http://gettext-lint.sourceforge.net/
Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
Patch0: gettext-lint-0.4-check_formats.patch
Group: Development/Other
Requires: gettext
BuildArchitectures: noarch
BuildRequires: python-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The gettext lint tools are a collection of tools for checking the validity,
consistency and spelling of PO and POT files.
An experimental glossary building tool is also included.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/POFileChecker
%{_bindir}/POFileClean
%{_bindir}/POFileConsistency
%{_bindir}/POFileEquiv
%{_bindir}/POFileFill
%{_bindir}/POFileGlossary
%{_bindir}/POFileSpell
%{_bindir}/POFileStatus
%{_mandir}/man1/POFileChecker.1*
%{_mandir}/man1/POFileClean.1*
%{_mandir}/man1/POFileConsistency.1*
%{_mandir}/man1/POFileEquiv.1*
%{_mandir}/man1/POFileFill.1*
%{_mandir}/man1/POFileGlossary.1*
%{_mandir}/man1/POFileSpell.1*
%{_mandir}/man1/POFileStatus.1*
%{_datadir}/%{name}
%doc README NEWS AUTHORS

