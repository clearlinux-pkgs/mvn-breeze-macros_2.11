#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-breeze-macros_2.11
Version  : 0.13.2
Release  : 2
URL      : https://repo1.maven.org/maven2/org/scalanlp/breeze-macros_2.11/0.13.2/breeze-macros_2.11-0.13.2.jar
Source0  : https://repo1.maven.org/maven2/org/scalanlp/breeze-macros_2.11/0.13.2/breeze-macros_2.11-0.13.2.jar
Source1  : https://repo1.maven.org/maven2/org/scalanlp/breeze-macros_2.11/0.13.2/breeze-macros_2.11-0.13.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-breeze-macros_2.11-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-breeze-macros_2.11 package.
Group: Data

%description data
data components for the mvn-breeze-macros_2.11 package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scalanlp/breeze-macros_2.11/0.13.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/scalanlp/breeze-macros_2.11/0.13.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/scalanlp/breeze-macros_2.11/0.13.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/scalanlp/breeze-macros_2.11/0.13.2


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/scalanlp/breeze-macros_2.11/0.13.2/breeze-macros_2.11-0.13.2.jar
/usr/share/java/.m2/repository/org/scalanlp/breeze-macros_2.11/0.13.2/breeze-macros_2.11-0.13.2.pom
