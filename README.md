# Chmura – laboratoria (UWB)

Marek Jancevic

- **Lab 2 – Jedna strona, dwa sposoby udostępnienia** (S3 Website + Lambda Function URL w LocalStack):
  raport [`dowody/02-s3-lambda.md`](dowody/02-s3-lambda.md), polecenia [`dowody/polecenia-lstk.txt`](dowody/polecenia-lstk.txt)

## Uruchomienie

```bash
cp .env.example .env        # wpisz LOCALSTACK_AUTH_TOKEN
docker compose up -d
lstk aws s3 ls
```
