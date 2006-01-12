%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	LanguageDetect
%define		_status		alpha
%define		_pearname	Text_LanguageDetect

Summary:	%{_pearname} - language detection class
Summary(pl):	%{_pearname} - klasa do okre�lania j�zyka
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	150bfb39fb13b49934a7a110691c66b5
URL:		http://pear.php.net/package/Text_LanguageDetect/
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
Text_LanguageDetect potrafi zidentyfikowa� 52 ludzkie j�zyki z pr�bek
tekstu i zwr�ci� list� najbardziej prawdopodobnych rezultat�w.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{docs/example_clui.php,docs/example_web.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/LanguageDetect.php
%{php_pear_dir}/data/Text_LanguageDetect/lang.dat
