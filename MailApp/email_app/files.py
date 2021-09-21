def handle_uploaded_file(f):
    with open('temp_plik/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)