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
