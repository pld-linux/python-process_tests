#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Tools for testing processes
Summary(pl.UTF-8):	Narzędzia do testowania procesów
Name:		python-process_tests
Version:	2.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/process-tests/
Source0:	https://files.pythonhosted.org/packages/source/p/process-tests/process-tests-%{version}.tar.gz
# Source0-md5:	785b73dda3c6260b2edb6479f33a878d
URL:		https://github.com/ionelmc/python-process-tests
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for testing processes.

%description -l pl.UTF-8
Narzędzia do testowania procesów.

%package -n python3-process_tests
Summary:	Tools for testing processes
Summary(pl.UTF-8):	Narzędzia do testowania procesów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-process_tests
Tools for testing processes.

%description -n python3-process_tests -l pl.UTF-8
Narzędzia do testowania procesów.

%prep
%setup -q -n process-tests-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/process_tests.py[co]
%{py_sitescriptdir}/process_tests-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-process_tests
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/process_tests.py
%{py3_sitescriptdir}/__pycache__/process_tests.cpython-*.py[co]
%{py3_sitescriptdir}/process_tests-%{version}-py*.egg-info
%endif
