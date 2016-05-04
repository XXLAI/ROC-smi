%define name        rocm-smi
%define version     1.0
%define packageroot $RPM_BUILD_ROOT
%define smiroot     $SMI_ROOT

Name:       %{name}
Version:    %{version}
Release:    1
Summary:    System Management Interface for ROCm

Group:      Applications/System
License:    Advanced Micro Devices Inc.

%description
This package includes the System Management Interface for the ROC Platform

%prep
%setup -T -D -c -n %{name}

%install
mkdir -p %{packageroot}/opt/rocm/bin
cp -R %{smiroot}/rocm-smi %{packageroot}/opt/rocm/bin

%clean
rm -rf %{packageroot}

%files
/opt/rocm/bin/rocm-smi
%defattr(-,root,root,-)
