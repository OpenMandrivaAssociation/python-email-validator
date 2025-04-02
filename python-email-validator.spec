%define module email-validator
%define uname email_validator

Name:		python-email-validator
Version:	2.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/e/%{uname}/%{uname}-%{version}.tar.gz
Summary:	A robust email address syntax and deliverability validation library
URL:		https://pypi.org/project/email-validator/
License:	Unlicense
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(idna)
BuildRequires:	python%{pyver}dist(dnspython)
BuildRequires:	python%{pyver}dist(pytest)
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
A robust email address syntax and deliverability validation library for
Python 3.8+ by Joshua Tauberer.

This library validates that a string is of the form name@example.com and
optionally checks that the domain name is set up to receive email.

This is the sort of validation you would want when you are identifying users
by their email address like on a registration form.

Key features:

  Checks that an email address has the correct syntax --- great for email-based
  registration/login forms or validating data.

  Gives friendly English error messages when validation fails that you can
  display to end-users.

  Checks deliverability (optional): Does the domain name resolve?
  (You can override the default DNS resolver to add query caching.)

  Supports internationalized domain names (like @ツ.life), internationalized
  local parts (like ツ@example.com), and optionally parses display names
  (e.g. "My Name" <me@example.com>).

  Rejects addresses with invalid or unsafe Unicode characters, obsolete email
  address syntax that you'd find unexpected, special use domain names like
  @localhost, and domains without a dot by default.

  Normalizes email addresses (important for internationalized and quoted-string
  addresses!).

  Python type annotations are used.


%prep
%autosetup -n %{uname}-%{version} -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/%{uname}
%{python3_sitelib}/%{uname}
%{python3_sitelib}/%{uname}-%{version}.dist-info
%license LICENSE
