%if 0%{?fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           reptyr
Version:        0.6.2
Release:        9%{?dist}
Summary:        Attach a running process to a new terminal

Group:          Applications/System
License:        MIT
URL:            http://github.com/nelhage/reptyr
# https://github.com/nelhage/reptyr/tags
Source0:        https://github.com/nelhage/reptyr/archive/%{name}-%{version}.tar.gz
Patch0:         https://github.com/nelhage/reptyr/commit/fa0d63ff8c488be15976e5353580b565e85586a1.patch
Patch1:         https://github.com/nelhage/reptyr/commit/b45fd9238958fcf2d8f3d6fc23e6d491febea2ac.patch

ExclusiveArch:  %{ix86} x86_64 %{arm}
%if %{with tests}
BuildRequires:  %{_bindir}/python
BuildRequires:  python-pexpect
# https://github.com/nelhage/reptyr/issues/69
BuildRequires:  kernel-headers >= 3.4
%endif

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal.  Started a long-running process over
ssh, but have to leave and don't want to interrupt it?  Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.


%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1 -F 2


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX="%{_prefix}" DESTDIR="$RPM_BUILD_ROOT"
%find_lang %{name} --with-man


%if %{with tests}
%check
make test CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc ChangeLog NOTES README.md
%{_bindir}/reptyr
%{_mandir}/man1/reptyr.1*


%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.6.2-6
- Apply upstream gcc7 build fixes (#1424256)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.6.2-3
- Remove unnecessary %%defattr
- Disable tests on EL (python-pexpect N/A, too old kernel-headers on 5 and 6)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb  1 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.2-1
- Update to 0.6.2

* Wed Jan 21 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-1
- Update to 0.6.1
- Mark license files as %%license where available

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5-1
- Update to 0.5.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4-1
- Update to 0.4.
- Link with $RPM_LD_FLAGS.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.3-1
- Update to 0.3.

* Fri Mar 11 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.2-2.20110311git919fff7
- Update to git revision 919fff7, fixes crash with invalid arguments.

* Sat Mar  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.2-1
- First build.
