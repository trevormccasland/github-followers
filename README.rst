================
github-followers
================
webclient for retrieving github followers.

Usage - Development
===================

API
---
To run the REST API for development you can install the github_followers python
package in development mode and start the API service with::

    $ python setup.py develop
    $ github-followers-api <config_file>

A sample of ``<config_file>`` can be found in
``etc/github-followers-api.conf``. This will start up a local webserver
listening on localhost. You can then send requests to the specified port on
stdout to see the response.

followers
^^^^^^^^^
To use the followers API you can send requests to the configured URL with the
username for the github login like so::

    GET /followers/:username
