# 0x09. Web infrastructure design

This project is about web infrastructure design and the different components that need to be considered when designing a web infrastructure.

## Files

### [0-simple_web_stack](./0-simple_web_stack)

A [link](https://github.com/4MR4N11/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/images/0-simple_web_stack.png) to a diagram of a simple web stack that includes:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

### [1-distributed_web_infrastructure](./1-distributed_web_infrastructure)

A [link](https://github.com/4MR4N11/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/images/1-distributed_web_infrastructure.png) to a diagram of a distributed web infrastructure that adds the following to the simple web stack:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)
