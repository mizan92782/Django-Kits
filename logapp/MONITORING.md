# Django Monitoring - Prometheus & Grafana (বাংলা গাইড)

---

## Prometheus কী?

Prometheus হলো একটি **monitoring tool** যেটা তোমার অ্যাপ থেকে ডেটা সংগ্রহ করে।

যেমন:
- কতটা request আসছে
- কোন request এ কত সময় লাগছে
- কতটা error হচ্ছে
- Database query কত হচ্ছে

Prometheus নির্দিষ্ট সময় পর পর (যেমন প্রতি ১৫ সেকেন্ডে) তোমার অ্যাপের `/metrics/` endpoint থেকে ডেটা নিয়ে নিজের কাছে জমা রাখে।

---

## Grafana কী?

Grafana হলো একটি **visualization tool** যেটা Prometheus এর জমানো ডেটাকে সুন্দর **গ্রাফ ও চার্টে** দেখায়।

সহজ কথায়:
- **Prometheus** = ডেটা সংগ্রহ করে ও জমা রাখে
- **Grafana** = সেই ডেটা সুন্দরভাবে দেখায়

---

## এরা একসাথে কীভাবে কাজ করে?

```
Django App (/metrics/)  →  Prometheus (ডেটা সংগ্রহ)  →  Grafana (ডেটা দেখায়)
```

১. Django অ্যাপ `/metrics/` endpoint এ সব তথ্য রাখে
২. Prometheus প্রতি ১৫ সেকেন্ডে সেখান থেকে ডেটা নেয়
৩. Grafana Prometheus থেকে ডেটা নিয়ে dashboard এ দেখায়

---

## Django তে Setup করার ধাপ

### ধাপ ১: Package ইনস্টল করো

```bash
pip install django-prometheus
```

### ধাপ ২: settings.py তে যোগ করো

```python
INSTALLED_APPS = [
    ...
    'django_prometheus',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',  # সবার আগে
    ...
    'django_prometheus.middleware.PrometheusAfterMiddleware',   # সবার শেষে
]

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '172.24.0.1']
```

### ধাপ ৩: urls.py তে যোগ করো

```python
from django.urls import path, include
from django_prometheus import exports

urlpatterns = [
    ...
    path('metrics/', exports.ExportToDjangoView, name='prometheus-django-metrics'),
]
```

এখন `http://localhost:8000/metrics/` এ গেলে raw metrics ডেটা দেখা যাবে।

### ধাপ ৪: Prometheus config ফাইল বানাও

`monitoring/prometheus.yml` ফাইল:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'django'
    static_configs:
      - targets: ['172.24.0.1:8000']
    metrics_path: '/metrics/'
```

> **নোট:** `172.24.0.1` হলো Docker এর host gateway IP। তোমার মেশিনে আলাদা হতে পারে।

### ধাপ ৫: docker-compose.yml বানাও

```yaml
services:
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
    extra_hosts:
      - "host.docker.internal:host-gateway"

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - prometheus
```

### ধাপ ৬: Docker চালু করো

```bash
docker compose up -d
```

### ধাপ ৭: Django চালু করো

```bash
python manage.py runserver 0.0.0.0:8000
```

### ধাপ ৮: Firewall ঠিক করো (Linux এ একবার করতে হয়)

```bash
sudo iptables -I INPUT -i br+ -p tcp --dport 8000 -j ACCEPT
```

এটা না করলে Docker container থেকে host এর port 8000 এ পৌঁছানো যায় না।

---

## Grafana Setup করার ধাপ

### ধাপ ১: Grafana খোলো
Browser এ যাও: `http://localhost:3000`
- Username: `admin`
- Password: `admin`

### ধাপ ২: Prometheus Data Source যোগ করো
1. বাম পাশে **Connections** → **Data Sources**
2. **Add data source** ক্লিক করো
3. **Prometheus** সিলেক্ট করো
4. URL দাও: `http://prometheus:9090`
5. **Save & Test** ক্লিক করো → সবুজ দেখালে সফল

### ধাপ ৩: Dashboard Import করো
1. বাম পাশে **Dashboards** → **Import**
2. `https://grafana.com/grafana/dashboards/17658` থেকে JSON ডাউনলোড করো
3. **Upload dashboard JSON file** দিয়ে আপলোড করো
4. Prometheus data source সিলেক্ট করো
5. **Import** ক্লিক করো

---

## সব কিছু ঠিকঠাক কিনা যাচাই করো

| চেক করো | URL |
|----------|-----|
| Django metrics | `http://localhost:8000/metrics/` |
| Prometheus targets | `http://localhost:9090/targets` |
| Grafana dashboard | `http://localhost:3000` |

Prometheus targets এ django এর পাশে **UP** (সবুজ) দেখালে সব ঠিক আছে।

---

## সমস্যা হলে

**Prometheus target DOWN দেখাচ্ছে?**
```bash
# Docker container থেকে Django reach হচ্ছে কিনা দেখো
docker exec logapp-prometheus-1 wget -qO- http://172.24.0.1:8000/metrics/ | head -3

# না হলে firewall rule দাও
sudo iptables -I INPUT -i br+ -p tcp --dport 8000 -j ACCEPT
```

**Grafana তে data নেই?**
```bash
# কিছু request করো যাতে metrics তৈরি হয়
curl http://localhost:8000/api/
```
তারপর ৩০ সেকেন্ড অপেক্ষা করো এবং dashboard refresh করো।
