# ==============================
#  Base Image
# ==============================
FROM python:3.12.3





# ==============================
#  Environment Variables
# ==============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1




# ==============================
#  Working Directory
# ==============================
WORKDIR /dockerize





# ==============================
# 4 System Dependencies
# ==============================
RUN apt-get update



# ==============================
# Python Dependencies
# ==============================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt




# ==============================
# Project Copy
# ==============================
COPY . .



# ==============================
#  Port Expose
# ==============================
EXPOSE 8000



# ==============================
# 9️⃣ Start Command
# ==============================
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
