# 0x0F. Load balancer

This project is about load balancer, web stack debugging

## Files

- [0-custom_http_response_header](./0-custom_http_response_header): Bash script that configures a server to return a custom HTTP response header `X-Served-By` with the value of the server's hostname.

- [1-install_load_balancer](./1-install_load_balancer): Bash script that installs and configures HAproxy on a server.

- [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp): Puppet manifest that configures a server to return a custom HTTP response header `X-Served-By` with the value of the server's hostname.