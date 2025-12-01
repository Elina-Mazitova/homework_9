from models.user import User
from pages.registration_page import RegistrationPage

def test_registration_high_level():
    student = User(
        first_name='Elina',
        last_name='QA',
        email='elina.qa@example.com',
        gender='Female',
        phone='9991111111',
        birth_day='14',
        birth_month='June',
        birth_year='1996',
        subjects=['Maths', 'Computer Science'],
        hobbies=['Sports', 'Music'],
        picture='file_resource.jpg',
        address='Oakton, VA',
        state='NCR',
        city='Delhi'
    )

    page = RegistrationPage()
    page.open().register(student).should_have_registered_user(student)
