import os

print("[deploy] Produtor: exemplo de deploy executado com sucesso")
print(f"[deploy] Produtor: recebeu kms_key_arn={os.environ.get('KMS_KEY_ARN', '(nao informado)')}")
