from pages.registration_page import RegistrationPage

def test_registration_mid_level():
    page = RegistrationPage()
    page.open() \
        .fill_first_name('Elina') \
        .fill_last_name('QA') \
        .fill_email('elina.qa@example.com') \
        .select_gender('Female') \
        .fill_phone('9991111111') \
        .fill_birth_date('1996', 'June', '14') \
        .fill_subject('Math') \
        .fill_subject('Computer Science') \
        .choose_hobby('Sports') \
        .choose_hobby('Music') \
        .upload_picture('file_resource.jpg') \
        .fill_address('Oakton, VA') \
        .select_state('NCR') \
        .select_city('Delhi') \
        .submit() \
        .should_have_registered(
            'Elina QA',
            'elina.qa@example.com',
            'Female',
            '9991111111',
            '14 June,1996',
            'Maths, Computer Science',
            'Sports, Music',
            'file_resource.jpg',
            'Oakton, VA',
            'NCR Delhi'
        )
