terraform {
  required_version = ">= 1.6"
}

# Exemplo básico, sem provider nem credenciais: só valida que o Terraform está instalado e executa.
resource "terraform_data" "hello" {
  input = "terraform instalado e funcionando"
}

output "mensagem" {
  value = terraform_data.hello.input
}
