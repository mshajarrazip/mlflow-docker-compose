# MLFlow Deployment with Docker Compose

## [Scenario 3: MLFlow on localhost with Tracking Server](https://www.mlflow.org/docs/latest/tracking.html#scenario-3-mlflow-on-localhost-with-tracking-server)

Simple mlflow deployment with docker-compose, backend store and artifact store on local storage.

Simply do:

```
git checkout basic-scenario3
docker-compose up -d --build
```

By default, the directory `${HOME}/mnt/mlruns` will be created (this will be the default store directory),
and mounted at the same path in the container*. The client will handle the store persistence directly, so we
need to appropriately set the permissions.

> When we send the REST API requests to log MLFlow entities to the tracking server,
> the server will respond with the store locations based on what's set in the container. If the values
> are different, then the client will end up assuming that the container-relative paths are available
> on the host, which will cause permission errors.

## References

1. [sachua/mlflow-docker-compose](https://github.com/sachua/mlflow-docker-compose)
2. [mlflow/mlfow/issues#989](https://github.com/mlflow/mlflow/issues/989#issuecomment-473491268)
3. [MLFLow Tracking Guide](https://www.mlflow.org/docs/latest/tracking.html#storage)
