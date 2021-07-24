Name:           python-httptools
Version:        0.1.2
Release:        1
Summary:        Fast HTTP parser

License:        MIT
URL:            https://github.com/MagicStack/httptools
Source0:        https://github.com/MagicStack/httptools/archive/v0.1.2/httptools-0.1.2.tar.gz

BuildRequires:  gcc
BuildRequires:  http-parser-devel

%description
httptools is a Python binding for nodejs HTTP parser.

%package -n python3-httptools
Summary:        %{summary}
%{?python_provide:%python_provide python3-httptools}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-Cython

%description -n python3-httptools
httptools is a Python binding for nodejs HTTP parser.

%prep
%autosetup -n httptools-%{version} -p1
rm -vrf vendor/
sed -i 's#../../vendor/http-parser/http_parser.h#http_parser.h#' ./httptools/parser/cparser.pxd

%build
%py3_build build_ext \--use-system-http-parser

%install
%py3_install

%check
pushd tests
  PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover -v || :
popd

%files -n python3-httptools
%license LICENSE
%doc README.md
%{python3_sitearch}/httptools-*.egg-info/
%{python3_sitearch}/httptools/

%changelog
* Wed Jul 7 2021 liuliang <liuliang1@kylinos.cn> - 0.1.2-1
- Package init
