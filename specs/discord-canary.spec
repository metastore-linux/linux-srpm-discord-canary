%global debug_package %{nil}

%define install_dir /opt/discord-canary
%define apps_dir    /usr/share/applications

Name:               discord-canary
Version:            0.0.52
Release:            1%{?dist}
Summary:            Free Voice and Text Chat for Gamers
Group:              Applications/Internet
License:            Proprietary
URL:                https://discordapp.com/

Source0:            https://discordapp.com/api/download/canary?platform=linux&format=tar.gz#/%{name}-%{version}.tar.gz
Source1:            discord.desktop

BuildRequires:      libXScrnSaver libcxx
Requires:           libXScrnSaver libcxx
AutoReqProv:        no

%description
All-in-one voice and text chat for gamers that’s free, secure, and works on both your desktop and phone.
It’s time to ditch Skype and TeamSpeak.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep
%autosetup -n DiscordCanary

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{install_dir}
mkdir -p $RPM_BUILD_ROOT%{apps_dir}

cp -r * $RPM_BUILD_ROOT%{install_dir}/
ln -sf %{install_dir}/DiscordCanary $RPM_BUILD_ROOT%{_bindir}/
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

%post
cd %{install_dir}
sh postinst.sh

%files
%defattr(-,root,root)
%{install_dir}/
%{_bindir}/DiscordCanary
%{apps_dir}/discord.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jul 6 2018 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.52-1
- Update to discord-canary-0.0.52

* Tue Jan 9 2018 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.45-1
- Update to discord-canary-0.0.45

* Fri Dec 22 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.44-1
- Update to discord-canary-0.0.44

* Thu Dec 21 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.42-1
- Update to discord-canary-0.0.42

* Wed Dec 20 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.41-1
- Update to discord-canary-0.0.41

* Tue Dec 19 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.39-1
- Update to discord-canary-0.0.39

* Sat Dec 16 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.36-1
- Update to discord-canary-0.0.36

* Thu Dec 14 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.35-1
- Update to discord-canary-0.0.35

* Thu Dec 14 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.34-1
- Update to discord-canary-0.0.34

* Wed Dec 13 2017 Kitsune Solar <kitsune.solar@gmail.com> - 0.0.32-1
- Initial build (using discord-canary-0.0.32)
