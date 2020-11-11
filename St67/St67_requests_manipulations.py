def requests_manipulations():
    import requests, os, io

    path = os.path.join('.', 'St67_requests_manipulations_input.txt')
    with io.open(path, 'r', encoding='utf-8') as inf:
        url = inf.readline().strip()

    r = requests.get(url)
    if r.text != '':
        print(len((r.text).splitlines()))
    else:
        print('Что-то пошло не так %(')
        print(r.url)

requests_manipulations()