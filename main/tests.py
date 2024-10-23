from django.test import TestCase
from django.test import SimpleTestCase
from .models import Project, Task, TaskHistory, Profile, User


class ProjectModelTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title='Ariet',
            description='думаем',
            start_date='2024-10-17',
            end_date='2025-01-05',
            status='выполнил'
        )

    def test_title(self):
        self.assertEqual(str(self.project.title), 'Ariet')

    def test_description(self):
        self.assertEqual(str(self.project.description), 'думаем')

    def test_start_end(self):
        self.assertEqual(str(self.project.start_date), '2024-10-17')

    def test_end_date(self):
        self.assertEqual(str(self.project.end_date), '2025-01-05')

    def test_status(self):
        self.assertEqual(str(self.project.status), 'выполнил')


class TaskModelTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title='Ariet',
            description='думаем',
            start_date='2024-10-17',
            end_date='2025-01-05',
            status='зделал'
        )

        self.task = Task.objects.create(
            title='Site_Klub',
            description='Перенашу задачу',
            start_date='2024-10-16',
            end_date='2024-12-31',
            status='Выполнил',
            project=self.project

        )

    def test_title(self):
        self.assertEqual(str(self.task.title), 'Site_Klub')

    def test_description(self):
        self.assertEqual(str(self.task.description), 'Перенашу задачу')

    def test_start_date(self):
        self.assertEqual(str(self.task.start_date), '2024-10-16')

    def test_end_date(self):
        self.assertEqual(str(self.task.end_date), '2024-12-31')

    def test_status(self):
        self.assertEqual(str(self.task.status), 'Выполнил')


class TaskHistoryModelTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title='Ariet',
            description='думаем',
            start_date='2024-10-17',
            end_date='2025-01-05',
            status='зделал'
        )

        self.task = Task.objects.create(
            title='Site_Klub',
            description='Перенашу задачу',
            start_date='2024-10-16',
            end_date='2024-12-31',
            status='Выполнил',
            project=self.project

        )
        self.taskhistory = TaskHistory.objects.create(
            task=self.task,
            status_change_date='2024-12-09 00:00:00',
            old_status='просить помощи',
            new_status='думаем',
            change_by='выполнил'
        )

    def test_status_change_date(self):
        self.assertEqual(self.taskhistory.status_change_date, '2024-12-09 00:00:00')

    def test_old_status(self):
        self.assertEqual(str(self.taskhistory.old_status), 'просить помощи')

    def test_new_status(self):
        self.assertEqual(str(self.taskhistory.new_status), 'думаем')

    def test_change_by(self):
        self.assertEqual(str(self.taskhistory.change_by), 'выполнил')


class ProfileModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='редит',
            password='0909'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            role='Новичок',
            parol='wordkey20099009'

        )

    def test_role(self):
        self.assertEqual(str(self.profile.role), 'Новичок')

    def test_parol(self):
        self.assertEqual(str(self.profile.parol), 'wordkey20099009')

    def test_username(self):
        self.assertEqual(str(self.user.username), 'редит')

    def test_paasword(self):
        self.assertEqual(str(self.user.password), '0909')


class ProjectSimpleTests(SimpleTestCase):
    def test_project_status_code(self):
        response = self.client.get('projects/')
        self.assertEqual(response.status_code, 200)


class TaskSimpleTests(SimpleTestCase):
    def test_task_status_code(self):
        response = self.client.get('tasks/')
        self.assertEqual(response.status_code, 200)


class UserSimpleTests(SimpleTestCase):
    def test_user_status_code(self):
        response = self.client.get('users/')
        self.assertEqual(response.status_code, 200)


class TaskHistorySimpleTests(SimpleTestCase):
    def test_taskhistory_status_code(self):
        response = self.client.get('taskhistorys')
        self.assertEqual(response.status_code, 200)


class ProfileSimpleTests(SimpleTestCase):
    def test_profile_status_code(self):
        response = self.client.get('profiles')
        self.assertEqual(response.status_code, 200)






class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_abaout_page_status_code(self):
        response = self.client.get('about')
        self.assertEquals(response.status_code, 200)