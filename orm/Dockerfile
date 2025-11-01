FROM python:3.12


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /Restaurant 



# Copy requirements file into container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . .


# Expose port (optional, default Django port)
EXPOSE 8000



# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]