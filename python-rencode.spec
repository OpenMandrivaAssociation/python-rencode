%define debug_package %{nil}

Name:           python-rencode
Version:        1.0.8
Release:        2
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            https://github.com/aresch/rencode
Source0:	https://github.com/aresch/rencode/archive/v%{version}/rencode-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:	python-cython
BuildRequires:  python-pip
BuildRequires:  python-wheel
BuildRequires:  python-poetry-core
BuildSystem:    python

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%prep -a
# Upstream force risky -march=native and other like msse2, not available for ARM.
sed -i 's/COMPILE_ARGS = \[.*\]/COMPILE_ARGS = ["-O3"]/' build.py


%files
%{python_sitearch}/rencode
%{python_sitearch}/rencode*.dist-info
%doc COPYING README.md

