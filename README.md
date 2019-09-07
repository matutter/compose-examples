# Docker Compose Example

An example project using docker-compose to build images and
run containers.

## Building images

```bash
docker-compose build
```

## Running instance

Python uses buffered io, so the `PYTHONUNBUFFERED=1` environment variable may
be used to enable it for displaying application output for debugging. We'll set
that in the _compose file_ so our actual images do not have that hard-coded
environment variable.

```bash
docker-compose up
```

## References

- [aiohttp server docs](https://docs.aiohttp.org/en/stable/web.html)
- [aiohttp client docs](https://docs.aiohttp.org/en/stable/client.html)
- [docker-compose Overview](https://docs.docker.com/compose/)
- [docker-compose Networking](https://runnable.com/docker/docker-compose-networking)
