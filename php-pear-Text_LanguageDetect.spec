%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	LanguageDetect
%define		_status		alpha
%define		_pearname	Text_LanguageDetect

Summary:	%{_pearname} - language detection class
Summary(pl):	%{_pearname} - klasa do okre¶lania jêzyka
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	76243ad353743b15c5257fc17f63ab5a
Patch0:		Text_LanguageDetect.patch
URL:		http://pear.php.net/package/Text_LanguageDetect/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.0.3
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_LanguageDetect can identify 52 human languages from text samples
and return confidence scores for each.

In PEAR status of this package is: %{_status}.

%description -l pl
Text_LanguageDetect potrafi zidentyfikowaæ 52 ludzkie jêzyki z próbek
tekstu i zwróciæ listê najbardziej prawdopodobnych rezultatów.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1

mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/{docs/example_clui.php,docs/example_web.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/LanguageDetect.php
%dir %{php_pear_dir}/Text/LanguageDetect
%{php_pear_dir}/Text/LanguageDetect/Parser.php

%{php_pear_dir}/data/Text_LanguageDetect

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
