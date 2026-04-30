# A Reproducible Experimental Study of Clustering
## Hotel Booking Demand — Course Release v1

Este repositório contém o ambiente experimental e os artefactos necessários para o estudo de clustering baseado no dataset **Hotel Booking Demand (Course Release v1)**. O foco deste projeto é a reprodutibilidade rigorosa, integridade dos dados e governação metodológica.

---

## Conteúdo do Arquivo

O pacote de dados "Course Release v1" inclui os seguintes componentes críticos para a proveniência dos dados:

1.  **`hotel_bookings_course_release_v1.csv`**: O snapshot autoritário do dataset para todas as experiências.
2.  **`SHA256SUMS.txt`**: Verificação criptográfica (SHA-256) para garantir a integridade e rastreabilidade dos dados.
3.  **`DATASET_MANIFEST.yml`**: Metadados estruturados (*Data Card*) especificando versão, unidade de análise, fonte, licença e dimensões.
4.  **`column_roles.csv`**: Especificação técnica das variáveis para suporte ao controlo de *leakage* e inclusão responsável de variáveis.
5.  **`subsample_indices_v1_n30000_seed12345.txt`**: Índices de linha (0-based) para amostragem reprodutível em métodos computacionalmente exigentes.

---

## Instruções de Reprodução

### 1. Verificação de Integridade
Antes de iniciar qualquer análise, deves verificar se a tua cópia local do dataset corresponde exatamente à "course release v1":
```bash
sha256sum -c SHA256SUMS.txt
```

# How to use
- conda env create -f environment.yml
- conda activate hotel-clustering
- python run_pipeline.py