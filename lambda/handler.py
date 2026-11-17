import html
import os

import boto3

BUCKET = os.environ.get("TEMPLATE_BUCKET", "raport-koszykow-szablony")
KEY = os.environ.get("TEMPLATE_KEY", "template.html")

# W LocalStack zmienna AWS_ENDPOINT_URL jest wstrzykiwana do środowiska funkcji,
# więc boto3 sam kieruje żądania do emulatora. Na prawdziwym AWS jej nie ma.
s3 = boto3.client("s3")


def _odpowiedz(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "text/html; charset=utf-8"},
        "body": body,
    }


def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    imie = (params.get("imie") or "").strip()

    if not imie:
        return _odpowiedz(
            400,
            "<!DOCTYPE html><html lang=\"pl\"><meta charset=\"utf-8\">"
            "<h1>400 – brak parametru</h1>"
            "<p>Podaj imię w adresie, np. <code>?imie=Ola</code></p></html>",
        )

    # szablon czytany przy każdym żądaniu, więc nowa wersja w S3 działa bez redeployu
    szablon = s3.get_object(Bucket=BUCKET, Key=KEY)["Body"].read().decode("utf-8")
    strona = szablon.replace("{{IMIE}}", html.escape(imie))
    return _odpowiedz(200, strona)
