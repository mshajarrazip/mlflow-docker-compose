# MLFlow Deployment with Docker Compose

## [Scenario 3: MLFlow on localhost with Tracking Server](https://www.mlflow.org/docs/latest/tracking.html#scenario-3-mlflow-on-localhost-with-tracking-server)

### Simple mlflow deployment with docker-compose, backend store and artifact store on local storage.

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

### MSSQL Server as Backend URI

To spin up an mssql container and have the backend URI point to the `mlflow` database on this server do:

```
git checkout basic-scenario3+mssql
docker-compose up -d --build
```

To access the mssql server running inside the container, use an SQL client software like [DBeaver](https://dbeaver.io/)
or [ssms](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)
with the following configurations:

|||
|-|-|
|Host|`localhost`|
|Port|`1433`|
|Authentication|`SQL Server Authentication`|
|Username|`sa`|
|Password|`Password123`|

If you don't want to spin up the mssql container and want a customized backend URI, set the variable `MLFLOW_BACKEND_URI`, then:

```
docker-compose -f docker-compose.yml up -d --build 
```

#### Tip: Set MLFLOW_ARTIFACTS_URI to a Sambashare folder

> See [this](https://ubuntu.com/tutorials/install-and-configure-samba#1-overview)
> on how to set up a sambashare server

1. Assume that there is a sambashare folder `/src/samba/share` accessible as follows:
    ```
    smb://172.16.200.100/sambashare
    ```
    with the following permissions:
    ```
    $ ls -l /srv
    drwxr-xr-x 3 samba samba 4096 Ogos  2 15:14 samba  
    ```
2. Say we are running the MLFlow tracking server at `172.16.200.100`, or we are accessing
   tracking server from anywhere else, then we need the same folder to exist everywhere,
   mounted to the same sambashare. See how to do this [here](https://chrisrmiller.com/mount-samba-share-in-ubuntu/).

3. Then we can set `MLFLOW_ARTIFACTS_URI=/src/samba/share`, and `docker-compose up` as usual.

## Additional Notes

1. After setting up the server, feel free to test it by using the [MLProject sample](mlproject-sample). If you are using
a database-backed backend, you may also try the model registry.
2. Managing permissions for the artifact location:
    ```
    sudo chmod -R ugo=rwx ~/mnt/mlruns
    ```

## References

1. [sachua/mlflow-docker-compose](https://github.com/sachua/mlflow-docker-compose)
2. [mlflow/mlfow/issues#989](https://github.com/mlflow/mlflow/issues/989#issuecomment-473491268)
3. [MLFLow Tracking Guide](https://www.mlflow.org/docs/latest/tracking.html#storage)
4. [install-and-configure-samba](https://ubuntu.com/tutorials/install-and-configure-samba#1-overview)
5. [Mount Samba Share in Linux](https://chrisrmiller.com/mount-samba-share-in-ubuntu/)
