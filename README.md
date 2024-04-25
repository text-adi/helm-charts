[![Test Helm Chart](https://github.com/text-adi/helm-charts/actions/workflows/test.yaml/badge.svg)](https://github.com/text-adi/helm-charts/actions/workflows/test.yaml)
[![Deploy GitHub Pages](https://github.com/text-adi/helm-charts/actions/workflows/deploy-pages.yaml/badge.svg)](https://github.com/text-adi/helm-charts/actions/workflows/deploy-pages.yaml)

# The My Library for Kubernetes

## Add repository

```console
helm repo add textadi https://text-adi.github.io/helm-charts/
```

## Before you begin

### Install Helm

Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

To install Helm, refer to the Helm install guide and ensure that the helm binary is in the PATH of your shell.

### Using Helm

Once you have installed the Helm client, you can deploy a Bitnami Helm Chart into a Kubernetes cluster.

Please refer to the [Quick Start guide](https://helm.sh/docs/intro/quickstart/) if you wish to get running in just a few commands, otherwise, the [Using Helm Guide](https://helm.sh/docs/intro/using_helm/) provides detailed instructions on how to use the Helm client to manage packages on your Kubernetes cluster.