import os

kms_key_arn = "arn:aws:kms:sa-east-1:222222222222:key/exemplo"
print("[deploy] Data Lake: exemplo de deploy executado com sucesso")
print(f"[deploy] Data Lake: kms_key_arn={kms_key_arn}")

# Publica o output para o job seguinte (só existe dentro do GitHub Actions)
output_file = os.environ.get("GITHUB_OUTPUT")
if output_file:
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"kms_key_arn={kms_key_arn}\n")
