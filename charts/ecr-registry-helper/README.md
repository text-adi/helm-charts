# Helm package for ECR Registry helper

## Installing the Chart

Add the repository to helm. How to do it is described in
detail [here](https://github.com/text-adi/helm-charts?tab=readme-ov-file#add-repository).

To install the chart:

Example:

```console
helm install ecr-registry-helper textadi/ecr-registry-helper
```

## Parameters

| Name                         | Description                                                                                                                                        | Value                         |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| `image.registry`             | Image registry                                                                                                                                     | `docker.io`                   |
| `image.repository`           | Image repository                                                                                                                                   | `textadi/ecr-registry-helper` |
| `image.tag`                  | Image tag                                                                                                                                          | `2.15.40-1.30.0`              |
| `aws.accessKeyID`            | AWS Access key ID                                                                                                                                  | ``                            |
| `aws.secretAccessKey`        | AWS Secret access key                                                                                                                              | ``                            |
| `aws.account`                | AWS account                                                                                                                                        | ``                            |
| `aws.region`                 | AWS region                                                                                                                                         | `eu-central-1`                |
| `secretName`                 | Secret name will created in k8s by job                                                                                                             | `regcred`                     |
| `cronJobSchedule`            | The frequency of running a job to update accesses                                                                                                  | `0 */1 * * *`                 |
| `successfulJobsHistoryLimit` | Number of copies of successful job execution.  [Details](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#jobs-history-limits) | `1`                           |
| `failedJobsHistoryLimit`     | Number of copies of unsuccessful job execution [Details](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#jobs-history-limits) | `1`                           |