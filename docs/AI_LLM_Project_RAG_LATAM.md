# 🤖 Plantilla Oficial de Documentación — Proyecto Final AI/LLM

**Programa:** AI-LLM Solution Architect  
**Curso:** 5 — Proyecto Final de Arquitectura e Integración AI/LLM  
**Documento:** Plantilla Oficial de Documentación del Proyecto

---

## 📋 Información General del Proyecto

| Campo | Valor |
|-------|-------|
| **Nombre del Proyecto** | RAG Para Análisis Político de la Actualidad en Latinoamérica |
| **Participante(s)** | Raymundo Rivera Hernández |
| **Instructor** | *Nombre del instructor del curso* |
| **Cohorte / Edición** | Programa Certified AI-LLM Solution Architect — BSG Institute |
| **Fecha de Inicio** | 20/03/2026 |
| **Fecha de Entrega Final** | 23/03/2026 |
| **Versión del Documento** | v1.0 |
| **Estado del Proyecto** | Borrador |
| **Repositorio GitHub/GitLab** | github.com/sunrise-org/rag-latam (monorepo) |
| **Entorno Cloud** | AWS (sa-east-1) |
| **Stack Tecnológico Principal** | Python 3.11, FastAPI, LangChain LCEL, GPT-4o, text-embedding-3-small, Pinecone, Docker, Kubernetes (EKS), Terraform, Langfuse |

---

> ⚠️ **Instrucciones Generales**
>
> 1. Complete **TODOS** los campos marcados. El texto en *cursiva* son instrucciones — reemplácelas con su contenido real.
> 2. Mantenga consistencia en nomenclatura, versiones y referencias cruzadas entre secciones.
> 3. Los diagramas deben insertarse como imágenes de alta resolución (mínimo 150 dpi).
> 4. Cite todas las fuentes técnicas en formato **IEEE** o **APA**.
> 5. La documentación debe reflejar el estado **REAL** del proyecto, no el ideal. Sea preciso y honesto.
> 6. Entregue este archivo `.md` en el repositorio Git del proyecto, junto con el PDF generado.

---

## Tabla de Contenidos

- [1. Resumen Ejecutivo](#1-resumen-ejecutivo)
- [2. Análisis y Especificación de Requerimientos](#2-análisis-y-especificación-de-requerimientos)
- [3. Diseño de Arquitectura AI/LLM](#3-diseño-de-arquitectura-aillm)
- [4. Diseño de APIs y Conectores](#4-diseño-de-apis-y-conectores)
- [5. Seguridad, Cumplimiento y Ética](#5-seguridad-cumplimiento-y-ética)
- [6. Implementación y Configuración de Infraestructura](#6-implementación-y-configuración-de-infraestructura)
- [7. Estrategia de Pruebas y Resultados](#7-estrategia-de-pruebas-y-resultados)
- [8. Despliegue, Escalabilidad y Costos](#8-despliegue-escalabilidad-y-costos)
- [9. Observabilidad y Monitoreo](#9-observabilidad-y-monitoreo)
- [10. Resultados, Conclusiones y Trabajo Futuro](#10-resultados-conclusiones-y-trabajo-futuro)
- [11. Rúbrica de Evaluación](#11-rúbrica-de-evaluación)
- [12. Referencias y Bibliografía](#12-referencias-y-bibliografía)
- [Anexos](#anexos)

---

## 1. Resumen Ejecutivo

El proyecto "RAG Para Análisis Político de la Actualidad en Latinoamérica" desarrolla una solución AI/LLM basada en Retrieval-Augmented Generation (RAG) que permite a periodistas, analistas políticos y portales de noticias especializados en Latinoamérica realizar consultas en lenguaje natural sobre la actualidad geopolítica de la región. El sistema recupera información de múltiples fuentes documentales (PDF, Word, bases de datos) y APIs de noticias, generando resúmenes fundamentados con citas de las fuentes originales y considerando los sesgos que estas puedan tener. La arquitectura se basa en Python 3.11 con FastAPI, LangChain LCEL para orquestación, GPT-4o como modelo de inferencia, Pinecone como vector store, y despliegue en AWS (EKS). El MVP apunta a una latencia p95 < 3s, fidelidad ≥ 0.85 (RAGAS), y soporte bilingüe español/inglés, con un costo operacional estimado entre USD $420 y $1,100/mes.

### 1.1 Propuesta de Valor y Problema que Resuelve

Actualmente, el proceso de análisis político en Latinoamérica es predominantemente manual: un moderador busca en más de 20 fuentes diferentes y elabora un documento con las notas más relevantes, incluyendo ligas a las fuentes originales y una columna pronóstica. Este proceso toma de 3 a 4 horas diarias y se envía cada día a las 6 am. El 65% de las consultas de los usuarios son repetitivas pero requieren contexto especializado que un buscador keyword tradicional no resuelve. El costo actual en suscripciones mensuales a fuentes es de aproximadamente $5,000 MXN, y la escalabilidad está limitada al número de personas que se agreguen al equipo. Una solución AI/LLM con RAG es la estrategia óptima porque permite automatizar la recuperación y síntesis de información geopolítica de múltiples fuentes, reduciendo el tiempo de generación de reportes de 3-4 horas a menos de 30 segundos, escalando sin límite de consultas concurrentes, y ofreciendo disponibilidad 24/7 frente al horario laboral actual limitado.

### 1.2 Alcance y Delimitación

| ✅ INCLUIDO EN EL ALCANCE | ❌ EXCLUIDO DEL ALCANCE |
|------------|----------------|
| Interfaz de consulta vía API REST para usuarios internos | Fine-tuning o entrenamiento de modelos desde cero |
| Pipeline RAG sobre documentos de noticias y geopolítica (PDF, Word, DB), posteriormente incluir agentes seleccionados | Interfaz de usuario frontend (solo API en esta fase) |
| Despliegue en entorno cloud AWS y local (on-premise) | Soporte multimodal (imágenes, audio, video) |
| Autenticación con proveedores de identidad (Google, Facebook) vía AWS Cognito | Integración con sistemas externos de terceros |
| Dashboard de monitoreo de calidad y costo LLM | SLA enterprise (> 99.9%) — MVP con 99.5% |
| Soporte bilingüe (español e inglés) | Idiomas distintos al español e inglés |
| Columna política mostrando los eventos más relevantes a nivel Latinoamérica de acuerdo a las tendencias de mayor relevancia | No se dará un sesgo específico para cada cliente; se tratará de dar información neutral |

### 1.3 Indicadores Clave de Éxito (KPIs del Proyecto)

| KPI / Métrica | Línea Base | Meta Objetivo | Resultado Obtenido |
|---------------|-----------|---------------|-------------------|
| Latencia promedio (p95) | N/A | < 3 segundos | *[Completar al final]* |
| Fidelidad (Faithfulness RAGAS) | N/A | ≥ 0.85 | *[Completar al final]* |
| Tasa de contacto/relevancia | N/A | > 70% | *[Completar al final]* |
| Costo operacional mensual (USD) | $5,000 MXN (suscripciones) | $420–$1,100 USD/mes | *[Completar al final]* |
| Cobertura de pruebas (%) | 0% | > 80% | *[Completar al final]* |
| Detección out-of-scope | N/A | ≥ 95% | *[Completar al final]* |

---

## 2. Análisis y Especificación de Requerimientos

### 2.1 Contexto del Caso de Uso Empresarial

**Industria/Sector:** Medios de comunicación, análisis geopolítico y periodismo especializado en Latinoamérica.

**Actores involucrados:** Periodistas y autores especializados en Latinoamérica (actor primario), Agentes y Analistas políticos (actor secundario), Portales de noticias que consumen la información.

**Aplicando el framework 5W+H:**

| Dimensión | Pregunta Clave | Respuesta del Proyecto |
|-----------|---------------|----------------------|
| **WHO** | ¿Quién lo usará? Actor primario, secundario, sistemas integrados | Periodistas y autores especializados en Latinoamérica, Agentes y Analistas, Portales de noticias |
| **WHAT** | ¿Qué debe hacer el sistema? Capacidad central y outputs esperados | Recibir consultas en lenguaje natural, recuperar información de documentos ingresados por el modelo y de varias APIs dedicadas a noticias y geopolítica vía RAG, y retornar resúmenes con citas de las fuentes tomando en cuenta los sesgos que estas puedan tener |
| **WHY** | ¿Por qué AI/LLM y no una solución tradicional? Justificación vs. alternativas | El 65% de las consultas son repetitivas pero requieren contexto especializado que un buscador keyword no resuelve. RAG aplica capacidad de comprensión y síntesis que herramientas tradicionales no ofrecen |
| **WHERE** | ¿Dónde se desplegará? Geografía, infraestructura y análisis | API REST interna, cloud AWS accesible desde LATAM, habla hispana e inglesa |
| **WHEN** | ¿Cuándo se usará? Frecuencia y volumen | 1,000 consultas/día pico 9am-11pm, 100 usuarios concurrentes máximo, disponibilidad L-D 8am a 12pm y 24/7 con asistencia AI |
| **HOW** | ¿Cómo se mide el éxito? KPIs cuantitativos | Tasa de contacto > 70%, latencia p95 < 3s, fidelidad = 0.85 (RAGAS), tiempo de inclusión y satisfacción |

**Flujo AS-IS vs TO-BE:**

| Criterio | SITUACIÓN ACTUAL (AS-IS) | CON AI/LLM (TO-BE) |
|----------|-------------------------|---------------------|
| Proceso | Manual: moderador busca en 20+ fuentes diferentes y elabora un documento con las notas más relevantes, incluyendo ligas a las fuentes y una columna pronóstica. Se envía cada día a las 6 am | Automatizado, respuesta sugerida en < 3 segundos |
| Tiempo de respuesta | De 3 a 4 horas para generar el documento de noticias | < 30 segundos con asistencia AI |
| Escalabilidad | Limitado al número de personas que se agreguen al equipo | Escalable, sin límite de consultas concurrentes |
| Costo por consulta | $5,000 MXN en suscripciones mensuales | Variable, dependiendo del agente o auto-scaling ~$1.5 USD |
| Disponibilidad | Solo horario laboral, previa solicitud | 24/7 |

### 2.2 Requerimientos Funcionales

| ID | Descripción del Requerimiento | Prioridad | Criterio de Aceptación |
|----|-------------------------------|-----------|------------------------|
| RF-001 | **Inferencia:** El sistema DEBE recibir una consulta en lenguaje natural (≤ 2,048 tokens) y retornar una respuesta fundamentada en texto recuperado. | Alta | Latencia < 3 segundos (p95). Tasa de fidelidad ≥ 0.85 medida por RAGAS |
| RF-002 | **Pipeline RAG:** El sistema DEBE recuperar los 5 fragmentos más relevantes del vector store mediante búsqueda semántica. | Alta | Recall@5 ≥ 0.85 en dataset de evaluación. Latencia retrieval < 500ms |
| RF-003 | **Formato Output:** Las respuestas DEBEN incluir citations (fuente, página, párrafo) verificables. | Alta | 100% de respuestas con al menos 1 fuente verificable. Citation accuracy ≥ 95% |
| RF-004 | **Casos Límite:** El sistema DEBE detectar consultas fuera de dominio y responder con mensaje predefinido en lugar de alucinar. | Alta | Detección out-of-scope ≥ 95%. Zero alucinaciones en consultas fuera de dominio |
| RF-005 | **Memoria Conversacional:** Soporte multi-turno con humanos en español e inglés con detección de idioma automática. | Media | Detección de idioma ≥ 98%. Calidad equivalente en ambos idiomas |
| RF-006 | **Indexación:** Indexar documentos corporativos en formatos PDF, Word y bases estructuradas. | Alta | Procesamiento exitoso. Tiempo de indexación < 60 segundos por documento |
| RF-007 | **Escalamiento Humano:** El sistema PUEDE escalar consultas complejas a un agente humano. | Baja | Transferencia completa con historial de conversación |
| RF-008 | **Transformación de Output:** Retornar respuesta en formato JSON cuando se solicite vía parámetro API. | Media | Respuestas válidas en JSON cuando el parámetro se active |
| RF-009 | **Seguridad de Prompts:** Bloquear ataques de prompt injection conocidos. | Alta | Bloqueo ≥ 99% de ataques en benchmark OWASP LLM Top 10 |

### 2.3 Requerimientos No Funcionales

| ID | Categoría | Descripción | Métrica / Umbral |
|----|-----------|-------------|-----------------|
| RNF-001 | Rendimiento | Latencia end-to-end de consultas | p50 < 1.5s, p95 < 3s, p99 < 5s — Medido con k6 / Locust load test |
| RNF-002 | Rendimiento | Time to First Token (TTFT) | < 800ms (p95) — Monitoreo en runtime con OpenTelemetry |
| RNF-003 | Rendimiento | Throughput del sistema | 50 RPS sostenidos con ramp-up progresivo |
| RNF-004 | Escalabilidad | Usuarios concurrentes máximo | 50 usuarios simultáneos sin degradación. Estrategia de auto-scaling < 60s |
| RNF-005 | Seguridad | Autenticación / Autorización | OAuth 2.0 / OIDC con JWT vía AWS Cognito + revisión de configuración |
| RNF-006 | Seguridad | Clasificación de datos | PII encriptado at-rest (AES-256) y in-transit (TLS 1.3). Auditoría trimestral |
| RNF-007 | Seguridad | Defensa contra Prompt Injection | Bloqueo ≥ 99% ataques conocidos — Examen + benchmark OWASP LLM Top 10 |
| RNF-008 | Disponibilidad | SLA objetivo | 99.5% uptime (MVP), RTO < 30min, RPO mínimo. Alertas 24/7 |
| RNF-009 | Observabilidad | Logging y trazabilidad | 100% requests con trace ID, logs estructurados + Langfuse |
| RNF-010 | Observabilidad | Dashboard de monitoreo | RAGAS score, latencia, costo por consulta en tiempo real |
| RNF-011 | Cumplimiento | Data residency y regulación | Región LATAM, cumplimiento con lineamientos GDPR aplicables |

### 2.4 Restricciones y Supuestos

| Restricciones | Supuestos |
|--------------|-----------|
| Costo operacional mensual MVP: USD $420–$1,100/mes | Los usuarios finales tienen acceso estable a Internet desde LATAM |
| No se permite almacenamiento de PII en logs | El modelo GPT-4o está disponible vía API de OpenAI |
| Esfuerzo total: 170–260 horas | Los proveedores de identidad (Google, Facebook) están disponibles para autenticación |
| Duración recomendada: 6–10 semanas (20 días de ejecución) | Pinecone como vector store mantiene disponibilidad y latencia adecuada |
| Si el costo supera $200 USD/mes, activar caching y/o fallback a GPT-4o mini | Las fuentes de noticias y APIs geopolíticas están accesibles para indexación |
| Rate limit: 60 req/min por usuario | Alerta: Si el costo supera $200 USD, activar caching por GPT-4o mini |

---

## 3. Diseño de Arquitectura AI/LLM

### 3.1 Diagrama de Arquitectura General (Nivel C4 — Contexto y Contenedor)

> 📌 **Instrucción:** Inserte aquí el diagrama de arquitectura de alto nivel. Herramientas recomendadas: Lucidchart, Draw.io, Miro, o AWS Architecture Diagram.
>
> El diagrama **DEBE** incluir: (1) Usuarios/Actores externos, (2) Capa de presentación/API, (3) Servicios de orquestación LLM, (4) Fuentes de datos y vector stores, (5) Servicios cloud, (6) Componentes de seguridad e identidad.
>
> Resolución mínima: 150 dpi. Formato: PNG o SVG.

```
[ INSERTE DIAGRAMA DE ARQUITECTURA GENERAL AQUÍ ]
```

*Figura 1. Diagrama de Arquitectura General — RAG Para Análisis Político LATAM v1.0*

### 3.2 Descripción de Componentes Arquitectónicos

| Componente | Tecnología / Servicio | Responsabilidad Principal | Justificación de Selección |
|------------|----------------------|--------------------------|---------------------------|
| API Gateway | FastAPI (Python 3.11) + AWS API Gateway | Enrutamiento, autenticación JWT vía Cognito, rate limiting (60 req/min) + Guardrails AI | Alto rendimiento asíncrono, integración nativa con ecosistema Python y AWS |
| Orquestador LLM | LangChain LCEL | Gestión de prompts, cadenas [RETRIEVAL] + [GENERATION], orquestación RAG | Ecosistema maduro, soporte RAG nativo, composabilidad con LCEL |
| Modelo LLM Base | GPT-4o (128K contexto) con fallback a GPT-4o mini | Generación de texto e inferencia | Contexto amplio (128K), mejor relación calidad/precio, function calling avanzado. GPT-4o mini como fallback para optimización de costos |
| Vector Store | Pinecone | Almacenamiento y búsqueda semántica (RAG). Top-K=5 chunks + Metadata filter | Búsqueda semántica de baja latencia, escalabilidad serverless, filtrado por metadatos |
| Modelo de Embeddings | text-embedding-3-small (1536 dimensiones) | Generación de vectores para indexación y búsqueda | Balance entre rendimiento semántico y costo, 1536 dimensiones |
| Capa de Datos | AWS S3 | Almacenamiento de documentos fuente, audit logs, persistencia de datos | Costo bajo, durabilidad 99.999999999%, integración nativa con EKS |
| Observabilidad | Langfuse + Dashboard | Monitoreo de RAGAS score, latencia, costo por consulta, trazas de prompts | Monitoreo diario con dashboard especializado para LLM. Trazabilidad completa |
| Seguridad / IAM | AWS Cognito (JWT) + Guardrails AI | Autenticación OAuth 2.0/OIDC, rate limiting, defensa prompt injection, PII masking | Integración nativa AWS, soporte para proveedores externos (Google, Facebook) |

### 3.3 Diagrama de Flujo de Datos e Integración

*Inserte diagrama de secuencia o flujo de datos que muestre el ciclo completo de una solicitud: desde el input del usuario hasta la respuesta final, incluyendo pasos de RAG, validación, logging y respuesta.*

```
[ INSERTE DIAGRAMA DE FLUJO DE DATOS / SECUENCIA AQUÍ ]
```

*Figura 2. Flujo de Datos — Ciclo de Request/Response en RAG Análisis Político LATAM*

**Flujo del sistema:**
1. Usuario (vía app Sunrise) envía consulta en español/inglés
2. API REST (FastAPI) → API Gateway con JWT Cognito + Rate Limit (60 req/min) + Guardrails AI
3. Orquestador LangChain LCEL:
   - [RETRIEVAL]: text-embedding-3-small genera embedding → Pinecone búsqueda semántica → Top-K=5 chunks + Metadata filter + latencia monitorizada
   - [GENERATION]: GPT-4o (128K) genera respuesta con contexto recuperado + prompt personalizado
4. Respuesta con citations → S3 audit log
5. Monitoreo: Langfuse dashboard (RAGAS score, latencia, costo)

### 3.4 Estrategia de Diseño de Prompts y RAG

**System Prompt Base:**

*Documente el system prompt que guía el comportamiento del modelo. Incluya: rol, restricciones, formato de respuesta esperado, y manejo de casos fuera de alcance.*

```
Eres un asistente experto en análisis político y geopolítica de Latinoamérica para Sunrise.
Tu función es analizar noticias, tendencias políticas y eventos geopolíticos de la región LATAM,
proporcionando resúmenes fundamentados con citas de las fuentes originales.

RESTRICCIONES:
  - Solo responde en base al contexto proporcionado por el pipeline RAG. Si no tienes
    información suficiente, indica "No tengo información sobre eso en mis fuentes actuales."
  - No generes contenido con sesgo político específico; mantén neutralidad informativa.
  - Responde en el idioma detectado del usuario (español o inglés) con un tono formal/periodístico.
  - Siempre incluye citations verificables (fuente, página, párrafo) en tus respuestas.
  - Identifica y señala posibles sesgos de las fuentes consultadas.

FORMATO DE RESPUESTA: Texto estructurado con citations inline. JSON cuando se solicite vía parámetro API.
```

### 3.4 Arquitectura física (equivalencias por nube)

| Capa | AWS | GCP | Azure |
|---|---|---|---|
| Ingesta | Lambda / ECS | Cloud Run / Functions | Azure Functions |
| Raw (Bronze) | S3 | GCS | ADLS Gen2 |
| Transform | Glue / EMR | Dataflow / Dataproc | Synapse / Databricks |
| Curated (Silver) | S3 Parquet | GCS Parquet | ADLS Parquet |
| Serving (Gold) | Athena / Redshift | BigQuery | Synapse SQL |
| Orquestación | Step Functions / MWAA | Composer / Workflows | ADF |
| Observabilidad | CloudWatch | Cloud Monitoring | Azure Monitor |

---

**Estrategia de Recuperación (RAG):**

| Parámetro | Valor |
|-----------|-------|
| **Modelo de Embeddings** | text-embedding-3-small (OpenAI) |
| **Dimensionalidad** | 1,536 dimensiones |
| **Vector Store** | Pinecone (búsqueda semántica) |
| **Top-K** | 5 chunks recuperados por consulta |
| **Filtrado** | Metadata filter (fuente, fecha, región, idioma) |
| **Función de Similitud** | Cosine similarity |
| **Documentos soportados** | PDF, Word, bases de datos estructuradas (noticias LATAM) |
| **Monitoreo de latencia** | Latencia de retrieval monitorizada, objetivo < 500ms |

---

## 4. Diseño de APIs y Conectores

### 4.1 Especificación de Endpoints (API REST / GraphQL)

*Para cada endpoint principal, complete la siguiente tabla. En un proyecto maduro se adjunta el archivo OpenAPI/Swagger como anexo.*

| Endpoint | Método | Descripción | Request Body / Params | Response Schema |
|----------|--------|-------------|----------------------|-----------------|
| `/api/v1/query` | `POST` | Envía una consulta al LLM con contexto RAG | `{"query": string, "session_id": string, "context_filter": object}` | `{"response": string, "sources": array, "tokens_used": int, "latency_ms": float}` |
| `/api/v1/ingest` | `POST` | Carga documentos al vector store | `{"documents": array, "metadata": object}` | `{"status": string, "indexed_docs": int, "errors": array}` |
| `/api/v1/health` | `GET` | Health check del sistema | N/A | `{"status": "healthy\|degraded", "components": object}` |
| *[Endpoint]* | | | | |

### 4.2 Autenticación y Autorización

| Campo | Descripción |
|-------|-------------|
| **Mecanismo Auth** | JWT Bearer Token con OAuth 2.0 / OIDC vía AWS Cognito |
| **Proveedor de Identidad** | AWS Cognito con proveedores federados (Google, Facebook) |
| **Gestión de Secrets** | Variables de entorno gestionadas vía .env (pydantic settings) — secretos en AWS |
| **Rate Limiting** | 60 req/min por usuario + Guardrails AI para validación |
| **Roles definidos** | Definidos en Cognito User Pool con Client ID dedicado |

### 4.3 Conectores de Fuentes de Datos

| Fuente de Datos | Tipo | Conector/SDK | Frecuencia de Sync | Manejo de Errores |
|----------------|------|-------------|-------------------|------------------|
| APIs de noticias geopolíticas LATAM | APIs REST externas | Loaders personalizados (LangChain) | Batch + tiempo real | Retry con backoff, logging en S3 |
| Documentos PDF/Word | Documentos no-estructurados | LangChain Document Loaders | Indexación bajo demanda | Validación de formato, alertas de error |
| Bases de datos estructuradas | SQL / NoSQL | Conectores nativos | Sync programado | Retry x3, audit log en S3 |

---

## 5. Seguridad, Cumplimiento y Ética

### 5.1 Modelo de Amenazas y Controles de Seguridad

| Amenaza / Riesgo | Vector de Ataque | Nivel | Control Implementado | Justificación Técnica |
|-----------------|-----------------|-------|---------------------|----------------------|
| Prompt Injection | Input malicioso del usuario | **ALTO** | Input sanitization + guardrails LLM | Validación de input, detección de patrones de inyección con regex + LLM classifier |
| Data Leakage | Respuestas con PII no autorizado | **ALTO** | Output filtering + PII redaction | Integración con AWS Comprehend PII detection o equivalente |
| API Key Exposure | Repositorio público / logs | **CRÍTICO** | Secrets Manager + SAST CI/CD | Pre-commit hooks, rotación automática de keys |
| DoS / Abuso de API | Volumen excesivo de requests | **MEDIO** | Rate limiting + WAF | API Gateway throttling + AWS WAF / CloudFlare |
| *[Amenaza]* | | | | |

### 5.2 Cumplimiento Regulatorio

| Regulación | Requerimiento Aplicable | Control Implementado | Evidencia |
|-----------|------------------------|---------------------|-----------|
| GDPR (si aplica) | Derecho al olvido, consentimiento explícito, notificación de breaches | *[Medidas implementadas]* | *[Link a política / log]* |
| ISO 27001 / SOC 2 | Gestión de accesos, auditoría, continuidad del negocio | *[Controles]* | *[Evidencia]* |
| Política Interna de IA | Uso responsable de IA, revisión humana de decisiones críticas | *[Definir]* | *[Evidencia]* |
| *[Otra regulación]* | | | |

### 5.3 Marco Ético de la Solución AI

| Dimensión Ética | Riesgo Identificado | Mecanismo de Mitigación |
|----------------|--------------------|-----------------------|
| Sesgos algorítmicos | El modelo puede perpetuar sesgos del corpus de entrenamiento | Evaluación periódica de outputs + dataset de benchmarking de equidad |
| Transparencia | Los usuarios pueden no saber que interactúan con IA | Disclosure explícito en interfaz + mecanismo de escalamiento a humano |
| Alucinaciones | El modelo puede generar información falsa con confianza alta | RAG + citación de fuentes + umbral de confianza mínimo configurable |
| Privacidad de datos | Inputs del usuario podrían usarse para reentrenamiento | Opt-out explícito, cero retention policy en APIs de terceros |
| *[Dimensión adicional]* | | |

---

## 6. Implementación y Configuración de Infraestructura

### 6.1 Stack Tecnológico y Justificación

| Capa | Tecnología Seleccionada | Alternativas Evaluadas | Razón de Selección |
|------|------------------------|----------------------|-------------------|
| LLM Provider | OpenAI GPT-4o (128K) + GPT-4o mini (fallback) | Anthropic Claude 3, Gemini 1.5 Pro | Contexto amplio 128K, madurez del ecosistema, velocidad de setup, function calling avanzado. GPT-4o mini para optimización de costos vía caching |
| Orquestación | LangChain LCEL | LlamaIndex, Semantic Kernel | Composabilidad con LCEL, ecosistema maduro, soporte RAG nativo, amplia comunidad |
| Backend API | FastAPI + Python 3.11 | Flask, Django, Node.js | Alto rendimiento asíncrono, tipado nativo, documentación automática OpenAPI |
| Embeddings | text-embedding-3-small (1536 dim) | all-MiniLM-L6-v2, Cohere Embed | Balance entre dimensionalidad (1536), performance semántica y costo |
| Vector DB | Pinecone | Weaviate, ChromaDB, pgvector | Búsqueda semántica serverless, baja latencia, filtrado por metadatos, escalabilidad |
| Cloud Provider | AWS (sa-east-1) | Azure, GCP | Región LATAM disponible (sa-east-1), ecosistema completo (EKS, S3, Cognito), costos competitivos |
| Containerización | Docker + Kubernetes (EKS) | ECS, Cloud Run | Orquestación robusta, auto-scaling granular, portabilidad. Imagen base python-slim |
| CI/CD | GitHub Actions (ci.yml) | GitLab CI, CircleCI | Integración nativa con GitHub repo, pipelines: pytest + build + push ECR + deploy EKS |
| Observabilidad | Langfuse + Dashboard personalizado | CloudWatch, Grafana, LangSmith | Especializado en trazas LLM, monitoreo de RAGAS scores, costo por consulta, latencia |

### 6.2 Estructura del Repositorio

```
github.com/sunrise-org/rag-latam/          # Monorepo — creado en Sprint 1, 5 juntos CI/CD
├── README.md                               # NUNCA commitear secrets reales
├── PULL_REQUEST_TEMPLATE.md
├── .github/workflows/
│   └── ci.yml                              # pytest + build + push ECR + deploy EKS
├── api/                                    # Código fuente API
│   ├── app/                                # main.py, routes/, middleware
│   └── ...
├── rag/                                    # Pipeline RAG
│   ├── loaders/                            # Document Loaders + indexación
│   ├── retrieval/                          # Retrieval + búsqueda semántica
│   └── ...
├── security/                               # Guardrails
│   ├── defense/                            # Prompt injection defense + PII masking
│   └── ...
├── config/                                 # Settings desde .env (pydantic)
├── infra/                                  # Terraform
│   ├── terraform/                          # EKS, S3, Cognito, Pinecone
│   └── helm/                               # K8s manifests (ingress, service, hpa)
├── tests/
│   ├── dataset/                            # Dataset LATAM (JSONL): preguntas + ground truth
│   ├── e2e/                                # Tests end-to-end
│   ├── load/                               # k6 scripts: 50 RPS, ramp-up 5 min
│   └── ragas_eval/                         # Evaluación: Faithfulness ≥ 0.85, Relevancy
├── docs/
│   ├── diagrams/                           # Diagramas C4 + ADR-001 a ADR-003
│   └── ...
├── notebooks/                              # Prototipo rápido (S1-S2), index, evaluate
├── .pre-commit-config.yaml                 # pre-commit hooks + flake8 + detect-secrets
├── pyproject.toml                          # poetry
├── Dockerfile                              # Image python-slim
├── .env.example                            # Variables de entorno (NUNCA commitear .env)
└── .gitignore                              # .local, __pycache__/, .venv, *.egg-info, etc.
```

**Estrategia de branching:** `main` (protegido) + `feature/SPRINT-XXX`

### 6.3 Variables de Entorno y Configuración

| Variable de Entorno | Descripción | Gestión / Almacenamiento |
|--------------------|-------------|------------------------|
| `OPENAI_API_KEY` | Clave de autenticación con la API de OpenAI | Secrets — `sk-your-openai-api-key-here` |
| `MODEL` | Modelo LLM principal | Variable de entorno — `gpt-4o` |
| `EMBEDDING_MODEL` | Modelo de embeddings | Variable de entorno — `text-embedding-3-small` |
| `MAX_TOKENS` | Máximo de tokens por respuesta | Variable de entorno — `2048` |
| `TEMPERATURE` | Temperatura del modelo | Variable de entorno — `0.1` |
| `PINECONE_API_KEY` | Clave API de Pinecone | Secrets |
| `PINECONE_INDEX_NAME` | Nombre del índice vectorial | Variable de entorno — `rag-latam` |
| `PINECONE_DIMENSION` | Dimensionalidad de embeddings | Variable de entorno — `1536` |
| `PINECONE_TOP_K` | Número de chunks a recuperar | Variable de entorno — `5` |
| `AWS_ACCESS_KEY_ID` | ID de acceso AWS | Secrets |
| `AWS_SECRET_ACCESS_KEY` | Clave secreta AWS | Secrets |
| `AWS_DEFAULT_REGION` | Región AWS | Variable de entorno — `sa-east-1` |
| `S3_BUCKET_DOCS` | Bucket S3 para documentos y logs | Variable de entorno |
| `LANGFUSE_PUBLIC_KEY` | Clave pública de Langfuse | Variable de entorno — `pk-lf-public` |
| `LANGFUSE_HOST` | Host de Langfuse | Variable de entorno — `https://cloud.langfuse.com` |
| `COGNITO_USER_POOL_ID` | ID del User Pool de Cognito | Variable de entorno |
| `COGNITO_CLIENT_ID` | ID del cliente Cognito | Variable de entorno |
| `APP_ENV` | Entorno de ejecución | Variable de entorno — `production` |
| `LOG_LEVEL` | Nivel de logging | Variable de entorno — `INFO` |
| `PORT` | Puerto del servicio | Variable de entorno — `8000` |
| `RATE_LIMIT_REQUESTS_PER_MINUTE` | Límite de peticiones por minuto | Variable de entorno — `60` |
| `CONCURRENT_REQUESTS` | Límite de peticiones concurrentes | Variable de entorno |
| `COST_ALERT_THRESHOLD_USD` | Umbral de alerta de costos | Variable de entorno — `20` |
| `GUARDRAILS_ENABLED` | Habilitar guardrails de seguridad | Variable de entorno — `true` |
| `PII_MASK_ENABLED` | Habilitar enmascaramiento de PII | Variable de entorno — `true` |
| `PROMPT_INJECTION_DETECTION` | Habilitar detección de prompt injection | Variable de entorno — `true` |

---

## 7. Estrategia de Pruebas y Resultados

### 7.1 Plan de Pruebas

| Tipo de Prueba | Alcance | Herramienta | Criterio de Aceptación | Estado |
|---------------|---------|-------------|----------------------|--------|
| Unitarias | Funciones de chunking, embeddings, retrievers, loaders | pytest (integrado en ci.yml) | Cobertura > 80% | ⬜ Pendiente |
| Integración | Pipeline RAG end-to-end, APIs internas | pytest + Docker Compose | Todos los flujos críticos validados | ⬜ Pendiente |
| Rendimiento / Carga | Endpoint `/api/v1/query` bajo carga concurrente | k6 scripts: 50 RPS, ramp-up 5 min | p95 < 3s con 50 usuarios concurrentes | ⬜ Pendiente |
| Seguridad | OWASP LLM Top 10, prompt injection benchmark | OWASP ZAP + benchmark personalizado | Bloqueo ≥ 99% ataques, 0 vulnerabilidades críticas | ⬜ Pendiente |
| LLM Evaluation (RAGAS) | Calidad de respuestas: fidelidad, relevancia, factualidad | RAGAS (ragas_eval/) + dataset LATAM (JSONL) | Faithfulness ≥ 0.85, Relevancy ≥ 0.80 | ⬜ Pendiente |
| E2E / Aceptación | Flujos completos desde API hasta respuesta con ground truth | Tests end-to-end con dataset de preguntas + ground truth | 100% de casos de uso críticos pasan | ⬜ Pendiente |

### 7.2 Resultados de Pruebas de Rendimiento

*Incluya gráficas y tablas de resultados. Las capturas de pantalla de dashboards (k6, Locust, CloudWatch) deben insertarse como figuras.*

| Métrica | 10 Usuarios Concurrentes | 50 Usuarios | 100 Usuarios | Meta Objetivo |
|---------|------------------------|------------|-------------|--------------|
| Latencia p50 (ms) | *[XXX]* | *[XXX]* | *[XXX]* | < 1,000 ms |
| Latencia p95 (ms) | *[XXX]* | *[XXX]* | *[XXX]* | < 2,000 ms |
| Latencia p99 (ms) | *[XXX]* | *[XXX]* | *[XXX]* | < 4,000 ms |
| Tasa de error (%) | *[XXX]* | *[XXX]* | *[XXX]* | < 1% |
| Throughput (RPS) | *[XXX]* | *[XXX]* | *[XXX]* | *[Definir]* |
| Tokens promedio/req | *[XXX]* | *[XXX]* | *[XXX]* | *[Definir]* |

### 7.3 Evaluación de Calidad LLM (LLM-as-Judge)

*Documente los resultados de evaluación con RAGAS, LangSmith, o evaluación manual estructurada.*

| Métrica RAGAS / Custom | Score Obtenido | Score Mínimo Aceptable | ¿Cumple? | Observaciones |
|----------------------|---------------|----------------------|---------|---------------|
| Faithfulness (fidelidad al contexto) | *[0.XX]* | 0.85 | ✅ / ❌ | |
| Answer Relevancy | *[0.XX]* | 0.80 | ✅ / ❌ | |
| Context Precision | *[0.XX]* | 0.75 | ✅ / ❌ | |
| Context Recall | *[0.XX]* | 0.75 | ✅ / ❌ | |
| Hallucination Rate | *[X%]* | < 5% | ✅ / ❌ | |
| *[Métrica personalizada]* | | | | |

---

## 8. Despliegue, Escalabilidad y Costos

### 8.1 Estrategia de Despliegue

| Campo | Descripción |
|-------|-------------|
| **Estrategia de Despliegue** | Despliegue containerizado en AWS EKS con Helm charts |
| **Herramienta CI/CD** | GitHub Actions (ci.yml): pytest → build → push ECR → deploy EKS |
| **Infrastructure as Code** | Terraform — módulos para EKS, S3, Cognito, Pinecone en `/infra/terraform/` |
| **Entornos** | Development → Staging → Production |
| **Rollback Strategy** | Automático vía health check failure en K8s + RTO < 30min |
| **Container Registry** | Amazon ECR |
| **Versioning** | Semantic Versioning + Git tags. Branch: `main` (protegido) + `feature/SPRINT-XXX` |
| **Metodología** | Híbrida Agile-Waterfall. Sprint reviews + milestones. IEEE 29148:2018. Gestión vía GitHub Projects |
| **Duración del Proyecto** | 20 días de ejecución (6–10 semanas). Inicio: 20/03/2026 — Cierre: 23/03/2026 |

### 8.2 Configuración de Escalabilidad

| Componente | Mínimo de Instancias | Máximo de Instancias | Trigger de Auto-Scaling |
|------------|---------------------|---------------------|------------------------|
| API Service (K8s Deployment) | 2 pods | 20 pods | CPU > 70% durante 2 min \| RPS > 100 |
| Worker / Background Jobs | 1 pod | 10 pods | Queue length > 100 mensajes |
| *[Otro componente]* | | | |

### 8.3 Análisis y Optimización de Costos

| Servicio / Componente | Costo Estimado/mes | Costo Real/mes | Unidad de Medida | Optimización Aplicada |
|----------------------|------------------|---------------|-----------------|----------------------|
| OpenAI API (GPT-4o + embeddings) | USD $*[Estimar]* | USD $*[Real]* | Por 1M tokens | Prompt caching + fallback a GPT-4o mini si costo > $200/mes |
| Pinecone (Vector DB) | USD $*[Estimar]* | USD $*[Real]* | Por unidades/mes | Serverless, escalado automático |
| AWS EKS (Compute) | USD $*[Estimar]* | USD $*[Real]* | Por hora | Spot instances, right-sizing, auto-scaling |
| AWS S3 (Almacenamiento) | USD $*[Estimar]* | USD $*[Real]* | Por GB/mes | Lifecycle policies |
| AWS Cognito (Auth) | USD $*[Estimar]* | USD $*[Real]* | Por MAU | Primeros 50K MAU gratis |
| Langfuse (Observabilidad) | USD $*[Estimar]* | USD $*[Real]* | Por mes | Cloud hosted |
| **TOTAL ESTIMADO** | **USD $420–$1,100/mes** | **USD $*[Real]*** | | Esfuerzo total: 170–260 horas. Duración: 6–10 semanas |

**Equipo Humano Estimado:**

| Rol / Servicio | Nivel / Tier | Estimación (horas) | Observaciones |
|---------------|-------------|-------------------|---------------|
| Arquitecto AI/LLM | Senior | 40–60h | Diseño, revisión técnica |
| ML Engineer | Mid | 80–120h | Pipeline RAG, evaluación |
| DevOps/SRE | Mid | 30–50h | IaC, CI/CD, monitoreo |
| Analista de Negocios | Mid | 20–30h | Reqs, validación, UAT |
| QA / Tester | Mid | *[Estimar]* | Tests funcionales, d-team |

---

## 9. Observabilidad y Monitoreo

### 9.1 Stack de Observabilidad

| Categoría | Solución Implementada |
|----------|-----------------------|
| **Logging** | Logs estructurados con trace ID — 100% de requests trazables. Python structured logging |
| **Métricas** | OpenTelemetry — métricas custom de LLM (token count, latencia, TTFT, error rate, costo por consulta) |
| **Trazabilidad (Tracing)** | OpenTelemetry + Langfuse para trazas completas de prompts/respuestas y pipeline RAG |
| **Alertas** | Alertas automáticas — costo > $20 USD umbral, latencia degradada, errores sostenidos |
| **Dashboard LLM** | Langfuse — monitoreo diario de RAGAS score, latencia, costo por consulta, calidad de respuestas |
| **SLO/SLA Monitoring** | SLA 99.5% uptime (MVP), latencia p95 < 3s, RTO < 30min — alertas 24/7 |

### 9.2 Métricas Clave Monitoreadas

| Métrica | Tipo | Umbral de Alerta | Acción Automática / Escalamiento |
|---------|------|-----------------|--------------------------------|
| Latencia p95 de API | Rendimiento | > 2,500 ms | Auto-scaling trigger + notificación Slack |
| Tasa de error de API | Confiabilidad | > 2% | PagerDuty alert + rollback automático |
| Tokens consumidos/hora | Costo | > 80% del budget mensual | Email al equipo + throttling de requests |
| Hallucination Rate (LLM Eval) | Calidad | > 10% | Revisión manual + retraining pipeline |
| Vector Store Query Latency | Rendimiento | > 500 ms | Cache warming + índice rebuild |
| *[Métrica custom]* | | | |

---

## 10. Resultados, Conclusiones y Trabajo Futuro

### 10.1 Resultados Obtenidos vs. Objetivos

| Objetivo | Meta Planificada | Resultado Real | Estado |
|----------|-----------------|---------------|--------|
| Latencia de respuesta | p95 < 2 segundos | *[X.XX] segundos* | ✅ Logrado / ⚠️ Parcial / ❌ No logrado |
| Calidad de respuestas | Faithfulness > 0.85 | *[0.XX]* | |
| Cobertura de pruebas | > 80% | *[XX]%* | |
| Costo operacional | < USD $*[X]*/mes | USD $*[Y]*/mes | |
| *[Objetivo adicional]* | | | |

### 10.2 Conclusiones Técnicas

*Mínimo 300 palabras. Responda: ¿Qué funcionó bien y por qué? ¿Qué no funcionó y cuáles fueron los obstáculos? ¿Qué decisiones arquitectónicas resultaron acertadas? ¿Cuáles cambiaría? ¿Qué aprendizajes aplica a proyectos futuros?*

### 10.3 Lecciones Aprendidas

| Categoría | Lección Aprendida | Aplicación Futura |
|-----------|------------------|------------------|
| Diseño de Prompts | *[Descripción de lección]* | *[Cómo aplicaría esto en el siguiente proyecto]* |
| Arquitectura de Datos | *[Descripción]* | *[Aplicación]* |
| Gestión del Proyecto | *[Descripción]* | *[Aplicación]* |
| Seguridad / Cumplimiento | *[Descripción]* | *[Aplicación]* |
| *[Categoría]* | | |

### 10.4 Hoja de Ruta — Trabajo Futuro

| Horizonte | Mejora / Feature Planeada | Justificación | Complejidad Estimada |
|-----------|--------------------------|---------------|---------------------|
| Corto Plazo (1–3 meses) | *[Ej. Fine-tuning del modelo con datos propios de la empresa]* | *[Mejora esperada en calidad]* | Alta / Media / Baja |
| Mediano Plazo (3–6 meses) | *[Ej. Multi-modal: soporte para imágenes y documentos escaneados vía OCR]* | *[Impacto]* | |
| Largo Plazo (6–12 meses) | *[Ej. Sistema de agentes autónomos multi-step para automatización de procesos]* | *[Impacto]* | |

---

## 11. Rúbrica de Evaluación

*La puntuación máxima es **4.0** por criterio. El promedio ponderado determina la nota final del módulo.*

| Criterio | Excepcional (4) | Competente (3) | En Desarrollo (2) | Insuficiente (1) |
|----------|----------------|---------------|------------------|-----------------|
| **Análisis de Requerimientos** (10%) | Requerimientos funcionales y no funcionales completamente especificados, priorizados con criterios de aceptación medibles, trazables a objetivos de negocio. | Requerimientos bien documentados con criterios de aceptación. Pequeños gaps en trazabilidad. | Requerimientos incompletos o sin criterios de aceptación claros. Falta de priorización. | Requerimientos ausentes, genéricos o sin relación con el caso de uso real. |
| **Diseño Arquitectónico** (25%) | Arquitectura técnicamente sólida, completamente justificada, con diagramas C4, decisiones de diseño documentadas (ADRs), y consideración de trade-offs. | Arquitectura correcta con diagramas claros. Justificaciones presentes pero con algunas decisiones sin fundamentar. | Arquitectura básica presente. Diagramas incompletos. Pocas o ninguna justificación de decisiones técnicas. | Sin diagrama de arquitectura coherente. Componentes mal definidos o sin integración aparente. |
| **Implementación Técnica** (25%) | Código funcional, modular, bien documentado, con manejo de errores robusto, pruebas con cobertura > 80%, y siguiendo principios SOLID / Clean Architecture. | Código funcional con estructura razonable. Pruebas básicas presentes (> 50% cobertura). Documentación parcial. | Código funcional pero monolítico, sin pruebas o con cobertura muy baja (< 30%). Errores sin manejo. | Código no funcional, sin estructura, sin pruebas, o no disponible en repositorio. |
| **Seguridad y Cumplimiento** (15%) | Modelo de amenazas completo, todos los controles implementados y validados, cumplimiento regulatorio documentado con evidencias, marco ético exhaustivo. | Principales controles de seguridad implementados. Cumplimiento parcialmente documentado. Análisis ético presente. | Consideraciones de seguridad básicas. Sin validación de cumplimiento. Análisis ético superficial. | Sin controles de seguridad. Sin consideraciones de cumplimiento ni ética. |
| **Pruebas y Validación** (15%) | Plan de pruebas completo ejecutado. Métricas de rendimiento y calidad LLM documentadas. Todos los KPIs medidos con evidencias. | Pruebas funcionales y de rendimiento ejecutadas. Métricas parcialmente reportadas. | Solo pruebas funcionales básicas. Sin pruebas de carga o evaluación LLM. Métricas escasas. | Sin evidencia de pruebas realizadas o resultados no disponibles. |
| **Documentación y Presentación** (10%) | Documento técnico completo, profesional y preciso. Presentación oral clara, con demo funcional, manejo experto de preguntas técnicas. | Documentación completa con pocos errores. Presentación clara con demo. Respuestas adecuadas. | Documentación incompleta o con inconsistencias. Presentación básica. Dificultades en preguntas técnicas. | Documentación ausente o irrelevante. Presentación confusa o sin demo funcional. |

### Escala de Calificación

| Rango | Equivalencia |
|-------|-------------|
| 3.6 – 4.0 — Excepcional | ✅ Aprobado con Distinción |
| 3.0 – 3.5 — Competente | ✅ Aprobado |
| 2.0 – 2.9 — En Desarrollo | ⚠️ Condicional — revisión requerida |
| < 2.0 — Insuficiente | ❌ Reprobado — nueva entrega requerida |

---

### 11.1 Criterios de evaluación  

***Evaluación técnica (70%)***
| Criterio                | Peso |
| ----------------------- | ---- |
| Diseño de arquitectura  | 20%  |
| Implementación          | 20%  |
| Almacenamiento en cloud | 15%  |
| Automatización          | 10%  |
| Calidad del código (validacion por 3 IAs)      | 5%   |

---
***Conceptual (30%).***  
| Criterio              | Peso |
| --------------------- | ---- |
| Justificación técnica | 15%  |
| Claridad documental   | 10%  |
| Defensa de decisiones | 5%   |


---

### 11.2 Entregables oficiales

- 👨‍💻Código funcional
- 🏛️Arquitectura documentada
- ☁️Datos en la nube
- 📃README técnico
- 🎥Video de no mas de 30 minutos donde se evidencie el funcionamiento del proyecto

---

## 12. Referencias y Bibliografía

*Liste todas las fuentes citadas en el documento en formato **IEEE** o **APA**. Mínimo **10 referencias** técnicas. Incluya: documentación oficial de APIs/SDKs, papers académicos, libros técnicos, y recursos del curso.*

1. M. Kleppmann, *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. Sebastopol, CA: O'Reilly Media, 2017.
2. B. Beyer, C. Jones, J. Petoff, and N. R. Murphy, *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol, CA: O'Reilly Media, 2016.
3. OpenAI, "GPT-4 Technical Report," arXiv preprint arXiv:2303.08774, 2023. [Online]. Available: https://arxiv.org/abs/2303.08774
4. P. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," in *Proc. NeurIPS 2020*, vol. 33, pp. 9459–9474.
5. L. Moroney, *AI and Machine Learning for Coders*. Sebastopol, CA: O'Reilly Media, 2020.
6. B. Wilder, *Cloud Architecture Patterns*. Sebastopol, CA: O'Reilly Media, 2012.
7. A. García Serrano, *Inteligencia Artificial: Fundamentos, Práctica y Aplicaciones*. Madrid: RC Libros, 2016.
8. LangChain, "LangChain Documentation v0.2," [Online]. Available: https://python.langchain.com/docs
9. *[Agregue referencia adicional — artículo, documentación oficial, paper]*
10. *[Agregue referencia adicional]*

---

## Anexos

### Anexo A — Architecture Decision Records (ADR)

Utilice una plantilla ADR para documentar cada decisión arquitectónica clave. Mínimo **3 ADRs** requeridos.

```markdown
# ADR-001: [Título descriptivo de la decisión]

**Fecha:** DD/MM/AAAA  
**Estado:** Propuesto / Aceptado / Rechazado / Deprecado  
**Autores:** [Nombre(s)]

## Contexto
[Describa la situación y el problema que motivó esta decisión arquitectónica.]

## Decisión
[Describa la decisión tomada y cómo resuelve el problema.]

## Consecuencias Positivas
- [Beneficio 1]
- [Beneficio 2]

## Consecuencias Negativas / Trade-offs
- [Desventaja o deuda técnica 1]

## Alternativas Consideradas
- **Opción A:** [Descripción] — Descartada porque [razón]
- **Opción B:** [Descripción] — Descartada porque [razón]
```

---

### Anexo B — Glosario de Términos Técnicos

| Término | Definición |
|---------|-----------|
| **RAG** (Retrieval-Augmented Generation) | Técnica que combina recuperación de información relevante de una base de conocimiento externa con la generación de texto de un LLM, reduciendo alucinaciones y mejorando la factualidad de las respuestas. |
| **LLM** (Large Language Model) | Modelo de lenguaje de gran escala entrenado con enormes corpus de texto usando arquitecturas Transformer, capaz de generar, resumir, traducir y razonar con lenguaje natural. |
| **Embeddings** | Representaciones vectoriales densas de texto que capturan relaciones semánticas, permitiendo búsqueda por similitud en espacios de alta dimensionalidad. |
| **Vector Store** | Base de datos especializada en almacenar y recuperar eficientemente vectores de alta dimensionalidad mediante algoritmos ANN (Approximate Nearest Neighbors) como HNSW o IVF. |
| **Prompt Engineering** | Disciplina de diseño y optimización de instrucciones para guiar el comportamiento de LLMs hacia resultados deseados de forma consistente y controlada. |
| **Guardrails** | Mecanismos de control que validan, filtran o restringen los inputs y outputs de un sistema LLM para garantizar seguridad, cumplimiento y adherencia a políticas. |
| **Hallucination** | Fenómeno en el que un LLM genera información factualmente incorrecta o inventada con aparente confianza, sin base en los datos de entrenamiento o el contexto provisto. |
| **Fine-tuning** | Proceso de ajuste de los pesos de un modelo pre-entrenado sobre un dataset específico del dominio para mejorar su rendimiento en tareas particulares. |
| **ADR** (Architecture Decision Record) | Documento que captura una decisión arquitectónica importante, incluyendo contexto, opciones evaluadas, decisión tomada y consecuencias. |
| **RAGAS** | Framework de evaluación automatizada de pipelines RAG que mide faithfulness, answer relevancy, context precision y context recall. |
| *[Término adicional]* | *[Definición]* |

---

### Anexo C — Checklist de Entrega Final

Marque cada ítem antes de hacer la entrega final:

- [ ] Documento Markdown completado en todas sus secciones
- [ ] Repositorio Git con código fuente, notebooks y configuración IaC
- [ ] `README.md` del repositorio con instrucciones de despliegue local
- [ ] Diagramas de arquitectura en alta resolución (PNG/SVG en `/docs/architecture/`)
- [ ] ADRs documentados para al menos 3 decisiones arquitectónicas clave (en `/docs/adr/`)
- [ ] Especificación OpenAPI/Swagger del API (YAML/JSON en `/docs/api/`)
- [ ] Reporte de pruebas de rendimiento (k6/Locust outputs)
- [ ] Reporte de evaluación LLM (RAGAS o equivalente)
- [ ] Análisis de costos completo con datos reales del entorno cloud
- [ ] Presentación de diapositivas para la defensa oral (15–20 slides)
- [ ] Video demo del sistema funcionando (máx. 5 minutos — link a YouTube/Drive)
- [ ] Evidencias de pruebas de seguridad (OWASP ZAP reporte o equivalente)

---

*— Fin del Documento —*  
*Programa AI-LLM Solution Architect | Curso 5: Proyecto Final*
