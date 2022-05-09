Name:           python-httptools
Version:        0.4.0
Release:        1
Summary:        Fast HTTP parser

License:        MIT
URL:            https://github.com/MagicStack/httptools
Source0:        https://github.com/MagicStack/httptools/archive/v0.4.0/httptools-0.4.0.tar.gz
Source1:        https://github.com/nodejs/llhttp/archive/refs/tags/release/v6.0.6.tar.gz#/llhttp-release-v6.0.6.tar.gz
Source2:        https://github.com/nodejs/http-parser/archive/refs/tags/v2.9.4.tar.gz#/http-parser-2.9.4.tar.gz

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
rm -df vendor/llhttp/
tar -xzf '%{SOURCE1}' -C vendor
mv vendor/llhttp-release*/ vendor/llhttp/
rm -df vendor/http-parser/
tar -xzf '%{SOURCE2}' -C vendor
mv vendor/http-parser*/ vendor/http-parser/

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
* Tue May 17 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.4.0-1
- update to 0.4.0

* Wed Jul 7 2021 liuliang <liuliang1@kylinos.cn> - 0.1.2-1
- Package init
