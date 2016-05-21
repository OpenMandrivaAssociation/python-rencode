Name:           python-rencode
Version:        1.0.4
Release:        1
Summary:        Web safe object pickling/unpickling
License:        GPLv3+ and BSD
URL:            https://github.com/aresch/rencode
Source0:        https://github.com/aresch/rencode/archive/rencode-%{version}.tar.gz
BuildRequires:  python-devel

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.


%prep
%setup -n rencode-%{version}


%build
%__python setup.py build

%install
%__python setup.py install --skip-build --root %{buildroot}

%files
%{python_sitearch}/rencode
%{python_sitearch}/rencode*.egg-info
%doc COPYING README.md

