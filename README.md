# PostGIS 2 RPM Spec
RPM for the PostGIS 2 Postgres Extension

**Description**:

PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.

```
SELECT superhero.name
FROM city, superhero
WHERE ST_Contains(city.geom, superhero.geom)
AND city.name = 'Gotham';
```

In addition to basic location awareness, PostGIS offers many features rarely found in other competing spatial databases such as Oracle Locator/Spatial and SQL Server. Refer to PostGIS Feature List for more details.

**Technology stack**:

When installed postgis2 will act as an extension for Postgresql.

**Functions**:

See the [PostGIS website](http://postgis.net/) for a full description of functionality.

=======

## Dependencies

The build process for the postgis2 rpm requires postgresql9.4-devel and postgresql9.4 (x86_64) packages, or equivalent.  the *pg_config* binary must be accessible from the PATH.

## Installation

Build RPM using Vagrant

    1. The repo is cloned into a local sandbox
    2. Run "vagrant up" to build the VM.
    3. Run "vagrant ssh" to connect to VM.
    4. Run rpmbuild -ba SPECS/postgis2.spec --define 'pg_dir /usr/pgsql-9.4'  to build the postgis2 rpm package.  Substitute your custom Postgres path as needed.

    Please note: "pg_config" must be available in your environment PATH

Build RPM on server

    1. Once repo is cloned, run "sh ./bootstrap.sh" (sudo privileges are required)
    2. cd to ~/rpmbuild
    3. Run the following command
      rpmbuild -ba /SPECS/postgis2.spec  --define 'pg_dir /usr/pgsql-9.4'  Substitute your custom Postgres path as needed.

    Please note that "pg_config" MUST be accessible in users PATH

## Installing the RPM

Install the built RPM by running "sudo yum install RPMS/x86_64/postgis2.el6.x86_64.rpm"


## Configuration

Edit the SPEC file (SPEC/postgis2.spec) to make necessary changes to the build configuration

=======

## Known issues

## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

For general instructions on _how_ to contribute, please refer to [CONTRIBUTING](CONTRIBUTING.md).

----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

----

## Credits and references

See below links

- http://postgis.net/
