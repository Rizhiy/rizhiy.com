# rizhiy.com

Personal website

## Dev

Install dependencies:

```
pip install -e ".[dev]"
```

Run locally with:

```bash
flask --app rizhiy_com run --debug --cert=adhoc
```

## Prod

See scripts on how to install and run it.

To see logs when running the service use: `journalctl -u waitress.service -f`.
