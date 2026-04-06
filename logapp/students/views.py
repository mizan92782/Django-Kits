from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
import logging

logger = logging.getLogger(__name__)


class TeacherViewSet(viewsets.ModelViewSet):
    """ViewSet for Teacher CRUD operations"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def list(self, request, *args, **kwargs):
        """GET - Retrieve all teachers"""
        logger.info("Fetching all teachers")
        response = super().list(request, *args, **kwargs)
        logger.info(f"Successfully fetched {len(response.data)} teachers")
        return response

    def retrieve(self, request, *args, **kwargs):
        """GET - Retrieve a specific teacher by ID"""
        teacher_id = kwargs.get('pk')
        ip_address = self.get_client_ip(request)
        logger.info(f"Fetching teacher with ID: {teacher_id} from IP: {ip_address}")
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """POST - Create a new teacher"""
        logger.info(f"Creating new teacher with data: {request.data}")
        try:
            experience_years = int(request.data.get('experience_years', 0))
            if experience_years < 5:
                logger.warning("Experience less than 5 years will not be accepted")
        except (ValueError, TypeError):
            logger.warning("Invalid experience_years value provided")

        response = super().create(request, *args, **kwargs)
        logger.info(f"Successfully created teacher with ID: {response.data.get('id')}")
        return response

    def update(self, request, *args, **kwargs):
        """PUT - Update a teacher"""
        teacher_id = kwargs.get('pk')
        logger.info(f"Updating teacher with ID: {teacher_id}, data: {request.data}")
        response = super().update(request, *args, **kwargs)
        logger.info(f"Successfully updated teacher with ID: {teacher_id}")
        return response

    def destroy(self, request, *args, **kwargs):
        """DELETE - Delete a teacher"""
        teacher_id = kwargs.get('pk')
        logger.warning(f"Deleting teacher with ID: {teacher_id}")
        return super().destroy(request, *args, **kwargs)

    def get_client_ip(self, request):
        """Get the client IP address from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Take the first IP if there are multiple
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for Student CRUD operations"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        """GET - Retrieve all students"""
        logger.info("Fetching all students")
        response = super().list(request, *args, **kwargs)
        logger.info(f"Successfully fetched {len(response.data)} students")
        return response

    def retrieve(self, request, *args, **kwargs):
        """GET - Retrieve a specific student by ID"""
        student_id = kwargs.get('pk')
        logger.info(f"Fetching student with ID: {student_id}")
        try:
            response = super().retrieve(request, *args, **kwargs)
            logger.info(f"Successfully retrieved student with ID: {student_id}")
            return response
        except Exception as e:
            logger.error(f"Error retrieving student with ID: {student_id}, error: {str(e)}")
            raise

    def create(self, request, *args, **kwargs):
        """POST - Create a new student"""
        logger.info(f"Creating new student with data: {request.data}")
        try:
            response = super().create(request, *args, **kwargs)
            logger.info(f"Successfully created student with ID: {response.data.get('id')}")
            return response
        except Exception as e:
            logger.error(f"Error creating student: {str(e)}")
            raise

    def update(self, request, *args, **kwargs):
        """PUT - Update a student"""
        student_id = kwargs.get('pk')
        logger.info(f"Updating student with ID: {student_id}, data: {request.data}")
        try:
            response = super().update(request, *args, **kwargs)
            logger.info(f"Successfully updated student with ID: {student_id}")
            return response
        except Exception as e:
            logger.error(f"Error updating student with ID: {student_id}: {str(e)}")
            raise

    @action(detail=False, methods=['get'])
    def by_teacher(self, request):
        """GET - Retrieve students filtered by teacher"""
        teacher_id = request.query_params.get('teacher_id')
        logger.info(f"Fetching students for teacher_id: {teacher_id}")

        if not teacher_id:
            logger.warning("teacher_id parameter is missing")
            return Response({'error': 'teacher_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        students = Student.objects.filter(teacher_id=teacher_id)
        serializer = self.get_serializer(students, many=True)
        logger.info(f"Found {students.count()} students for teacher_id: {teacher_id}")
        return Response(serializer.data)
