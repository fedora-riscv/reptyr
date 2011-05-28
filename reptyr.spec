Name:           reptyr
Version:        0.3
Release:        1%{?dist}
Summary:        Attach a running process to a new terminal

Group:          Applications/System
License:        MIT
URL:            http://github.com/nelhage/reptyr
# https://github.com/nelhage/reptyr/downloads
Source0:        nelhage-reptyr-reptyr-0.3-0-g3cad834.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:  %{ix86} x86_64 %{arm}

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal.  Started a long-running process over
ssh, but have to leave and don't want to interrupt it?  Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.


%prep
%setup -q -n nelhage-reptyr-b83e8f6


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX="%{_prefix}" DESTDIR="$RPM_BUILD_ROOT"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING NOTES README
%{_bindir}/reptyr
%{_mandir}/man1/reptyr.1*

%changelog
* Sat May 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.3-1
- Update to 0.3.

* Fri Mar 11 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.2-2.20110311git919fff7
- Update to git revision 919fff7, fixes crash with invalid arguments.

* Sat Mar  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.2-1
- First build.
