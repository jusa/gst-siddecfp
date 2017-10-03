Name:       gst-siddecfp
Summary:    GStreamer SID playback element
Version:    0.1
Release:    1
Group:      System/Libraries
License:    LGPL 2.0
URL:        https://github.com/oniongarlic/gst-siddecfp
Source:     %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gstreamer-base-1.0) >= 1.2
BuildRequires: pkgconfig(gstreamer-controller-1.0) >= 1.2
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) >= 1.2
BuildRequires: pkgconfig(gstreamer-audio-1.0) >= 1.2
BuildRequires: pkgconfig(libsidplayfp) >= 1.7

%description
Gstreamer element for playback of SID files using the libsiddecfp engine.

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-1.0/libgstsidfp.so
