import requests


def get_ortodont():
    cookies = {
        'csrftoken': 'NOTPROVIDED',
    }

    headers = {
        'authority': 'kalmdoctor.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'csrftoken=NOTPROVIDED',
        'referer': 'https://kalmdoctor.ru/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
    }

    response = requests.get('https://kalmdoctor.ru/schedule/', cookies=cookies, headers=headers)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/css/style.css', headers=headers)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/css/style_vision.css', headers=headers)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/js/app/schedule-built.js', headers=headers)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/ajax-loader.gif', headers=headers)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/css/style_print.css', headers=headers)

    headers = {
        'Referer': '',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_logo.gif', headers=headers)

    headers = {
        'Referer': '',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_h_menu_arrow.png', headers=headers)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/static/css/style.css',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_h_menu_cur.png', headers=headers)

    headers = {
        'Referer': '',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_footer.gif', headers=headers)

    cookies = {
        'csrftoken': 'NOTPROVIDED',
    }

    headers = {
        'authority': 'kalmdoctor.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'csrftoken=NOTPROVIDED',
        'origin': 'https://kalmdoctor.ru',
        'referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'district_form-district_id': '1',
    }

    response = requests.post('https://kalmdoctor.ru/api/clinic_list/', cookies=cookies, headers=headers, data=data)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/static/css/style.css',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_header_fade_1.png', headers=headers)

    cookies = {
        'csrftoken': 'NOTPROVIDED',
    }

    headers = {
        'authority': 'kalmdoctor.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'csrftoken=NOTPROVIDED',
        'origin': 'https://kalmdoctor.ru',
        'referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'clinic_form-clinic_id': '1034',
        'clinic_form-patient_id': '',
        'clinic_form-history_id': '',
    }

    response = requests.post('https://kalmdoctor.ru/api/speciality_list/', cookies=cookies, headers=headers, data=data)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/static/css/style.css',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_header_fade_2.png', headers=headers)

    cookies = {
        'csrftoken': 'NOTPROVIDED',
    }

    headers = {
        'authority': 'kalmdoctor.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'csrftoken=NOTPROVIDED',
        'origin': 'https://kalmdoctor.ru',
        'referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'speciality_form-speciality_id': '47',
        'speciality_form-clinic_id': '1034',
        'speciality_form-patient_id': '',
        'speciality_form-history_id': '',
    }

    response = requests.post('https://kalmdoctor.ru/api/doctor_list/', cookies=cookies, headers=headers, data=data)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/static/css/style.css',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_header_fade_3.png', headers=headers)

    cookies = {
        'csrftoken': 'NOTPROVIDED',
    }

    headers = {
        'authority': 'kalmdoctor.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'csrftoken=NOTPROVIDED',
        'origin': 'https://kalmdoctor.ru',
        'referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'doctor_form-doctor_id': '195',
        'doctor_form-clinic_id': '1034',
        'doctor_form-patient_id': '',
        'doctor_form-history_id': '',
        'doctor_form-appointment_type': '',
    }

    response = requests.post('https://kalmdoctor.ru/api/doctor_schedule/', cookies=cookies, headers=headers, data=data)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/static/css/style.css',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/bg_header_fade_4.png', headers=headers)

    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': 'https://kalmdoctor.ru/static/css/style.css',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://kalmdoctor.ru/static/img/md_buttons.png', headers=headers)

    cookies = {
        'csrftoken': 'NOTPROVIDED',
    }

    headers = {
        'authority': 'kalmdoctor.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'csrftoken=NOTPROVIDED',
        'origin': 'https://kalmdoctor.ru',
        'referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'doctor_form-doctor_id': '206',
        'doctor_form-clinic_id': '1034',
        'doctor_form-patient_id': '',
        'doctor_form-history_id': '',
        'doctor_form-appointment_type': '',
    }

    response = requests.post('https://kalmdoctor.ru/api/doctor_schedule/', cookies=cookies, headers=headers, data=data)

    cookies = {
        'csrftoken': 'NOTPROVIDED',
    }

    headers = {
        'authority': 'kalmdoctor.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'csrftoken=NOTPROVIDED',
        'origin': 'https://kalmdoctor.ru',
        'referer': 'https://kalmdoctor.ru/schedule/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'doctor_form-doctor_id': '195',
        'doctor_form-clinic_id': '1034',
        'doctor_form-patient_id': '',
        'doctor_form-history_id': '',
        'doctor_form-appointment_type': '',
    }

    response = requests.post('https://kalmdoctor.ru/api/doctor_schedule/', cookies=cookies, data=data)

    print(response.status_code)
    print(response.json())


get_ortodont()
