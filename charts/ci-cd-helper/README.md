# Helm package for CI/CD

## Installing the Chart

Add the repository to helm. How to do it is described in
detail [here](https://github.com/text-adi/helm-charts?tab=readme-ov-file#add-repository).

To install the chart:

Example:

```console
helm install ci-cd-helper textadi/ci-cd-helper
```

## Installing the Chart

To update the chart:

```console
helm upgrade ci-cd-helper textadi/ci-cd-helper
```

## Parameters

| Name               | Description                                                                                                                                                | Value                         |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| `image.registry`   | Image registry                                                                                                                                             | `docker.io`                   |
| `image.repository` | Image repository                                                                                                                                           | `textadi/ecr-registry-helper` |
| `image.tag`        | Image tag                                                                                                                                                  | `2.15.40-1.30.0`              |
| `apiServer`        | Link to server cluster API. To get the required value, run the command in the terminal `kubectl config view --minify --output jsonpath={..cluster.server}` | `https://localhost:6443`      |