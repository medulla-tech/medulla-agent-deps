%global __provides_exclude_from ^%_var/lib/tomcat/webapps/guacamole/classpath/.*$

%define use_git                1
%define git                    SHA

Summary:	Dependancies needed for pulse windows agent
Name:		medulla-agent-deps
Version:	3.0
%if ! %use_git
Release:        0%{?dist}
%else
Release:        0.%git.1%{?dist}
%endif
Source0:	%{name}-%{version}.tar.gz
Source1:    https://agents.siveo.net/3.0/win/downloads/python-3.11.7-amd64.exe
Source2:    https://agents.siveo.net/3.0/win/downloads/libcurl4-8.0.1-1.tar.xz
Source3:    https://agents.siveo.net/3.0/win/downloads/cwrsync_6.2.8_x64_free.zip
Source4:    https://agents.siveo.net/3.0/win/downloads/LGPO.zip
Source5:    https://agents.siveo.net/3.0/win/downloads/OpenSSH-Win64.zip
Source6:    https://agents.siveo.net/3.0/win/downloads/fusioninventory-agent_windows-x64_2.6.exe
Source7:    https://agents.siveo.net/3.0/win/downloads/tightvnc-2.8.81-gpl-setup-64bit.msi
Source8:    https://agents.siveo.net/3.0/win/downloads/syncthing-windows-amd64-v1.23.4.zip
Source9:    https://agents.siveo.net/3.0/win/downloads/bootstrap.js
Source10:   https://agents.siveo.net/3.0/win/downloads/bootstrap.css
Source11:   https://agents.siveo.net/3.0/win/downloads/jquery-3.6.4.js
Source12:   https://agents.siveo.net/3.0/win/downloads/jquery-ui.css
Source13:   https://agents.siveo.net/3.0/win/downloads/jquery-ui.js
Source14:   https://agents.siveo.net/3.0/win/downloads/jquery.dataTables.css
Source15:   https://agents.siveo.net/3.0/win/downloads/jquery.dataTables.js
Source16:   https://agents.siveo.net/3.0/win/downloads/glyphicons-halflings-regular.woff
Source17:   https://agents.siveo.net/3.0/win/downloads/style.css
Source18:   https://agents.siveo.net/3.0/win/downloads/script.js
Source19:   https://agents.siveo.net/3.0/win/downloads/UrBackup_Client_2.5.25.exe
Source20:   https://agents.siveo.net/3.0/win/downloads/paexec_1_29.exe
Source22:   https://agents.siveo.net/3.0/win/downloads/GLPI-Agent-1.5-x64.msi
Source23:   https://agents.siveo.net/3.0/win/downloads/vim.exe

Source100:  https://agents.siveo.net/3.0/win/downloads/python_modules/pypiwin32-223-py3-none-any.whl
Source101:  https://agents.siveo.net/3.0/win/downloads/python_modules/pywin32-306-cp311-cp311-win_amd64.whl
Source102:  https://agents.siveo.net/3.0/win/downloads/python_modules/netifaces2-0.0.18-cp37-abi3-win_amd64.whl
Source103:  https://agents.siveo.net/3.0/win/downloads/python_modules/comtypes-1.1.14-py2.py3-none-any.whl
Source104:  https://agents.siveo.net/3.0/win/downloads/python_modules/slixmpp-1.8.4.tar.gz
Source105:  https://agents.siveo.net/3.0/win/downloads/python_modules/aiodns-3.0.0-py3-none-any.whl
Source106:  https://agents.siveo.net/3.0/win/downloads/python_modules/pyasn1-0.5.0-py2.py3-none-any.whl
Source107:  https://agents.siveo.net/3.0/win/downloads/python_modules/pyasn1_modules-0.3.0-py2.py3-none-any.whl
Source108:  https://agents.siveo.net/3.0/win/downloads/python_modules/pycares-4.3.0-cp311-cp311-win_amd64.whl
Source109:  https://agents.siveo.net/3.0/win/downloads/python_modules/cffi-1.15.1-cp311-cp311-win_amd64.whl
Source110:  https://agents.siveo.net/3.0/win/downloads/python_modules/pycparser-2.21-py2.py3-none-any.whl
Source111:  https://agents.siveo.net/3.0/win/downloads/python_modules/WMI-1.5.1-py2.py3-none-any.whl
Source112:  https://agents.siveo.net/3.0/win/downloads/python_modules/pycurl-7.45.1-cp311-cp311-win_amd64.whl
Source113:  https://agents.siveo.net/3.0/win/downloads/python_modules/lxml-4.9.2-cp311-cp311-win_amd64.whl
Source114:  https://agents.siveo.net/3.0/win/downloads/python_modules/pycryptodome-3.18.0-cp35-abi3-win_amd64.whl
Source115:  https://agents.siveo.net/3.0/win/downloads/python_modules/croniter-1.3.14-py2.py3-none-any.whl
Source116:  https://agents.siveo.net/3.0/win/downloads/python_modules/python_dateutil-2.8.2-py2.py3-none-any.whl
Source117:  https://agents.siveo.net/3.0/win/downloads/python_modules/six-1.16.0-py2.py3-none-any.whl
Source118:  https://agents.siveo.net/3.0/win/downloads/python_modules/psutil-5.9.5-cp36-abi3-win_amd64.whl
Source119:  https://agents.siveo.net/3.0/win/downloads/python_modules/PyQt6-6.6.1-cp38-abi3-win_amd64.whl
Source120:  https://agents.siveo.net/3.0/win/downloads/python_modules/PyQt6_sip-13.6.0-cp311-cp311-win_amd64.whl
Source121:  https://agents.siveo.net/3.0/win/downloads/python_modules/PyQt6_Qt6-6.6.1-py3-none-win_amd64.whl
Source122:  https://agents.siveo.net/3.0/win/downloads/python_modules/sip-6.8.1-py3-none-any.whl
Source123:  https://agents.siveo.net/3.0/win/downloads/python_modules/packaging-23.1-py3-none-any.whl
Source124:  https://agents.siveo.net/3.0/win/downloads/python_modules/ply-3.11-py2.py3-none-any.whl
Source125:  https://agents.siveo.net/3.0/win/downloads/python_modules/toml-0.10.2-py2.py3-none-any.whl
Source126:  https://agents.siveo.net/3.0/win/downloads/python_modules/pyparsing-3.0.9-py3-none-any.whl
Source128:  https://agents.siveo.net/3.0/win/downloads/python_modules/paramiko-3.1.0-py3-none-any.whl
Source129:  https://agents.siveo.net/3.0/win/downloads/python_modules/PyNaCl-1.5.0-cp36-abi3-win_amd64.whl
Source130:  https://agents.siveo.net/3.0/win/downloads/python_modules/bcrypt-4.0.1-cp36-abi3-win_amd64.whl
Source131:  https://agents.siveo.net/3.0/win/downloads/python_modules/cryptography-41.0.2-cp37-abi3-win_amd64.whl
Source132:  https://agents.siveo.net/3.0/win/downloads/python_modules/ecdsa-0.18.0-py2.py3-none-any.whl
Source133:  https://agents.siveo.net/3.0/win/downloads/python_modules/syncthing2-2.4.4-py3-none-any.whl
Source134:  https://agents.siveo.net/3.0/win/downloads/python_modules/requests-2.28.2-py3-none-any.whl
Source135:  https://agents.siveo.net/3.0/win/downloads/python_modules/charset_normalizer-3.1.0-cp311-cp311-win_amd64.whl
Source136:  https://agents.siveo.net/3.0/win/downloads/python_modules/certifi-2022.12.7-py3-none-any.whl
Source137:  https://agents.siveo.net/3.0/win/downloads/python_modules/idna-3.4-py3-none-any.whl
Source138:  https://agents.siveo.net/3.0/win/downloads/python_modules/urllib3-1.26.15-py2.py3-none-any.whl
Source139:  https://agents.siveo.net/3.0/win/downloads/python_modules/chardet-5.1.0-py3-none-any.whl
Source140:  https://agents.siveo.net/3.0/win/downloads/python_modules/pathlib-1.0.1-py3-none-any.whl
Source141:  https://agents.siveo.net/3.0/win/downloads/python_modules/CherryPy-18.8.0-py2.py3-none-any.whl
Source142:  https://agents.siveo.net/3.0/win/downloads/python_modules/autocommand-2.2.2-py3-none-any.whl
Source143:  https://agents.siveo.net/3.0/win/downloads/python_modules/cheroot-9.0.0-py2.py3-none-any.whl
Source144:  https://agents.siveo.net/3.0/win/downloads/python_modules/inflect-6.0.4-py3-none-any.whl
Source145:  https://agents.siveo.net/3.0/win/downloads/python_modules/jaraco.classes-3.2.3-py3-none-any.whl
Source146:  https://agents.siveo.net/3.0/win/downloads/python_modules/jaraco.collections-4.1.0-py3-none-any.whl
Source147:  https://agents.siveo.net/3.0/win/downloads/python_modules/jaraco.context-4.3.0-py3-none-any.whl
Source148:  https://agents.siveo.net/3.0/win/downloads/python_modules/jaraco.functools-3.6.0-py3-none-any.whl
Source149:  https://agents.siveo.net/3.0/win/downloads/python_modules/jaraco.text-3.11.1-py3-none-any.whl
Source150:  https://agents.siveo.net/3.0/win/downloads/python_modules/more_itertools-9.1.0-py3-none-any.whl
Source151:  https://agents.siveo.net/3.0/win/downloads/python_modules/portend-3.1.0-py3-none-any.whl
Source152:  https://agents.siveo.net/3.0/win/downloads/python_modules/pydantic-1.10.7-cp311-cp311-win_amd64.whl
Source153:  https://agents.siveo.net/3.0/win/downloads/python_modules/pytz-2023.3-py2.py3-none-any.whl
Source154:  https://agents.siveo.net/3.0/win/downloads/python_modules/tempora-5.2.2-py3-none-any.whl
Source155:  https://agents.siveo.net/3.0/win/downloads/python_modules/typing_extensions-4.5.0-py3-none-any.whl
Source156:  https://agents.siveo.net/3.0/win/downloads/python_modules/zc.lockfile-3.0.post1-py3-none-any.whl
Source157:  https://agents.siveo.net/3.0/win/downloads/python_modules/Routes-2.5.1-py2.py3-none-any.whl
Source158:  https://agents.siveo.net/3.0/win/downloads/python_modules/repoze.lru-0.7-py3-none-any.whl
Source159:  https://agents.siveo.net/3.0/win/downloads/python_modules/simplejson-3.19.1-py3-none-any.whl
Source160:  https://agents.siveo.net/3.0/win/downloads/python_modules/WebOb-1.8.7-py2.py3-none-any.whl
Source161:  https://agents.siveo.net/3.0/win/downloads/python_modules/pypiwin32-223-py3-none-any.whl
Source162:  https://agents.siveo.net/3.0/win/downloads/python_modules/PyYAML-6.0.1-cp311-cp311-win_amd64.whl
Source163:  https://agents.siveo.net/3.0/win/downloads/python_modules/netaddr-0.8.0-py2.py3-none-any.whl
Source164:  https://agents.siveo.net/3.0/win/downloads/python_modules/wheel-0.42.0-py3-none-any.whl

Source200:	https://agents.siveo.net/3.0/lin/downloads/bootstrap.js
Source201:	https://agents.siveo.net/3.0/lin/downloads/bootstrap.css
Source202:	https://agents.siveo.net/3.0/lin/downloads/jquery-3.6.4.js
Source203:	https://agents.siveo.net/3.0/lin/downloads/jquery-ui.css
Source204:	https://agents.siveo.net/3.0/lin/downloads/jquery-ui.js
Source205:	https://agents.siveo.net/3.0/lin/downloads/jquery.dataTables.css
Source206:	https://agents.siveo.net/3.0/lin/downloads/jquery.dataTables.js
Source207:	https://agents.siveo.net/3.0/lin/downloads/glyphicons-halflings-regular.woff
Source208:	https://agents.siveo.net/3.0/lin/downloads/style.css
Source209:	https://agents.siveo.net/3.0/lin/downloads/script.js
Source210:	https://agents.siveo.net/3.0/lin/downloads/UrBackup_Client_Linux_2.5.25.sh


Source300:	https://agents.siveo.net/3.0/mac/downloads/bootstrap.js
Source301:	https://agents.siveo.net/3.0/mac/downloads/bootstrap.css
Source302:	https://agents.siveo.net/3.0/mac/downloads/jquery-3.6.4.js
Source303:	https://agents.siveo.net/3.0/mac/downloads/jquery-ui.css
Source304:	https://agents.siveo.net/3.0/mac/downloads/jquery-ui.js
Source305:	https://agents.siveo.net/3.0/mac/downloads/jquery.dataTables.css
Source306:	https://agents.siveo.net/3.0/mac/downloads/jquery.dataTables.js
Source307:	https://agents.siveo.net/3.0/mac/downloads/glyphicons-halflings-regular.woff
Source308:	https://agents.siveo.net/3.0/mac/downloads/style.css
Source309:	https://agents.siveo.net/3.0/mac/downloads/script.js

Source310:  https://agents.siveo.net/3.0/mac/downloads/syncthing-macos-amd64-v1.23.4.zip
Source311:  https://agents.siveo.net/3.0/mac/downloads/VineServer-5.3.1.dmg
Source312:  https://agents.siveo.net/3.0/mac/downloads/4.0.15.tar.gz

License:	MIT
Group:		Development/Java
Url:		http://www.siveo.org/
BuildArch:	noarch

%description
Dependancies needed for pulse windows agent

%package -n pulse-xmpp-agent-deps
Summary:    Dependancies needed for pulse windows agent
Group:      System/Servers
Requires:   pulse2-common = %version-%release

Obsoletes:  pulse-kiosk-agent-deps < 3.0
Provides:   pulse-kiosk-agent-deps = %version-%release

%description -n pulse-xmpp-agent-deps
Dependancies needed for pulse windows agent


%prep
%setup -q -c

%build

%install
mkdir -p %buildroot/var/lib/pulse2/clients/win/downloads/
cp %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9 %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 %SOURCE15 %SOURCE16 %SOURCE17 %SOURCE18 %SOURCE19 %SOURCE20 %SOURCE22 %SOURCE23 %buildroot/var/lib/pulse2/clients/win/downloads/

mkdir -p %buildroot/var/lib/pulse2/clients/win/downloads/python_modules/
cp %SOURCE100 %SOURCE101 %SOURCE102 %SOURCE103 %SOURCE104 %SOURCE105 %SOURCE106 %SOURCE107 %SOURCE108 %SOURCE109 %SOURCE110 %SOURCE111 %SOURCE112 %SOURCE113 %SOURCE114 %SOURCE115 %SOURCE116 %SOURCE117 %SOURCE118 %SOURCE119 %SOURCE120 %SOURCE121 %SOURCE122 %SOURCE123 %SOURCE124 %SOURCE125 %SOURCE126 %SOURCE128 %SOURCE129 %SOURCE130 %SOURCE131 %SOURCE132 %SOURCE133 %SOURCE134 %SOURCE135 %SOURCE136 %SOURCE137 %SOURCE138 %SOURCE139 %SOURCE140 %SOURCE141 %SOURCE142 %SOURCE143 %SOURCE144 %SOURCE145 %SOURCE146 %SOURCE147 %SOURCE148 %SOURCE149 %SOURCE150 %SOURCE151 %SOURCE152 %SOURCE153 %SOURCE154 %SOURCE155 %SOURCE156 %SOURCE157 %SOURCE158 %SOURCE159 %SOURCE160 %SOURCE161 %SOURCE162 %SOURCE163 %SOURCE164 %buildroot/var/lib/pulse2/clients/win/downloads/python_modules/

mkdir -p %buildroot/var/lib/pulse2/clients/linux/downloads/
cp %SOURCE200 %SOURCE201 %SOURCE202 %SOURCE203 %SOURCE204 %SOURCE205 %SOURCE206 %SOURCE207 %SOURCE208 %SOURCE209 %SOURCE210 %buildroot/var/lib/pulse2/clients/linux/downloads/
mkdir -p %buildroot/var/lib/pulse2/clients/linux/downloads/python_modules/

mkdir -p %buildroot/var/lib/pulse2/clients/mac/downloads/
cp %SOURCE300 %SOURCE301 %SOURCE302 %SOURCE303 %SOURCE304 %SOURCE305 %SOURCE306 %SOURCE307 %SOURCE308 %SOURCE309 %SOURCE310 %SOURCE311 %SOURCE312 %buildroot/var/lib/pulse2/clients/mac/downloads/
mkdir -p %buildroot/var/lib/pulse2/clients/mac/downloads/python_modules/


%files
/var/lib/pulse2/clients/linux/downloads/
/var/lib/pulse2/clients/mac/downloads/
/var/lib/pulse2/clients/win/downloads/
