%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     ryzen-smu
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  A Linux kernel driver that exposes access to the SMU
License:  GPLv2
URL:      https://github.com/ublue-os/ryzen_smu

VCS:      {{{ git_dir_vcs }}}
Source:   {{{ git_dir_pack }}}

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros
BuildRequires: make
BuildRequires: gcc

%description
A Linux kernel driver that exposes access to the SMU (System Management Unit) for certain AMD Ryzen Processors

%prep
{{{ git_dir_setup_macro }}}

%build
make -C userspace

%install
mkdir -p %{buildroot}%{_bindir}
mv userspace/monitor_cpu %{buildroot}%{_bindir}/monitor_cpu

%files
%{_bindir}/monitor_cpu
%doc README.md
%license LICENSE

%changelog
{{{ git_dir_changelog }}}
