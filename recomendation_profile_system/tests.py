from datetime import datetime

from django.contrib.auth.models import User, Group
from django.test import TestCase

from recomendation_profile_system.models import ProfessionalOffer, Settings
from student.models import Student, Ability
from teacher.models import Teacher

# Create your tests here.
"""
Orden:
Añadir Habilidades
Añadir Usuarios
Añadir estudiantes
Añadir estudiantes
Añadir empleadores

"""


class AddAbilities(TestCase):
    abilities = [];
    #   Gestión de BD:
    abilities.append('Diseño')
    abilities.append('Diseño UI UX')
    abilities.append('SQL')
    abilities.append('Oracle')
    abilities.append('MySql')
    abilities.append('Microsoft SQL Server')
    abilities.append('PostgreSQL')
    abilities.append('SQLite')
    abilities.append('Redis')
    abilities.append('MongoDB')
    abilities.append('AWS RDS')
    #     Programación:
    abilities.append('Python')
    abilities.append('c')
    abilities.append('c++')
    abilities.append('Java')
    abilities.append('C#')
    abilities.append('HTML')
    abilities.append('CSS')
    abilities.append('JavaScript')
    abilities.append('Ruby')
    abilities.append('PHP')
    abilities.append('Swift')
    abilities.append('Go')
    abilities.append('Kotlin')
    abilities.append('R')
    abilities.append('Rust')
    abilities.append('Perl')
    abilities.append('Matlab')
    # Web Development Frameworks:
    abilities.append('React')
    abilities.append('Angular')
    abilities.append('Vue.js')
    abilities.append('Django')
    abilities.append('Node.js')
    abilities.append('Flask')
    abilities.append('ASP.NET Core')
    abilities.append('Spring Boot')
    abilities.append('ASP.NET')
    abilities.append('Laravel')
    abilities.append('Symfony')
    abilities.append('Express')
    #   Mobile Framework
    abilities.append('React Native')
    abilities.append('Flutter')
    abilities.append('Xamarin')
    abilities.append('Ionic')
    abilities.append('NativeScript')
    # Desktop Development Frameworks:
    abilities.append('Electron')
    #   Cloud Platforms and Services:
    abilities.append('Amazon Web Services (AWS)')
    abilities.append('Microsoft Azure')
    abilities.append('Google Cloud Platform (GCP)')
    abilities.append('Heroku')
    abilities.append('IBM Cloud')
    abilities.append('Firebase')
    #   DevOps Tools:
    abilities.append('Docker')
    abilities.append('Kubernetes')
    abilities.append('GitLab CI/CD')
    abilities.append('Travis CI')
    abilities.append('Ansible')
    abilities.append('Puppet')
    abilities.append('Chef')
    #   Testing Frameworks:
    abilities.append('JUnit')
    abilities.append('Selenium')
    abilities.append('Cypress')
    abilities.append('Pytest')
    abilities.append('Jest')
    abilities.append('Mockito')
    #   Frontend Development Tools:
    abilities.append('Sass')
    abilities.append('Less')
    abilities.append('Bootstrap')
    abilities.append('Tailwind CSS')
    abilities.append('Webpack')
    #   Version Control Systems:
    abilities.append('Git')
    abilities.append('Subversion (SVN)')
    abilities.append('Mercurial')
    #   Integrated Development Environments (IDEs):
    abilities.append('Visual Studio')
    abilities.append('Eclipse')
    abilities.append('IntelliJ IDEA')
    abilities.append('NetBeans')
    abilities.append('Android Studio')
    abilities.append('PyCharm')
    abilities.append('PHPStorm')
    abilities.append('Xcode')
    #   Code Editors:
    abilities.append('Visual Studio Code')
    abilities.append('Sublime Text')
    abilities.append('Notepad++')
    abilities.append('Vim')
    abilities.append('Emacs')
    #   APIS
    abilities.append('Postman')
    abilities.append('JSON')
    abilities.append('XML')
    # Redes
    abilities.append('Http')
    abilities.append('Https')
    abilities.append('DNS')
    abilities.append('DHCP')
    abilities.append('Socket')
    abilities.append('Direccionamiento IP')
    abilities.append('Firewall')
    abilities.append('VPN')
    abilities.append('Antivirus')
    abilities.append('IDS')
    abilities.append('IPS')
    #   tools
    abilities.append('Wireshark')
    abilities.append('Nmap')
    abilities.append('Metasploit Framework')
    abilities.append('Nessus')
    abilities.append('Snort')
    abilities.append('Burp Suite')
    abilities.append('OpenVAS')
    abilities.append('Tcpdump')
    abilities.append('Aircrack-ng')
    abilities.append('Splunk')
    abilities.append('ArcSight')
    abilities.append('LogRhythm')
    #   servers
    abilities.append('Apache')
    abilities.append('Nginx')
    abilities.append('Active Directory')
    #   Operative Systems
    abilities.append('Windows Server')
    abilities.append('Linux')
    abilities.append('CenTos')
    abilities.append('CaliLinux')
    abilities.append('Debian')
    abilities.append('Nova')
    abilities.append('Unix')
    abilities.append('FreeBSD')
    abilities.append('VMware ESXi')
    abilities.append('Citrix XenServer')
    abilities.append('IBM z/OS')
    #   Methodologies
    abilities.append('Scrum')
    abilities.append('XP (Programación Extrema)')
    abilities.append('Kanban')
    abilities.append('Lean')
    abilities.append('Crystal')
    abilities.append('Dynamic Systems Development Method (DSDM)')
    abilities.append('Feature Driven Development (FDD)')
    abilities.append('Adaptive Software Development (ASD)')
    abilities.append('Agile Unified Process (AUP)')
    abilities.append('Agile Modeling (AM)')
    abilities.append('Agile Data Method (ADM)')
    abilities.append('Agile Project Management (APM)')
    abilities.append('Lean Software Development (LSD)')
    abilities.append('Scaled Agile Framework (SAFe)')
    abilities.append('Disciplined Agile Delivery (DAD)')
    abilities.append('Nexus')
    abilities.append('RUP')
    abilities.append('AUP UCI')
    # Rolls
    abilities.append('Tester')
    abilities.append('Developer')
    abilities.append('Project manager')
    abilities.append('Desarrollador de software')
    abilities.append('Analista')
    abilities.append('Diseñador')

    Ability.objects.all().delete()
    Settings.objects.all().delete()
    ProfessionalOffer.objects.all().delete()
    User.objects.all().delete()
    Teacher.objects.all().delete()
    Student.objects.all().delete()

    for h in abilities:
        a = Ability(ability=h)
        a.save()


class AddUser(TestCase):
    # 19 usuarios
    u = User(first_name='Yoel', last_name='Alejandro', is_active=True, is_staff=True,
             username='yoel', is_superuser=True)
    u.set_password("12345678")
    u.save()
    Settings.objects.create(user_id=u.pk)

    u2 = User(first_name='Carlos', is_active=True, is_staff=True,
              username='carlos', is_superuser=True)
    u2.set_password("12345678")
    u2.save()
    Settings.objects.create(user_id=u2.pk)

    u3 = User(first_name='Mariem', last_name='', is_active=True, is_staff=True,
              username='mariem', is_superuser=True)
    u3.set_password("12345678")
    u3.save()
    Settings.objects.create(user_id=u3.pk)

    u4 = User(first_name='Jose', last_name='Ricardo', is_active=True, is_staff=True,
              username='jose_ricardo', is_superuser=True)
    u4.set_password("12345678")
    u4.save()
    Settings.objects.create(user_id=u4.pk)

    u5 = User(first_name='Jonathan', is_active=True, is_staff=True,
              username='jonathan', is_superuser=True)
    u5.set_password("12345678")
    u5.save()
    Settings.objects.create(user_id=u5.pk)

    u6 = User(first_name='Gretter', last_name='', is_active=True, is_staff=True,
              username='gretter', is_superuser=True)
    u6.set_password("12345678")
    u6.save()
    Settings.objects.create(user_id=u6.pk)

    u7 = User(first_name='Lorem', is_active=True, is_staff=True,
              username='lorem', is_superuser=True)
    u7.set_password("12345678")
    u7.save()
    Settings.objects.create(user_id=u7.pk)

    u8 = User(first_name='Luis', last_name='Angel', is_active=True, is_staff=True,
              username='luis', is_superuser=True)
    u8.set_password("12345678")
    u8.save()
    Settings.objects.create(user_id=u8.pk)

    u9 = User(first_name='Leonardo', is_active=True, is_staff=True,
              username='leonardo', is_superuser=True)
    u9.set_password("12345678")
    u9.save()
    Settings.objects.create(user_id=u9.pk)

    u10 = User(first_name='Leandro', is_active=True, is_staff=True,
               username='leandro', is_superuser=True)
    u10.set_password("12345678")
    u10.save()
    Settings.objects.create(user_id=u10.pk)

    u11 = User(first_name='Richard', last_name='', is_active=True, is_staff=True,
               username='richard', is_superuser=True)
    u11.set_password("12345678")
    u11.save()
    Settings.objects.create(user_id=u11.pk)

    u12 = User(first_name='Lorena', is_active=True, is_staff=True,
               username='lorena', is_superuser=True)
    u12.set_password("12345678")
    u12.save()
    Settings.objects.create(user_id=u12.pk)

    u13 = User(first_name='Keylin', is_active=True, is_staff=True,
               username='keylin', is_superuser=True)
    u13.set_password("12345678")
    u13.save()
    Settings.objects.create(user_id=u13.pk)

    u14 = User(first_name='Jennifer', is_active=True, is_staff=True,
               username='jennifer', is_superuser=True)
    u14.set_password("12345678")
    u14.save()
    Settings.objects.create(user_id=u14.pk)

    u15 = User(first_name='Heidys', is_active=True, is_staff=True,
               username='heidys', is_superuser=True)
    u15.set_password("12345678")
    u15.save()
    Settings.objects.create(user_id=u15.pk)

    u16 = User(first_name='Juan', last_name='Antonio', is_active=True, is_staff=True,
               username='juan', is_superuser=True)
    u16.set_password("12345678")
    u16.save()
    Settings.objects.create(user_id=u16.pk)

    u17 = User(first_name='Yoan', is_active=True, is_staff=True,
               username='yoan', is_superuser=True)
    u17.set_password("12345678")
    u17.save()
    Settings.objects.create(user_id=u17.pk)

    u18 = User(first_name='Julio', is_active=True, is_staff=True,
               username='julio', is_superuser=True)
    u18.set_password("12345678")
    u18.save()
    Settings.objects.create(user_id=u18.pk)


class AddTeacher(TestCase):
    # 2 Profesores
    users = User.objects.all()
    Teacher.objects.create(profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png', mobile='57121212',
                           address='La Habana', user=users.get(username='julio'),
                           status=True, salary=5000)
    my_teacher_group = Group.objects.get_or_create(name='TEACHER')
    my_teacher_group[0].user_set.add(users.get(username='julio'))

    Teacher.objects.create(profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png', mobile='58909870',
                           address='La Habana', user=users.get(username='yoan'),
                           status=True, salary=5000)
    my_teacher_group = Group.objects.get_or_create(name='TEACHER')
    my_teacher_group[0].user_set.add(users.get(username='yoan'))


class AddStudent(TestCase):
    # 17 Egresados o sus abilidades
    a = Ability.objects.all()
    users = User.objects.all()
    student = Student.objects.create(user=users.get(username='yoel'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='54545454', )
    student.abilities.add(a.get(ability='Laravel'))
    student.abilities.add(a.get(ability='PHP'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='Bootstrap'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='yoel'))

    student = Student.objects.create(user=users.get(username='heidys'), address="Mayabeque",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='54543232', )
    student.abilities.add(a.get(ability='SQL'))
    student.abilities.add(a.get(ability='MySql'))
    student.abilities.add(a.get(ability='PostgreSQL'))
    student.abilities.add(a.get(ability='SQLite'))
    student.abilities.add(a.get(ability='Git'))
    student.abilities.add(a.get(ability='Scrum'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='heidys'))

    student = Student.objects.create(user=users.get(username='carlos'), address="Las Villas",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='58099009', )
    student.abilities.add(a.get(ability='Pytest'))
    student.abilities.add(a.get(ability='Selenium'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='JUnit'))
    student.abilities.add(a.get(ability='Python'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='carlos'))

    student = Student.objects.create(user=users.get(username='luis'), address="Matanzas",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='56464343', )
    student.abilities.add(a.get(ability='Angular'))
    student.abilities.add(a.get(ability='JSON'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='Node.js'))
    student.abilities.add(a.get(ability='Scrum'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='luis'))

    student = Student.objects.create(user=users.get(username='mariem'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='56445640', )
    student.abilities.add(a.get(ability='Python'))
    student.abilities.add(a.get(ability='SQL'))
    student.abilities.add(a.get(ability='PostgreSQL'))
    student.abilities.add(a.get(ability='Django'))
    student.abilities.add(a.get(ability='Flask'))
    student.abilities.add(a.get(ability='Scrum'))
    student.abilities.add(a.get(ability='Git'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='mariem'))

    """student = Student.objects.create(user=users.get(username='jose_ricardo'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='59687967', )
    student.abilities.add(a.get(ability='Symfony'))
    student.abilities.add(a.get(ability='MySql'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='Bootstrap'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='jose_ricardo'))
    """
    student = Student.objects.create(user=users.get(username='jonathan'), address="Pinar del Río",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='56765543', )
    student.abilities.add(a.get(ability='SQL'))
    student.abilities.add(a.get(ability='PostgreSQL'))
    student.abilities.add(a.get(ability='MySql'))
    student.abilities.add(a.get(ability='Nginx'))
    student.abilities.add(a.get(ability='Git'))
    student.abilities.add(a.get(ability='Scrum'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='jonathan'))

    student = Student.objects.create(user=users.get(username='gretter'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='53243212', )
    student.abilities.add(a.get(ability='React'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='JSON'))
    student.abilities.add(a.get(ability='Node.js'))
    student.abilities.add(a.get(ability='Scrum'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='gretter'))

    student = Student.objects.create(user=users.get(username='lorem'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='53079845', )
    student.abilities.add(a.get(ability='Pytest'))
    student.abilities.add(a.get(ability='Selenium'))
    student.abilities.add(a.get(ability='JUnit'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='PHP'))
    student.abilities.add(a.get(ability='Tester'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='lorem'))

    student = Student.objects.create(user=users.get(username='leonardo'), address="Las Villas",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='53122334', )
    student.abilities.add(a.get(ability='Selenium'))
    student.abilities.add(a.get(ability='JUnit'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='Git'))
    student.abilities.add(a.get(ability='Python'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='leonardo'))

    """student = Student.objects.create(user=users.get(username='leandro'), address="Granma",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='58976875', )
    student.abilities.add(a.get(ability='Python'))
    student.abilities.add(a.get(ability='Flask'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='Git'))
    student.abilities.add(a.get(ability='Postman'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='leandro'))

    student = Student.objects.create(user=users.get(username='richard'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='59876509', )
    student.abilities.add(a.get(ability='Python'))
    student.abilities.add(a.get(ability='PHP'))
    student.abilities.add(a.get(ability='Docker'))
    student.abilities.add(a.get(ability='Django'))
    student.abilities.add(a.get(ability='Laravel'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='Git'))
    student.abilities.add(a.get(ability='Scrum'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='richard'))

    student = Student.objects.create(user=users.get(username='lorena'), address="Artemisa",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='55987654', )
    student.abilities.add(a.get(ability='Python'))
    student.abilities.add(a.get(ability='PHP'))
    student.abilities.add(a.get(ability='Apache'))
    student.abilities.add(a.get(ability='Django'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='Git'))
    student.abilities.add(a.get(ability='XML'))
    student.abilities.add(a.get(ability='JSON'))
    student.abilities.add(a.get(ability='Scrum'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='lorena'))

    student = Student.objects.create(user=users.get(username='keylin'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='55987654', )
    student.abilities.add(a.get(ability='Selenium'))
    student.abilities.add(a.get(ability='JUnit'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='PHP'))
    student.abilities.add(a.get(ability='JSON'))
    student.abilities.add(a.get(ability='Tester'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='keylin'))

    student = Student.objects.create(user=users.get(username='jennifer'), address="La habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='55987654', )
    student.abilities.add(a.get(ability='Python'))
    student.abilities.add(a.get(ability='Apache'))
    student.abilities.add(a.get(ability='Docker'))
    student.abilities.add(a.get(ability='Django'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='Git'))
    student.abilities.add(a.get(ability='Scrum'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='jennifer'))"""

    student = Student.objects.create(user=users.get(username='juan'), address="La Habana",
                                     profile_pic='profile_pic/Student/personal_correcto_oKXG8gH.png',
                                     mobile='53243212', )
    student.abilities.add(a.get(ability='Laravel'))
    student.abilities.add(a.get(ability='PHP'))
    student.abilities.add(a.get(ability='HTML'))
    student.abilities.add(a.get(ability='JavaScript'))
    student.abilities.add(a.get(ability='CSS'))
    student.abilities.add(a.get(ability='Bootstrap'))
    student.abilities.add(a.get(ability='Git'))
    my_student_group = Group.objects.get_or_create(name='STUDENT')
    my_student_group[0].user_set.add(users.get(username='juan'))


class AddJobOffer(TestCase):
    # 4 ofertas de trabajo
    abilities = Ability.objects.all()
    teachers = Teacher.objects.all()
    job_offer = ProfessionalOffer.objects.create(modality='Presencial', address='La Habana',
                                                 title='Desarrollador Laravel',
                                                 teacher=teachers.get(user__username='julio'),
                                                 date=datetime.now().date())
    job_offer.abilities.add(abilities.get(ability='Bootstrap'))
    job_offer.abilities.add(abilities.get(ability='HTML'))
    job_offer.abilities.add(abilities.get(ability='CSS'))
    job_offer.abilities.add(abilities.get(ability='JavaScript'))
    job_offer.abilities.add(abilities.get(ability='PHP'))
    job_offer.abilities.add(abilities.get(ability='Laravel'))

    job_offer = ProfessionalOffer.objects.create(modality='Teletrabajo', address='',
                                                 title='Administrador de bases de datos',
                                                 teacher=teachers.get(user__username='julio'),
                                                 date=datetime.now().date())
    job_offer.abilities.add(abilities.get(ability='SQL'))
    job_offer.abilities.add(abilities.get(ability='MySql'))
    job_offer.abilities.add(abilities.get(ability='PostgreSQL'))
    job_offer.abilities.add(abilities.get(ability='SQLite'))
    job_offer.abilities.add(abilities.get(ability='Git'))
    job_offer.abilities.add(abilities.get(ability='Scrum'))

    job_offer = ProfessionalOffer.objects.create(modality='Teletrabajo', address='',
                                                 title='Desarrollador backend',
                                                 teacher=teachers.get(user__username='julio'),
                                                 date=datetime.now().date())
    job_offer.abilities.add(abilities.get(ability='Python'))
    job_offer.abilities.add(abilities.get(ability='SQL'))
    job_offer.abilities.add(abilities.get(ability='PostgreSQL'))
    job_offer.abilities.add(abilities.get(ability='Django'))
    job_offer.abilities.add(abilities.get(ability='Flask'))
    job_offer.abilities.add(abilities.get(ability='Scrum'))
    job_offer.abilities.add(abilities.get(ability='Git'))

    job_offer = ProfessionalOffer.objects.create(modality='Presencial', address='Las Villas', title='Tester',
                                                 teacher=teachers.get(user__username='yoan'),
                                                 description="Tester con alto nivel en Python y Selenium",
                                                 date=datetime.now().date())
    job_offer.abilities.add(abilities.get(ability='Pytest'))
    job_offer.abilities.add(abilities.get(ability='Selenium'))
    job_offer.abilities.add(abilities.get(ability='JUnit'))
    job_offer.abilities.add(abilities.get(ability='HTML'))
    job_offer.abilities.add(abilities.get(ability='JavaScript'))
    job_offer.abilities.add(abilities.get(ability='CSS'))
    job_offer.abilities.add(abilities.get(ability='Python'))

    job_offer = ProfessionalOffer.objects.create(modality='Presencial', address='Matanzas', title='Fullstack',
                                                 teacher=teachers.get(user__username='yoan'),
                                                 date=datetime.now().date())
    job_offer.abilities.add(abilities.get(ability='Angular'))
    job_offer.abilities.add(abilities.get(ability='HTML'))
    job_offer.abilities.add(abilities.get(ability='CSS'))
    job_offer.abilities.add(abilities.get(ability='JavaScript'))
    job_offer.abilities.add(abilities.get(ability='JSON'))
    job_offer.abilities.add(abilities.get(ability='Node.js'))
    job_offer.abilities.add(abilities.get(ability='Scrum'))
