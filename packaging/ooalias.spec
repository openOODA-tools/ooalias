Name:           ooalias
Version:        0.2.0
Release:        1%{?dist}
Summary:        Cryptographically verifiable command macro and alias resolver with scope isolation.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/ooalias
Source0:        ooalias-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooalias is a sovereign, capability-bounded command macro and alias resolver written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooalias
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooalias-uninstall

%files
/usr/bin/ooalias
/usr/bin/ooalias-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to pure openOODA 0.2.0 with MCP server and multi-distro packaging parity
