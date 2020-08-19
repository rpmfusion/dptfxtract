Name:           dptfxtract
Version:        1.4.3
Release:        2%{?dist}
Summary:        Utility to generate a thermald configuration from DPTF

License:        Redistributable, no modification permitted
URL:            https://github.com/intel/dptfxtract
ExclusiveArch:  x86_64
Source0:        https://github.com/intel/dptfxtract/archive/v%{version}.tar.gz
Source1:        dptfxtract.service

BuildRequires:  systemd-rpm-macros
Requires:       thermald

%{?systemd_requires}

%global debug_package %{nil}

%description
This is a companion tool to Linux Thermal Daemon (thermald). This tool tries to
reuse some of the tables used by "Intel ® Dynamic Platform and Thermal
Framework (Intel® DPTF)" by converting to the thermal_conf.xml format used by
thermald.

Integration with thermald is included so that that a thermald configuration
will be created automatically if thermald is enabled.

%prep
%autosetup

%build

%post
%systemd_post dptfxtract.service
systemctl try-restart thermald.service

%preun
%systemd_preun dptfxtract.service

%postun
%systemd_postun_with_restart dptfxtract.service

%install
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_unitdir}/thermald.service.wants
mkdir -p %{buildroot}usr/share/doc/dptfxtract

install -m 755 dptfxtract %{buildroot}%{_libexecdir}/dptfxtract
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
ln -s ../dptfxtract.service %{buildroot}%{_unitdir}/thermald.service.wants/dptfxtract.service

%files
%{_libexecdir}/dptfxtract
%{_unitdir}/dptfxtract.service
%dir %{_unitdir}/thermald.service.wants
%{_unitdir}/thermald.service.wants/dptfxtract.service
%license COPYING
%doc README.txt


%changelog
* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Benjamin Berg <bberg@redhat.com> - 1.4.3-1
- New upstream release

* Tue Feb 11 2020 Benjamin Berg <bberg@redhat.com> - 1.4.2-3
- Fix error allowing access to / by dptfxtract
- Work aound dtpfxtract trying to write to the current working directory

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 03 2019 Benjamin Berg <bberg@redhat.com> - 1.4.2-1
- New upstream release
- Permit madvise syscall (#5451)

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Benjamin Berg <bberg@redhat.com> - 1.4.1-2
- New upstream release

* Sat Jun 08 2019 Benjamin Berg <bberg@redhat.com> - 1.3-1
- Package dptfxtract (#5268)
