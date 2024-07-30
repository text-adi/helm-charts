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

Once you have installed the Helm client, you can deploy a Helm Chart into a Kubernetes cluster.

Please refer to the [Quick Start guide](https://helm.sh/docs/intro/quickstart/) if you wish to get running in just a few
commands, otherwise, the [Using Helm Guide](https://helm.sh/docs/intro/using_helm/) provides detailed instructions on
how to use the Helm client to manage packages on your Kubernetes cluster.

---

## For Develop

### Raising the test k0s cluster

To test the helm chart during development, you can raise a local k0s cluster.
Create a virtual python environment and activate it:

```shell
python3 -m venv .venv && source .venv/bin/activate
```

Install python dependencies for the correct operation of the tool:

```shell
pip install -r requirements.txt
```

After setting up the environment, create a k0s cluster. To execute the command in the `scripts` directory:

```shell
python -m cli up-cluster --tag v1.30.2-k0s.0 --workers 2 --ready-wait --force > ../admin
```

Detailed information about the available parameters of the `up-cluster` command can be obtained using the command:

```shell
python -m cli up-cluster --help
```

From the received help, the following parameters are available:

| Parameters     | Value                                                                                                                                                                                           | Required |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `--tag`        | Tag k0s docker image. It is recommended to use `v1.30.2-k0s.0`                                                                                                                                  | Yes      |
| `--workers`    | The number of created workers. It is recommended to use within reasonable limits. For example, `2` is used                                                                                      | Yes      |
| `--ready-wait` | Should we expect the k0s cluster to be ready for work? It is recommended to pass this parameter to the command to be sure that the k0s cluster was created successfully                         | No       |
| `--force`      | Whether to force k0s cluster to be created. If the parameter is not passed, an error will occur when the cluster is created again. This flag avoids this problem and rebuilds docker containers | No       |

### Install helm chart

To install helm chart, run the following command:

```shell
helm install -g charts/ci-cd-helper -n helm-test --create-namespace -f charts/ci-cd-helper/values.yaml --debug
```
