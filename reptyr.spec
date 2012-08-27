Name:           reptyr
Version:        0.4
Release:        1%{?dist}
Summary:        Attach a running process to a new terminal

Group:          Applications/System
License:        MIT
URL:            http://github.com/nelhage/reptyr
# https://github.com/nelhage/reptyr/tags
Source0:        nelhage-reptyr-reptyr-0.4-0-g28ca686.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:  %{ix86} x86_64 %{arm}

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal.  Started a long-running process over
ssh, but have to leave and don't want to interrupt it?  Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.


%prep
%setup -q -n nelhage-reptyr-57f9561


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX="%{_prefix}" DESTDIR="$RPM_BUILD_ROOT"
%find_lang %{name} --with-man


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING NOTES README.md
%{_bindir}/reptyr
%{_mandir}/man1/reptyr.1*


%changelog
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
