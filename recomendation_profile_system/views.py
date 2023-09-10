import json
import time

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from exam.models import Course, Result
from student.models import Student

from django.core import serializers


# Create your views here.
# 1 Normalizar las competencias a buscar
# 2 Obtener la matriz de competencias a buscar por perfiles
# 3 Obtener la Matriz resultante de multiplicar cada valor de la competencia normalizada por la fila o columna de la
# competencia correspondientte en la matriz de competencia por perfiles
# 4 Sumar los valores de las competencias por perfil
# 5 Selecionar el o los x mayores valores de la suma en el paso anterior.

class SearchRecommendationProfile(TemplateView):
    template_name = 'professional_profile_search.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['competencias'] = list(Course.objects.all().values('id', 'course_name'))
        context['competencias_count'] = Course.objects.all().count()
        return self.render_to_response(context)


@method_decorator(csrf_exempt)
def search_professional_profiles(request):
    if request.method == 'POST':
        competencias = json.loads(request.POST.get('competencias[]', None))
        # 1 Normalizar las competencias a buscar
        competencias_normalizadas = normalizar(competencias)

        # 2 Obtener la matriz de competencias a buscar por perfiles
        students_with_competences = get_competencias_by_profiles()
        matrix_de_competencias_por_perfiles = get_matrix(students_with_competences, competencias)

        # 3 Obtener la Matriz resultante de multiplicar cada valor de la competencia normalizada por la fila o columna
        # de la competencia correspondientte en la matriz de competencia por perfiles
        result_matrix = get_resultant_matrix(matrix_de_competencias_por_perfiles, competencias_normalizadas)

        # 4 Sumar los valores de las competencias por perfil
        profiles_to_recommendate = to_add(result_matrix)

        # 5 Ordena los perfiles en orden descendiente
        profiles_to_recommendate.sort(key=lambda x: x['sume'], reverse=True)
        # 6 Selecionar el o los x mayores valores de la suma en el paso anterior.
        profiles_to_return = get_profiles_to_return(profiles_to_recommendate)

        return JsonResponse(profiles_to_return, status=200, safe=False)
        # obtener los estudiantes.


def get_competencias_by_profiles():
    students = list(Student.objects.all().values())
    # Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
    for student in students:
        student['competences'] = get_student_competences(student['id'])
    return students


def get_student_competences(id):
    """
    Retorna una lista con el id de las competencias y su respectiva calificción
    """
    competencias = []
    for i in Result.objects.raw('select *, max(date) from exam_result where student_id = %s group by exam_id;', [id]):
        competencias.append({
            'exam_id': i.exam_id,
            'mark': i.marks,
        })
    return competencias


def normalizar(lista):
    competencias_normalizadas = []
    mayor = lista[0]['number']
    menor = lista[0]['number']
    list(lista)
    try:
        if len(lista) > 0:
            for competencia in lista:
                if competencia['number'] > mayor:
                    mayor = competencia['number']
                if competencia['number'] < menor:
                    menor = competencia['number']
            # calcular cada valor z = (valor_i- menor)/(maximo-menor)
            for competencia in lista:
                z = (int(competencia['number']) - int(menor)) / (int(mayor) - int(menor));
                competencias_normalizadas.append({'norm_number': z, 'competencia_id': competencia['competencia_id']})
    except Exception as e:
        e.__str__()
    return competencias_normalizadas


def get_matrix(students_with_competences, competencias_solicitadas):
    ids_competencias_solicitadas = []
    for c in competencias_solicitadas:
        ids_competencias_solicitadas.append(int(c['competencia_id']))
    matrix = []
    try:
        for swc in students_with_competences:
            comp = []
            ids_student_competences = []
            for competence in swc['competences']:
                ids_student_competences.append(int(competence['exam_id']))
            for id_competencia_solicitada in ids_competencias_solicitadas:
                if id_competencia_solicitada in ids_student_competences:
                    mark = 0
                    for c in swc['competences']:
                        if int(c['exam_id']) == id_competencia_solicitada:
                            mark = c['mark']
                            break
                    comp.append({
                        'exam_id': int(id_competencia_solicitada),
                        'mark': mark,
                    })
                else:
                    comp.append({
                        'exam_id': int(id_competencia_solicitada),
                        'mark': 0,
                    })
            matrix.append({
                'student_id': swc['id'],
                'competences': comp
            })
    except Exception as e:
        e.__str__()
    return matrix


def get_resultant_matrix(matrix_de_competencias_por_perfiles, competencias_normalizadas):
    result_marix = []
    for mcp in matrix_de_competencias_por_perfiles:
        comp = []
        for competence in mcp['competences']:
            for competencia_normalizada in competencias_normalizadas:
                if competence['exam_id'] == int(competencia_normalizada['competencia_id']):
                    mark = competence['mark'] * float(competencia_normalizada['norm_number'])
                    comp.append({
                        'exam_id': competence['exam_id'],
                        'mark': mark,
                    })
        result_marix.append({
            'student_id': mcp['student_id'],
            'competences': comp
        })
    return result_marix


def to_add(result_matrix):
    profiles = []
    for rm in result_matrix:
        sume = 0.0
        for competence in rm['competences']:
            sume += competence['mark']
        profiles.append({
            'student_id': rm['student_id'],
            'sume': sume
        })
    return profiles


def get_profiles_to_return(profiles_to_recommendate):
    time.sleep(3)
    ptr = []
    i = 0
    try:
        # Es hasta una variable que diga la cantidad de perfiles pero puse hasta 10
        while (i < 10 and i < len(profiles_to_recommendate)):
            student = serializers.serialize('json',
                                            Student.objects.filter(id=profiles_to_recommendate[i]['student_id']))
            id = list(Student.objects.filter(id=profiles_to_recommendate[i]['student_id']).values('user_id'))
            id = id[0]['user_id']
            user = serializers.serialize('json',
                                         User.objects.filter(id=id))
            data = {"student": student, 'user': user}
            ptr.append(data)
            print(student)
            i += 1

    except Exception as e:
        e.__str__()
    return ptr
