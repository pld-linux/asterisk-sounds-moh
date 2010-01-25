Summary:	Music on Hold for Asterisk, The Open Source PBX
Name:		asterisk-sounds-moh
Version:	2.03
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-ulaw-%{version}.tar.gz
# Source0-md5:	d5107998109f3bda5f528e548dd838dc
Source1:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-alaw-%{version}.tar.gz
# Source1-md5:	386b8acb431760ea40d405fec69f67bb
Source2:	http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-moh-opsound-wav-%{version}.tar.gz
# Source2-md5:	8277e2c693fd056773b1c15e4d52077d
URL:		http://www.asterisk.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		moh_dir	%{_datadir}/asterisk/moh

%description
Asterisk is an open source PBX and telephony development platform.
Asterisk can both replace a conventional PBX and act as a platform for
the development of custom telephony applications for the delivery of
dynamic content over a telephone; similar to how one can deliver
dynamic content through a web browser using CGI and a web server.

Asterisk supports a variety of telephony hardware including BRI, PRI,
POTS, and IP telephony clients using the Inter-Asterisk eXchange (IAX)
protocol (e.g. gnophone or miniphone). For more information and a
current list of supported hardware, see <http://www.asterisk.org>

%package opsound-ulaw
Summary:	Asterisk Music on Hold - opsound - ulaw
Group:		Applications/System
Provides:	%{name} = %{version}-%{release}
Obsoletes:	asterisk-sounds-moh-fpm-ulaw

%description opsound-ulaw
This package contains Asterisk Music on Hold - opsound - ulaw.

%package opsound-alaw
Summary:	Asterisk Music on Hold - opsound - alaw
Group:		Applications/System
Provides:	%{name} = %{version}-%{release}
Obsoletes:	asterisk-sounds-moh-fpm-alaw

%description opsound-alaw
This package contains Asterisk Music on Hold - opsound - alaw.

%package opsound-wav
Summary:	Asterisk Music on Hold - opsound - wav
Group:		Applications/System
Provides:	%{name} = %{version}-%{release}
Obsoletes:	asterisk-sounds-moh-fpm-wav

%description opsound-wav
This package contains Asterisk Music on Hold - opsound - wav.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{moh_dir}

tar xf %{SOURCE0} -C $RPM_BUILD_ROOT%{moh_dir}
touch $RPM_BUILD_ROOT%{moh_dir}/.asterisk-moh-opsound-ulaw

tar xf %{SOURCE1} -C $RPM_BUILD_ROOT%{moh_dir}
touch $RPM_BUILD_ROOT%{moh_dir}/.asterisk-moh-opsound-alaw

tar xf %{SOURCE2} -C $RPM_BUILD_ROOT%{moh_dir}
touch $RPM_BUILD_ROOT%{moh_dir}/.asterisk-moh-opsound-wav

%clean
cd $RPM_BUILD_DIR

%files opsound-ulaw
%defattr(644,root,root,755)
%{moh_dir}/CHANGES-asterisk-moh-opsound-ulaw
%{moh_dir}/CREDITS-asterisk-moh-opsound-ulaw
%{moh_dir}/LICENSE-asterisk-moh-opsound-ulaw
%{moh_dir}/macroform-cold_day.ulaw
%{moh_dir}/macroform-robot_dity.ulaw
%{moh_dir}/macroform-the_simplicity.ulaw
%{moh_dir}/manolo_camp-morning_coffee.ulaw
%{moh_dir}/reno_project-system.ulaw
%{moh_dir}/.asterisk-moh-opsound-ulaw

%files opsound-alaw
%defattr(644,root,root,755)
%{moh_dir}/CHANGES-asterisk-moh-opsound-alaw
%{moh_dir}/CREDITS-asterisk-moh-opsound-alaw
%{moh_dir}/LICENSE-asterisk-moh-opsound-alaw
%{moh_dir}/macroform-cold_day.alaw
%{moh_dir}/macroform-robot_dity.alaw
%{moh_dir}/macroform-the_simplicity.alaw
%{moh_dir}/manolo_camp-morning_coffee.alaw
%{moh_dir}/reno_project-system.alaw
%{moh_dir}/.asterisk-moh-opsound-alaw

%files opsound-wav
%defattr(644,root,root,755)
%{moh_dir}/CHANGES-asterisk-moh-opsound-wav
%{moh_dir}/CREDITS-asterisk-moh-opsound-wav
%{moh_dir}/LICENSE-asterisk-moh-opsound-wav
%{moh_dir}/macroform-cold_day.wav
%{moh_dir}/macroform-robot_dity.wav
%{moh_dir}/macroform-the_simplicity.wav
%{moh_dir}/manolo_camp-morning_coffee.wav
%{moh_dir}/reno_project-system.wav
%{moh_dir}/.asterisk-moh-opsound-wav
