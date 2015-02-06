Name: gettext-lint
Summary: Gettext linting tools
Version: 0.4
Release: 7
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



%changelog
* Tue Sep 13 2011 Götz Waschk <waschk@mandriva.org> 0.4-6mdv2012.0
+ Revision: 699630
- rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2011.0
+ Revision: 437671
- rebuild

* Fri Mar 27 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.4-4mdv2009.1
+ Revision: 361644
- added a patch to make POFileChecker also check for format strings
- moved auto* to %%build

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.4-3mdv2009.0
+ Revision: 240746
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 0.4-1mdv2008.0
+ Revision: 55227
- new version
- update file list
- fix build


* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.3.1-3mdk
- Rebuild

* Mon Feb 13 2006 Götz Waschk <waschk@mandriva.org> 0.3.1-2mdk
- Rebuild
- use mkrel

* Fri Feb 11 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.3.1-1mdk
- update file list
- New release 0.3.1

* Thu Nov 25 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.3.0-1mdk
- initial mdk package

