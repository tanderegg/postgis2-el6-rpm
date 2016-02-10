###########################
# Set global SPEC variables
###########################
%global _version 2.2.1

###############
# Set metadata
###############

Name:    postgis2
Version: %{_version}
Release: 1%{?dist}
Summary: PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.

Group:   Applications/Databases
License: Apache License
URL:     http://postgis.net/
Source:  http://download.osgeo.org/postgis/source/postgis-2.2.1.tar.gz
Obsoletes: postgis2 <= 2.2.1
Provides: postgis2 = 2.2.1

%description
PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.

###################
# Build requirements
#####################
BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)

########################################################
# PREP and SETUP
# The prep directive removes existing build directory
# and extracts source code so we have a fresh code base
# -n defines the name of the directory
#######################################################

%prep
%setup -n postgis-2.2.1

###########################################################
# BUILD
# The build directive does initial prep for building,
# then runs the configure script and then make to compile.
# Compiled code is placed in %{buildroot}
###########################################################

%build
CFLAGS="-O3 -Wall -Wno-format-security"
LDFLAGS="-pthread"

./configure
make

###########################################################
# INSTALL
# This directive is where the code is actually installed
# in the %{buildroot} folder in preparation for packaging.

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%files
/usr/local/include/liblwgeom.h
/usr/local/include/liblwgeom_topo.h
/usr/local/lib/liblwgeom-2.2.so.5
/usr/local/lib/liblwgeom-2.2.so.5.0.0
/usr/local/lib/liblwgeom.a
/usr/local/lib/liblwgeom.la
/usr/local/lib/liblwgeom.so
%{pg_dir}/bin/pgsql2shp
%{pg_dir}/bin/raster2pgsql
%{pg_dir}/bin/shp2pgsql
%{pg_dir}/lib/postgis-2.2.so
%{pg_dir}/lib/postgis_topology-2.2.so
%{pg_dir}/lib/rtpostgis-2.2.so
%{pg_dir}/share/contrib/postgis-2.2/legacy.sql
%{pg_dir}/share/contrib/postgis-2.2/legacy_gist.sql
%{pg_dir}/share/contrib/postgis-2.2/legacy_minimal.sql
%{pg_dir}/share/contrib/postgis-2.2/postgis.sql
%{pg_dir}/share/contrib/postgis-2.2/postgis_comments.sql
%{pg_dir}/share/contrib/postgis-2.2/postgis_restore.pl
%{pg_dir}/share/contrib/postgis-2.2/postgis_upgrade.sql
%{pg_dir}/share/contrib/postgis-2.2/raster_comments.sql
%{pg_dir}/share/contrib/postgis-2.2/rtpostgis.sql
%{pg_dir}/share/contrib/postgis-2.2/rtpostgis_legacy.sql
%{pg_dir}/share/contrib/postgis-2.2/rtpostgis_upgrade.sql
%{pg_dir}/share/contrib/postgis-2.2/sfcgal_comments.sql
%{pg_dir}/share/contrib/postgis-2.2/spatial_ref_sys.sql
%{pg_dir}/share/contrib/postgis-2.2/topology.sql
%{pg_dir}/share/contrib/postgis-2.2/topology_comments.sql
%{pg_dir}/share/contrib/postgis-2.2/topology_upgrade.sql
%{pg_dir}/share/contrib/postgis-2.2/uninstall_legacy.sql
%{pg_dir}/share/contrib/postgis-2.2/uninstall_postgis.sql
%{pg_dir}/share/contrib/postgis-2.2/uninstall_rtpostgis.sql
%{pg_dir}/share/contrib/postgis-2.2/uninstall_topology.sql
%{pg_dir}/share/extension/postgis--2.0.0--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.0.1--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.0.2--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.0.3--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.0.4--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.0.5--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.0.6--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.0.7--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.0--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.1--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.2--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.3--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.4--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.5--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.6--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.7--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.8--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.1.9--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.2.0--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.2.1--2.2.1next.sql
%{pg_dir}/share/extension/postgis--2.2.1.sql
%{pg_dir}/share/extension/postgis--2.2.1next--2.2.1.sql
%{pg_dir}/share/extension/postgis--unpackaged--2.2.1.sql
%{pg_dir}/share/extension/postgis.control
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.0--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.1--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.2--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.3--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.4--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.5--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.6--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.0.7--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.0--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.1--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.2--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.3--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.4--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.5--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.6--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.7--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.8--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.1.9--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.2.0--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.2.1--2.2.1next.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--2.2.1next--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder--unpackaged--2.2.1.sql
%{pg_dir}/share/extension/postgis_tiger_geocoder.control
%{pg_dir}/share/extension/postgis_tiger_geocoder.sql
%{pg_dir}/share/extension/postgis_topology--2.0.0--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.0.1--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.0.2--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.0.3--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.0.4--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.0.5--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.0.6--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.0.7--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.0--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.1--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.2--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.3--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.4--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.5--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.6--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.7--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.8--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.1.9--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.2.0--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.2.1--2.2.1next.sql
%{pg_dir}/share/extension/postgis_topology--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--2.2.1next--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology--unpackaged--2.2.1.sql
%{pg_dir}/share/extension/postgis_topology.control

%doc

%changelog
