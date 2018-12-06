%global goipath      github.com/10gen/escaper
%global commit       17fe61c658dcbdcbf246c783f4f7dc97efde3a8b

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Escaper lets you create your own formatting syntax
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%gosetup

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git17fe61c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 mskalick@redhat.com - 0-0.1.20180528git17fe61c
- Initial packaging for Fedora
