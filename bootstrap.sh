#!/usr/bin/env bash

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
  SCRIPTPATH=/vagrant
fi

# Install Dependencies
wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
sudo rpm -ivh epel-release-6-8.noarch.rpm
sudo yum -y install libxml2-devel gdal-devel proj-devel json-c-devel geos-devel libxslt-devel docbook-style-xsl
sudo yum -y groupinstall "Development Tools"

# Configure directory layout
mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros

# Download source code
cd $HOME/rpmbuild/SOURCES
wget --quiet http://download.osgeo.org/postgis/source/postgis-2.2.1.tar.gz
