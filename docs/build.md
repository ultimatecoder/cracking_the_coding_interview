# Build

## Developer

Make sure required [dependencies](dependencies.md) are installed. You are only
required to perform this steps if your intention is to make the developer build
of this project. If your intention is to try these solutions, then you are not
required to perform these developer build steps.

```
pipenv shell
```

This command will create a virtual environment wrapper if it is not already
created. If it is already created, then this command will activate it.

```
pipenv install --dev
```

Above command will install all the required python developer level dependencies.
