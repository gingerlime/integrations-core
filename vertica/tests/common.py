# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.dev import get_docker_hostname, get_here

HERE = get_here()
COMPOSE_FILE = os.path.join(HERE, 'docker', 'docker-compose.yaml')

HOST = get_docker_hostname()
PORT = 5433
ID = 'datadog'

CONFIG = {
    'db': ID,
    'server': HOST,
    'port': PORT,
    'username': 'dbadmin',
    'password': 'monitor',
    'timeout': 10,
    'tags': ['foo:bar'],
    'tls_verify': False,
}

# TLS certs
CERTIFICATE_DIR = os.path.join(os.path.dirname(__file__), 'certificate')
cert = os.path.join(CERTIFICATE_DIR, 'cert.cert')
private_key = os.path.join(CERTIFICATE_DIR, 'server.pem')

TLS_CONFIG = {
    'db': 'abc',
    'server': 'localhost',
    'port': '999',
    'username': 'dbadmin',
    'password': 'monitor',
    'timeout': 10,
    'tags': ['foo:bar'],
    'tls_verify': True,
    'validate_hostname': True,
    'tls_cert': cert,
    'tls_private_key': private_key,
    'tls_ca_cert': CERTIFICATE_DIR,
}
