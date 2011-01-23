%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Text_LanguageDetect
Summary:	%{_pearname} - language detection class
Summary(pl.UTF-8):	%{_pearname} - klasa do określania języka
Name:		php-pear-%{_pearname}
Version:	0.2.3
Release:	3
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	551092304e74624972f86e5b7e18a0ca
URL:		http://pear.php.net/package/Text_LanguageDetect/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.0.3
Requires:	php-pcre
Requires:	php-pear
Suggests:	php-mbstring
Obsoletes:	php-pear-Text_LanguageDetect-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_LanguageDetect can identify 52 human languages from text samples
and return confidence scores for each.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Text_LanguageDetect potrafi zidentyfikować 52 ludzkie języki z próbek
tekstu i zwrócić listę najbardziej prawdopodobnych rezultatów.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

install -d examples
mv docs/%{_pearname}/docs/example_* examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/LanguageDetect.php
%dir %{php_pear_dir}/Text/LanguageDetect
%{php_pear_dir}/Text/LanguageDetect/Parser.php

%{php_pear_dir}/data/Text_LanguageDetect

%{_examplesdir}/%{name}-%{version}
