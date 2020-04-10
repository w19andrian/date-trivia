# Date Trivia

## Introduction
This is a simple service to display various trivia related to the current date. Pardon for the over-simplicity on the frontend, this project is for educational purpose.

## Prerequisites
- Docker
- Kubernetes 1.13+
- Helm 2.6.*
- Make
- [metrics-server](https://github.com/kubernetes-sigs/metrics-server) ( for `autoScale` feature )
- [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
  
## Quickstart
```sh
git clone https://github.com/w19andrian/date-trivia.git
cd date-trivia
make all
```
The above commands will clone the repository, build docker images, and then deploy the chart for both `development` and `production` environment. By default, the frontend services are exposed via `NodePort`

Key differences between `development` and `production` on default configuration: 

|            | Development         | Production     |
|:----------:|:-------------------:|:--------------:|
| namespace  | trivia-devel        | trivia         |
| autoscale  | disabled            | enabled        |


## Advanced


Below are the list of parameters you can run with `make`

| Parameter  | Description                                      |
| ---------- | -------------------------------------------------|
| `all`      | deploy `development` and `production` packages   |
| `devel`    | deploy `development` package                     |
| `prod`     | deploy `production` package                      |
| `clean`    | remove all built images and helm releases        |

`ingress` feature is disabled due to the variety of *ingress controller*  and by default, kubernetes doesn't have it's own *ingress controller* and needs to be installed separately. You can always enable the `ingress` feature by executing this command 
```sh
helm upgrade --set ingress.enabled=true --set ingress.hosts=your.ingress.host my-release path/to/chart
```